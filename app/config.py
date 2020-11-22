class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_LINK='https://newsapi.org/v2/sources?category=general&apiKey={}'

    ARTICLE_API_BASE_URL= 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    

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
    NEWS_API_LINK='https://newsapi.org/v2/sources?category=general&apiKey={}'

    DEBUG = True