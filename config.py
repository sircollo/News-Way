import os

from instance.config import NEWS_API_KEY

class Config:
  
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
  




class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True
  
config_options = {
    'development':DevConfig,
    'production':ProdConfig
  }