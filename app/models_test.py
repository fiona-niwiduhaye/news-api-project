import unittest
from models import Source
from models import Article

class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source Class
    """
    def setup(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source("nana","igihe","Test to see if sources is being known","TestUrl","sport")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sourcce,Source))


    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_source.id,"nana")
        self.assertEqual(self.new_source.name,"igihe")
        self.assertEqual(self.new_source.description,"Test to see if Source is being known")
        self.assertEqual(self.new_source.url,"TestUrl")
        self.assertEqual(self.new_source.category,"sport")

class ArticleTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """
    def setup(self):
        """
        Set up method that will run before every Test
        """
        self.new_article = Article("nana","TestTitle","TestDescription","TestUrl","TestUrlToImage","TestPublishedAt","TestContent")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_article.id,"nana")
        self.assertEqual(self.new_article.title,"TestTitle")
        self.assertEqual(self.new_article.description,"TestDescription")
        self.assertEqual(self.new_article.url,"TestUrl")
        self.assertEqual(self.new_article.urlToImage,"TestUrlToImage")
        self.assertEqual(self.new_article.publishedAt,"TestPublishedAt")
        self.assertEqual(self.new_article.content,"TestContent")

    if __name__ == '__main__':

        unittest.main()