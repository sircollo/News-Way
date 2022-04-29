import os

from instance.config import NEWS_API_KEY

class Config:
  
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY') 




class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True
  
config_options = {
    'development':DevConfig,
    'production':ProdConfig
  }