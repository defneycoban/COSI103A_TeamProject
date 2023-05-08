/*
  prompt.js -- Router for the Prompt
*/
const express = require("express");
const router = express.Router();
const Prompt = require("../models/Prompt");
const User = require("../models/User");
const axios = require("axios"); //for API

isLoggedIn = (req, res, next) => {
  if (res.locals.loggedIn) {
    next();
  } else {
    res.redirect("/login");
  }
};

//for importing images from public
router.use(express.static("public"));

//routes for other pages
router.get("/index", (req, res, next) => {
  res.render("index");
});

router.get("/about", (req, res, next) => {
  res.render("about");
});

router.get("/team", (req, res, next) => {
  res.render("team");
});

router.get("/villain", (req, res, next) => {
  console.log("inside villain");
  res.render("elioraPrompt");
});

//Eliora's prompt
router.post("/villain", isLoggedIn, async (req, res, next) => {
  const prompt = req.body.prompt;
  console.log("prompt:", prompt);
  response = await axios.post(
    "http://gracehopper.cs-i.brandeis.edu:3500/openai",
    {
      prompt:
        "What would be a good Dungeons and Dragons monster to fight against for:" +
        prompt,
    }
  );
  result = response.data.choices[0].message.content;
  const message = new Prompt({
    //create a new Prompt item
    question: req.body.prompt,
    category: "villain",
    answer: result,
    createdAt: new Date(),
    userId: req.user._id,
  });
  await message.save();
  res.render("response", { result });
});

//Defne's prompt section
router.get('/hero', (req, res, next) => {
  res.render('defnePrompt')
})

router.post('/hero',
isLoggedIn,
  async (req,res,next) => {
    const prompt = req.body.prompt;
    console.log('prompt:', prompt)
    response =
await axios.post('http://gracehopper.cs-i.brandeis.edu:3500/openai',
{prompt:'Generate a hero for a dungeons and dragons hero with the following characteristics:' + prompt})
      result = response.data.choices[0].message.content
      const message = new Prompt( //create a new Prompt item
        {question:req.body.prompt,
          category: 'hero',
          answer: result,
          createdAt: new Date(),
          userId: req.user._id
        }
      )
      await message.save();
      res.render('response', {result})
}
)
//end of Defne's section

router.get("/quest", (req, res, next) => {
  res.render("madinaPrompt");
});

//Madina's prompt
router.post("/quest", 
  isLoggedIn, 
  async (req, res, next) => {
    const prompt = req.body.prompt;
    console.log("prompt:", prompt);
    response = await axios.post(
      "http://gracehopper.cs-i.brandeis.edu:3500/openai",
      {
        prompt:
          "What could be a Dungeons and Dragons quest for:" + prompt,
      }
    );
    result = response.data.choices[0].message.content;
    const message = new Prompt({
      question: req.body.prompt,
      category: "quest",
      answer: result,
      createdAt: new Date(),
      userId: req.user._id,
    });
    await message.save();
    res.render("response", { result });
});

// end of Madina's prompt


router.get("/setting", async (req, res, next) => {
  res.render("zevPrompt");
});

router.post("/setting", async (req, res, next) => {
  console.log("getting setting");
  const prompt = req.body.prompt;
  response = await axios.post(
    "http://gracehopper.cs-i.brandeis.edu:3500/openai",
    {
      prompt: "Give a dnd setting for the following character(s): " + prompt,
    }
  );
  let result = response.data.choices[0].message.content;
  const message = new Prompt({
    question: prompt,
    category: "setting",
    answer: result,
    createdAt: new Date(),
    userId: req.user._id,
  });
  await message.save();
  res.render("response", { result });
});

const getSetting = async (prompt) => {
  const message =
    "Give a dnd setting for the following character(s): " + prompt;
  const response = await getResponse(message);
  console.log("Response:", response);
  return response;
};

//////////////////////////////////////////////////
//////////////////////////////////////////////////
//////////////////////////////////////////////////

router.get("/prompt/byUser", isLoggedIn, async (req, res, next) => {
  let results = await Prompt.aggregate([
    {
      $group: {
        _id: "$userId",
        total: { $count: {} },
      },
    },
    { $sort: { total: -1 } },
  ]);

  results = await User.populate(results, {
    path: "_id",
    select: ["username", "age"],
  });

  //res.json(results)
  res.render("summarizeByUser", { results });
});

router.get("/prompt/byCategory", isLoggedIn, async (req, res, next) => {
  res.locals.show = req.query.show;
  const sortBy = "category";
  const sortOrder = "asc";
  results = await Prompt.find({ userId: req.user._id }).sort({
    [sortBy]: sortOrder,
  });
  res.render("byCategory", { results });
});

module.exports = router;
