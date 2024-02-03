from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       text = request.form.get("fname")
       
       return "Text "+ str(text)

app.run(debug=True)