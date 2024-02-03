from flask import Flask
from flask import render_template
from flask import request

from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
       text =  request.form["textbox"]
       sentiment = TextBlob(text).sentiment

       return render_template("index.html", data = {"textInput" : text,
                                                    "pol" : round(sentiment.polarity, 3),
                                                    "subj" : round(sentiment.subjectivity, 3),})
    
    return render_template("index.html", data = {"textInput" : ""})

app.run(debug=True)