/*
  prompt.js -- Router for the Prompt
*/
const express = require('express');
const router = express.Router();
const Prompt = require('../models/Prompt')
const User = require('../models/User')
const ChatGPT = require('./chatgpt.js')


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

router.get('/villain', (req,res,next) => {
  res.render('elioraPrompt')
})

router.post('/villain',
  async (req,res,next) => {
    console.log('getting villain')
    res.locals.prompt = req.body.prompt
    result = await get_villain(req.body.prompt)
    console.log('Result:', result); //result is currently undefined :(
    res.render('response', {result})
}
)

//TODO: must be implemented
const get_villain = async (prompt) => {
  const message = 'What would be a good Dungeons and Dragons monster to fight against for:' + prompt;
  const response = await ChatGPT.getChatGPTResponse(message);
  console.log('Response:', response); //response is currently undefined :(
  return response;
};

router.get('/quest', (req,res,next) => {
  res.render('madinaPrompt')
})

router.post('/quest',
  async (req,res,next) => {
    console.log('generating quest')
    res.locals.prompt = req.body.prompt
    result = await get_quest(req.body.prompt)
    console.log('Result:', result); //result is currently undefined :(
    res.render('response', {result})
}
)

//TODO: must be implemented
const get_quest = async (prompt) => {
  const message = 'What could be a DnD quest for:' + prompt;
  const response = await ChatGPT.getChatGPTResponse(message);
  console.log('Response:', response); //response is currently undefined :(
  return response;
};


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
