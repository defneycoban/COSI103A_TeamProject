'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, render_template, url_for, Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def main():
    ''' displays links to index, about, and team '''
    # To edit the webpages, open the linked .html file in the 'templates' folder
    return render_template('home.html')

@app.route('/index')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return render_template('index.html')

@app.route('/about')
def about():
    '''describes our project'''
    return render_template('about.html')

@app.route('/team')
def team():
    '''team bios'''
    return render_template('team.html')

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_response(prompt)
        return render_template('gptdemo_result.html', prompt=prompt, answer=answer)
    else:
        return render_template('gptdemo_prompt.html')
    
@app.route('/setting', methods=['GET', 'POST'])
def setting():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_setting(prompt)
        return render_template('gptdemo_result.html', prompt=prompt, answer=answer)
    else:
        return render_template('gptdemo_prompt_setting.html')
    
@app.route('/villain', methods=['GET', 'POST'])
def villain():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.villain(prompt)
        return render_template('gptdemo_result.html', prompt=prompt, answer=answer)
    else:
        return render_template('gptdemo_prompt_villain.html')
    
@app.route('/quest', methods=['GET', 'POST'])
def quest():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.quest(prompt)
        return render_template('gptdemo_result.html', prompt=prompt, answer=answer)
    else:
        return render_template('gptdemo_prompt_quest.html')
    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)