import os
class Config:

    """
    General configuration parent class
    
    """
    # https://newsapi.org/v2/top-headlines/sources?apiKey=9f7096c15e1a4c23ae04d85928067e62

    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):

     pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}  
