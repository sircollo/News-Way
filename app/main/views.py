from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_articles
from ..models import sources,articles
#views
@main.route('/')
def index():
  '''
  View function to return the index page
  '''
  title = 'News-Way'
  tech_sources = get_news('technology')
  business_sources = get_news('business')
  sports_sources = get_news('sports')
  health_sources = get_news('health')
  entertainment_sources = get_news('entertainment')
  general_sources = get_news('general')
  science_sources = get_news('science')
  return render_template('index.html',title=title, tech_news = tech_sources, business_news = business_sources, sports_news = sports_sources,health_news = health_sources, entertainment_news = entertainment_sources, general_news = general_sources, science_news = science_sources)

@main.route('/sources/<id>')
def articles(id):
   '''
   View articles function to return more details of a source
   '''
   articles = get_articles(id)
  #  title = f'{articles.author}'
   return render_template('articles.html', articles=articles)