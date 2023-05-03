const express = require("express");
const router = express.Router();
const bcrypt = require("bcrypt");

const saltRounds = 10;
const User = require("../models/user");

// print request to console before continuing
router.use((req, res, next) => {
  console.log(`${req.method} ${req.url} ${new Date()}`);
  next();
});

// set the req.locals variables to match the logged in user, or to null if there is no user.
router.use((req, res, next) => {
  if (req.session.username) {
    res.locals.loggedIn = true;
    res.locals.username = req.session.username;
    res.locals.user = req.session.user;
    req.user = req.session.user;
  } else {
    res.locals.loggedIn = false;
    res.locals.username = null;
    res.locals.user = null;
    req.user = null;
  }
  next();
});

// render login form on GET for /login
router.get("/login", (req, res) => {
  res.render("pwlogin");
});

// handle login form data
router.post("/login", async (req, res, next) => {
  try {
    const { username, passphrase } = req.body;
    const user = await User.findOne({ username: username });
    const isMatch = await bcrypt.compare(passphrase, user.passphrase);

    if (isMatch) {
      req.session.username = username;
      req.session.user = user;
      res.redirect("/");
    } else {
      console.log("Incorrect username or password. ");
      req.session.username = null;
      req.session.user = null;
      res.redirect("/login");
    }
  } catch (e) {
    next(e);
  }
});

// handle signup and encrypt password
router.post("/signup", async (req, res, next) => {
  try {
    const { username, passphrase, passphrase2 } = req.body;
    if (passphrase != passphrase2) {
      res.redirect("/login");
    } else {
      const encrypted = await bcrypt.hash(
        passphrase,
        saltRounds,
        (err, hash) => {
          if (err) {
            console.log("Error: ", err);
          } else {
            console.log("Hash: ", hash);
          }
        }
      );

      // check if username isn't already taken
      const duplicates = User.find({ username });

      if (duplicates.length > 0) {
        res.send(
          "Username has already been taken. Please go back and try another username."
        );
      } else {
        // create new user
        const user = new User({
          username: username,
          passphrase: encrypted,
        });

        await user.save();
        req.session.username = user.username;
        req.session.user = user;
        res.redirect("/");
      }
    }
  } catch (e) {
    next(e);
  }
});

//handle logout
router.get("/logout", (req, res) => [req.session.destroy(), res.redirect("/")]);

// middleware for checking if the user is logged in or not
function isLoggedIn(req, res, next) {
  if (res.locals.loggedIn) {
    return next();
  } else {
    res.redirect("/login");
  }
}

router.isLoggedIn = isLoggedIn;

module.exports = router;
