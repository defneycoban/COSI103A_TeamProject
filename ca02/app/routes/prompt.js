/*
  prompt.js -- Router for the Prompt
*/
const express = require('express');
const router = express.Router();
const Prompt = require('../models/Prompt')
const User = require('../models/User')
const axios = require('axios')  //for API

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

//for importing images from public
router.use(express.static('public'));

//routes for other pages
router.get('/index', (req,res,next) => {
  res.render('index')
})

router.get('/about', (req,res,next) => {
  res.render('about')
})

router.get('/team', (req,res,next) => {
  res.render('team')
})

router.get('/villain', (req,res,next) => {
  console.log('inside villain')
  res.render('elioraPrompt')
})

//Eliora's prompt
router.post('/villain',
isLoggedIn,
  async (req,res,next) => {
    const prompt = req.body.prompt;
    console.log('prompt:', prompt)
    response =
await axios.post('http://gracehopper.cs-i.brandeis.edu:3500/openai',
{prompt:'What would be a good Dungeons and Dragons monster to fight against for:' + prompt})
      result = response.data.choices[0].message.content
      const message = new Prompt( //create a new Prompt item
        {question:req.body.prompt,
          category: 'villain',
          answer: result,
          createdAt: new Date(),
          userId: req.user._id
        }
      )
      await message.save();
      res.render('response', {result})
}
)

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
