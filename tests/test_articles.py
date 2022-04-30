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
    self.new_article = Articles('techcrunch','TechCrunch','Greg Kumarak',"Elon's big week - TechCrunch",'TechCrunch Week in Review welcomes its new host, Greg Kumparak','https://techcrunch.com/2022/04/30/elons-big-week/','https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600",','2022-04-30T20:07:58Z','Hi!\r\nI’m Greg Kumparak.\r\nI’ll be heading up Week in Review for the foreseeable future')
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))
  