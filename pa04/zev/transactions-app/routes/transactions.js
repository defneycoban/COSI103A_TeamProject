const express = require("express");
const router = express.Router();
const Transaction = require("../models/transaction");

// function for checking if user is logged in
function isLoggedIn(req, res, next) {
  if (res.locals.loggedIn) {
    next();
  } else {
    res.redirect("/login");
  }
}

// helper method to get date formats
function normalizeDate(date) {
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");
  return `${year}-${month}-${day}`;
}

// get the value associated to the key
router.get("/transactions/", isLoggedIn, async (req, res, next) => {
  const sortColumn = req.query.sortBy || "date";
  let data;

  switch (sortColumn) {
    case "description":
      data = {
        description: 1,
        date: -1,
      };
      break;
    case "amount":
      data = {
        amount: 1,
        date: -1,
      };
      break;
    case "category":
      data = {
        category: 1,
        date: -1,
      };
      break;
    default:
      data = {
        date: -1,
        description: 1,
      };
      break;
  }

  let items = await Transaction.find({ userId: req.user._id })
    .sort(data)
    .collation({ locale: "en", strength: 2 });

  res.render("transactionList", { items });
});

// handle POST - adding item
router.post("/transaction", isLoggedIn, async (req, res, next) => {
  const t = new Transaction({
    description: req.body.description,
    amount: req.body.amount,
    category: req.body.category,
    date: req.body.date,
    userId: req.user._id,
  });
  await t.save();
  res.redirect("/transactions");
});

// handle remove item
router.get(
  "/transactions/remove/:itemId",
  isLoggedIn,
  async (req, res, next) => {
    console.log("inside /transactions/remove/:itemId");
    await Transaction.deleteOne({ _id: req.params.itemId });
    res.redirect("/transactions");
  }
);

// handle edit
router.get("/transactions/edit/:itemId", isLoggedIn, async (req, res, next) => {
  console.log("inside /transactions/edit/:itemId");
  const t = await Transaction.findById(req.params.itemId);
  res.locals.item = t;
  res.render("edit", { normalizeDate });
});

// update transaction
router.post(
  "/transactions/updateTransaction",
  isLoggedIn,
  async (req, res, next) => {
    const { itemId, description, amount, category, date } = req.body;
    console.log("inside /transactions/updateTransaction");
    await Transaction.findOneAndUpdate(
      { _id: itemId },
      { $set: { description, amount, category, date } }
    );
    res.redirect("/transactions");
  }
);

router.get("/transactions/byCategory", isLoggedIn, async (req, res, next) => {
  const userId = req.user._id;
  let results = await Transaction.aggregate([
    { $match: { userId: userId } },
    {
      $group: {
        _id: "$category",
        total: { $sum: "$amount" },
      },
    },
  ]);
  console.log(results);

  res.render("byCategory", { results });
});

module.exports = router;
