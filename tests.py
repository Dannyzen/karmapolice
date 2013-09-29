import unittest
from user import dbInsertUser
from db import getEmail, getUserName, validateUser
from testinstances import MongoInstance



class TestKarma(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    # Set up an instance on port 12345
    cls.mongo = MongoInstance(7357)

  @classmethod
  def tearDownClass(cls):
    cls.mongo.terminate()

  def setUp(self):
    # All instance types implement ``flush``
    self.mongo.flush()

  def test_dbInsert(self):
    collection = self.mongo.conn['karma_test']['user']

    email = "staypuffed@marshmellow.com"
    karma = 230
    username = "stayPuffed"
    password = "iaintafraidofnoghosts"
    dbInsertUser(email,password,username, karma)

    self.assertEqual(getEmail(email)['email'], email)
    self.assertEqual(getEmail(email)['karma'],karma)
    self.assertEqual(getUserName(username)['username'],username)

if __name__ == '__main__':
    unittest.main(verbosity=2)
