from flask import render_template
from . import main
from ..requests import get_news
from app.models import sources
#views
@main.route('/')
def index():
  '''
  View function to return the index page
  '''
  title = 'News-Way'
  all_sources = get_news('sources')
  return render_template('index.html',title=title, sources= all_sources)