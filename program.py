from flask import Flask
from flask import render_template
from flask import request

from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger

import run_pipeline
from spacy_llm.util import assemble

import re

__all__ = ["run_pipeline"]
nlp = assemble("config.cfg")

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/try-it', methods = ['GET', 'POST'])
def tryIt():
    if request.method == "POST":
        text =  request.form["textbox"]
        if not bool(re.match('^\s+$', text)):
            doc = nlp(text)
            sentiment = TextBlob(text).sentiment
            filter = False
            categories = []
            for k,v in doc.cats.items():
                if v == 1:
                    categories.append(k)
            print(categories)
            print(sentiment)
            if len(categories) > 0 or sentiment.polarity < -0.75:
                filter = True


            return render_template("try-it.html", data = {"textInput" : text,
                                                        "pol" : round(sentiment.polarity, 3),
                                                        "subj" : round(sentiment.subjectivity, 3),
                                                        "cats" : categories,
                                                        "filter": filter})
    
    return render_template("try-it.html", data = {"textInput" : ""})

app.run()
