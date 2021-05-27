# modules required to run the app
import os
import json
from flask import Flask, render_template, request
from random import random
import math


# Init App
app = Flask(__name__)

# renders the home page
@app.route('/')
def home():
    msg1 = 'Welcome !'
    msg2 = 'To the world of Flask and Python.'
    return render_template('home.html', msg1=msg1, msg2=msg2)


# renders the confirmation page for the form submitted
@app.route('/form_submission', methods=['GET', 'POST'])
def form_submission():
    
    msg1 = f"Hello {request.form.get('name')} !"
    msg2 = f"We now know you like --> {request.form.get('favorite_activity')}"
    return render_template('form_submitted.html', msg1=msg1, msg2=msg2)


# renders the quotes HTML page
@app.route('/inspirational_quote')
def get_inspired():
    
    # reads the quotes from the JSON data file
    with open('data/quotes.json', 'r') as json_data:
        data = json.load(json_data)
        #generate random number for dict length
        random_quote = math.floor(random()*len(data))

    msg1 = "Your Inspiration For Today !"
        
    return render_template('quotes.html', msg1=msg1, quote=data[random_quote])


# Run server
if __name__ == '__main__':
    app.run(debug=True)
