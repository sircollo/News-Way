# from concurrent.futures import process
import urllib.request,json
from app.models.sources import Sources

#get api key
api_key = None

#get news base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
  

def get_news(sources):
    '''
    Function that gets the json response
    '''
    get_news_url = base_url.format(sources,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
      get_news_data = url.read()
      get_news_response = json.loads(get_news_data)
    
      news_results = None
    
      if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        print(news_results_list)
        news_results = process_results(news_results_list)
        
    return news_results

def process_results(news_list):
    news_results = []
    for news_source in news_list:
      id = news_source.get('id')
      name = news_source.get('name')
      description = news_source.get('description')
      url = news_source.get('url')
      category = news_source.get('category')
      language = news_source.get('language')
      country = news_source.get('country')
      
      news_object = Sources(id,name,description,url,category,language,country)
      news_results.append(news_object)
      
    return news_results