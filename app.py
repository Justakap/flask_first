from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_data():
    return "data is here"
