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


    def test_instance_variables(self):

        self.assertEqual(self.new_article.id, 'abc-news')
        self.assertEqual(self.new_article.author, 'The Associated Press')
        self.assertEqual(self.new_article.title, 'This Week: Consumer prices, Delta earns, retail sales')
        self.assertEqual(self.new_article.description, 'The Labour Department issues its monthly index of consumer prices Wednesday')
        self.assertEqual(self.new_article.url, 'https://abcnews.go.com/Travel/wireStory/week-consumer-prices-delta-earns-retail-sales-82173640')
        self.assertEqual(self.new_article.image, 'null')
        self.assertEqual(self.new_article.date, '2022-01-10T05:10:44Z')