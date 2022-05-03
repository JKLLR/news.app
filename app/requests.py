import urllib.request,json
from .models import Source, Articles

#Getting api key

api_key = None
base_url= None
articles_url= None

def configure_request(app):
    global api_key, base_url,articles_url
    api_key= app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']




def get_sources(category):

    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
       get_sources_data = url.read()
       get_sources_response = json.loads(get_sources_data)


       source_results = None

       if get_sources_response['sources']:
           sources_results_list = get_sources_response['sources']
           source_results = process_sources(sources_results_list)

    return source_results  


def process_sources(sources_list):


    source_results = []
    for source_item in sources_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url=source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')

        sources_object = Source(id, name, description, url, category, country, language)

        source_results.append(sources_object)


    return source_results

def get_article(id):

    get_article_details_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        get_article_data = url.read()
        get_articles_response = json.loads(get_article_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results


def process_articles(articles_list):

    articles_results = []

    for article_item in articles_list:
          id = article_item.get('id')
          author = article_item.get('author')
          title = article_item.get('title')
          description = article_item.get('description')
          url = article_item.get('url')
          image = article_item.get('urlToImage')
          date = article_item.get('publishedAt')


    

          if image:
            articles_result = Articles(id, author, title, description, url, image, date)

            articles_results.append(articles_result)

    return articles_results