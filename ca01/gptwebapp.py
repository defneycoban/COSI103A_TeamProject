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
        # return f'''
        # <h1>GPT Demo</h1>
        # <pre style="bgcolor:yellow">{prompt}</pre>
        # <hr>
        # Here is the answer in text mode:
        # <div style="border:thin solid black">{answer}</div>
        # Here is the answer in "pre" mode:
        # <pre style="border:thin solid black">{answer}</pre>
        # <a href={url_for('gptdemo')}> make another query</a>
        # <br>
        # <a href={url_for ('index')}> go to the main page</a>
        # '''
    else:
        return render_template('gptdemo_prompt.html')
        # return '''
        # <h1>GPT Demo App</h1>
        # Enter your query below
        # <form method="post">
        #     <textarea name="prompt"></textarea>
        #     <p><input type=submit value="get response">
        # </form>
        # '''
    
@app.route('/summary', methods=['GET', 'POST'])
def summary():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_encyclopedia_entry(prompt)
        return render_template('gptdemo_result.html', prompt=prompt, answer=answer)
        # return f'''
        # <h1>GPT Demo</h1>
        # <pre style="bgcolor:yellow">{prompt}</pre>
        # <hr>
        # Here is the answer in text mode:
        # <div style="border:thin solid black">{answer}</div>
        # Here is the answer in "pre" mode:
        # <pre style="border:thin solid black">{answer}</pre>
        # <a href={url_for('summary')}> make another summary</a>
        # <br>
        # <a href={url_for ('index')}> go to the main page</a>
        # '''
    else:
        return render_template('gptdemo_prompt_summary.html')
        # return '''
        # <h2>GPT summary</h2>
        # <p>Enter a topic below, and hit submit for a summary.</p>
        # <form method="post">
        #     <input name="prompt" type="text" placeholder="Example: Brandeis University">
        #     <input type=submit value="get response">
        # </form>
        # '''

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.compare_these(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('compare')}> make another comparison</a>
        <br>
        <a href={url_for ('index')}> go to the main page</a>
        '''
    else:
        return '''
        <h2>GPT Comparison</h2>
        <p>Enter two topics below, and hit submit for a comparison.</p>
        <form method="post">
            <input name="prompt" type="text" placeholder="Example: Monkeys and cats">
            <input type=submit value="get response">
        </form>
        '''
    
@app.route('/joke', methods=['GET', 'POST'])
def joke():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.joke(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('joke')}> tell another joke</a>
        <br>
        <a href={url_for ('index')}> go to the main page</a>
        '''
    else:
        return '''
        <h2>GPT Comparison</h2>
        <p>Enter a topic below, and hit submit to see what joke GPT comes up with!</p>
        <form method="post">
            <input name="prompt" type="text" placeholder="Example: Monkeys in space">
            <input type=submit value="get response">
        </form>
        '''
    
@app.route('/story', methods=['GET', 'POST'])
def story():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.story(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('story')}> tell another story</a>
        <br>
        <a href={url_for ('index')}> go to the main page</a>
        '''
    else:
        return '''
        <h2>GPT Comparison</h2>
        <p>Enter a topic below, and hit submit to see what story GPT comes up with!</p>
        <form method="post">
            <input name="prompt" type="text" placeholder="Example: Monkeys in space">
            <input type=submit value="get response">
        </form>
        '''   

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)