import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):


    """
    Test Class to test the behavior of the articles class
    """

    def setUp(self):
        self.new_article = Articles('abc-news', 'The Associated Press', 'This Week: Consumer prices, Delta earns, retail sales', 'The Labour Department issues its monthly index of consumer prices Wednesday', 'https://abcnews.go.com/Travel/wireStory/week-consumer-prices-delta-earns-retail-sales-82173640', 'null', '2022-01-10T05:10:44Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
    
