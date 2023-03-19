'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY='.......'  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY='.....' # in powershell
% python gpt.py
'''
import os
import openai


class GPT:
    '''make queries to gpt from a given API'''

    def __init__(self, apikey):
        '''store the apikey in an instance variable'''
        self.apikey = apikey
        # Set up the OpenAI API client
        openai.api_key = apikey  # os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = 'text-davinci-003'

    def get_response(self, prompt):
        '''Generate a GPT response'''
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8,
        )

        response = completion.choices[0].text
        return response

    # Zev's method
    def get_setting(self, prompt):
        '''The user inputs a subject, and gpt returns a brief summary of it.'''
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = 'Give a dnd setting for the following character(s): ' + prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8,
        )

        response = completion.choices[0].text
        return response
    
    #Eliora's method
    def villain(self, prompt):
        '''The user inputs one or more characters, and gpt returns a villain.'''
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = 'What would be a good Dungeons and Dragons monster to fight against for:' + prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8,
        )

        response = completion.choices[0].text
        return response

     # Madina's method
    def quest(self, prompt):
        '''The user inputs DnD character names/wish in which direction to head for the quest.'''
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = 'What could be a DnD quest for:' + prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8,
        )

        response = completion.choices[0].text
        return response

    #Defne's method
    def hero(self, prompt):
        '''The user inputs a DnD character names/wish in which direction to head for the quest.'''
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = 'What would be a a good Dungeons and Dragons hero give that they are:' + prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8,
        )

        response = completion.choices[0].text
        return response

if __name__ == '__main__':
    g = GPT(os.environ.get('APIKEY'))