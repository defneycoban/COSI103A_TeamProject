/*
  prompt.js -- Router for the Prompt
*/
const express = require('express');
const router = express.Router();
const Prompt = require('../models/Prompt')
const User = require('../models/User')


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

/* add the value in the body to the db associated to the key */
router.post('/prompt',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = new Prompt(
        {item:req.body.item,
         createdAt: new Date(),
         status: true,
         userId: req.user._id
        })
      await todo.save();
      res.redirect('/prompt')
});

router.get('/prompt/byUser',
  isLoggedIn,
  async (req, res, next) => {
      let results =
            await Prompt.aggregate(
                [ 
                  {$group:{
                    _id:'$userId',
                    total:{$count:{}}
                    }},
                  {$sort:{total:-1}},              
                ])
              
        results = 
           await User.populate(results,
                   {path:'_id',
                   select:['username','age']})

        //res.json(results)
        res.render('summarizeByUser',{results})
});



module.exports = router;
