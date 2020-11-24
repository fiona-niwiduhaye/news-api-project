from flask import render_template
from app import app
from .request import get_sources
from .request import get_articles
from .models import Source,Article

@app.route('/')
def index():
      """
      View root page function that returns the index page and its data
      """
      #Getting source

      sources = get_sources('general')

      return render_template('index.html', sources = sources)

@app.route('/articles/<id>')
def articles(id):
    """
    View Articles page function that returns the source details page and its data
    """
    articles = get_articles(id)
    title= f'{id}'

    return render_template('articles.html', id = id,articles= articles)
