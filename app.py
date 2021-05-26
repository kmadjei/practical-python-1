import os
import json
from flask import Flask, render_template, request, flash

# Init App
app = Flask(__name__)


@app.route('/')
def home():
    return 'hello' 


# Run server
if __name__ == '__main__':
    app.run(debug=True)