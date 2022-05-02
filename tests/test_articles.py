import unittest
from app.models.articles import Articles

class ArticlesTest(unittest.TestCase):
  '''
  Test class to test articles behaviour
  '''
  
  def setUp(self):
    '''
    setup method to run before each test
    '''
    self.new_article = Articles('cnn','CNN staff',"READ: Biden's full White House Correspondents' Dinner remarks",'President Joe Biden spoke Saturday at the White House Correspondent','www.cnn.com','www.cnn.com','2022-05-01T16:34:25Z')
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))
  