"""A module that is a web-based app generating a meme.

A randomly selected image is selected and combined with 
quotes ingested from different types of source formats.
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    images_path = "./_data/photos/dog/"
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(random.choice(quotes))
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)
    

@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    path = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    temp = requests.get(path, stream = True).content
    temp_path = f'./tmp_{random.randint(0,1000000)}.jpg'
    with open(temp_path, 'wb') as f:
        f.write(temp)
    try:
        path = meme.make_meme(temp_path, body, author)
    except PIL.UnidentifiedImageError:
        return render_template('meme.html', path = './static/invalid.png')
    os.remove(temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
