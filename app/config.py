import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_LINK='https://newsapi.org/v2/sources?category={}&apiKey={}'

    ARTICLE_API_BASE_URL= 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
class ProdConfig:
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass

class DevConfig:
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_LINK='https://newsapi.org/v2/sources?category={}&apiKey={}'

    ARTICLE_API_BASE_URL= 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    DEBUG = True