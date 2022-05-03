import unittest

from  app.models import Source

class SourceTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('abc-news-au', 'ABC News (AU)', 'Australia most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.', 'http://www.abc.net.au/news', 'general', 'au', 'en')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_instance_variables(self):

        self.assertEqual(self.newsource.id, 'abc-news-au')
        self.assertEqual(self.new_source.name, 'ABC News (AU)')
        self.assertEqual(self.new_source.description, 'Australia most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')
        self.assertEqual(self.new_source.url, 'http://www.abc.net.au/news')
        self.assertEqual(self.new_source.category, 'general')
        self.assertEqual(self.new_source.country, 'au')
        self.assertEqual(self.new_source.language, 'en')