import unittest
from app.models.sources import Sources

class SourcesTest(unittest.TestCase):
  '''
  Test Class to test sources class behaviour
  '''
  def setUp(self):
    '''
    method to run before every test
    '''
    self.new_sources = Sources("abc-news","ABC News","Your trusted source for … videos at ABCNews.com.","https://abcnews.go.com/","general","en","us")
    print("try")
  def test_instance(self):
    self.assertTrue(isinstance(self.new_sources,Sources))
    

