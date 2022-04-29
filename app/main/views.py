from flask import render_template
from . import main

#views
@main.route('/')
def index():
  '''
  View function to return the index page
  '''
  title = 'News-Way'
  return render_template('index.html',title=title)