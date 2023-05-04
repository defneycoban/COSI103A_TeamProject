const axios = require('axios'); //hoping this is allowed

const api_key = process.argv[2];

async function getChatGPTResponse(prompt) {
    console.log('prompt:', prompt);
    console.log('getting gpt response');
    console.log('api_key:', api_key);
    try {   //something's wrong here
      const response = await axios.post('https://api.openai.com/v1/engine/text-davinci-003/completions', {
        prompt: prompt,
        max_tokens: 1024,
        n: 1,
        temperature: 0.8,
      }, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ${api_key}'   //need to set API-KEY
        }
      });
      console.log('first response:', response.data.choices[0].text);
      return response.data.choices[0].text;
    } catch (error) {
      console.error(error);
    }
  }

  module.exports = {
    getChatGPTResponse
  };