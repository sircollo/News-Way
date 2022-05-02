import urllib.request,json
from app.models.sources import Sources
from app.models.articles import Articles

#get api key
api_key = None

#get news base url
base_url = None


def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
  

def get_news(category):
    '''
    Function that gets the json response
    '''
    get_news_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
      get_news_data = url.read()
      get_news_response = json.loads(get_news_data)
    
      news_results = None
    
      if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        # print(news_results_list)
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
  
def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
      articles_results = json.loads(url.read())


      articles_object = None
      if articles_results['articles']:
        articles_object = process_articles(articles_results['articles'])

    return articles_object

def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = articles_base_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object

def process_articles(articles_list):
    '''
    '''
    articles_object = []
    for article_item in articles_list:
      id = article_item.get('id')
      author = article_item.get('author')
      title = article_item.get('title')
      description = article_item.get('description')
      url = article_item.get('url')
      urlToImage = article_item.get('urlToImage')
      publishedAt = article_item.get('publishedAt')
      
      if urlToImage:
        articles_result = Articles(id,author,title,description,url,urlToImage,publishedAt)
        articles_object.append(articles_result)	      

    return articles_object