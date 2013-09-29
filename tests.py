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
    collection = self.mongo.conn['karma_test']['user']
    email = "staypuffed@marshmellow.com"
    karma = 2430
    username = "stayPuffed"
    password = "iaintafraidofnoghosts"
    #need to use the local mongo instance and not use any dbInsert functions as they map to my appDB
    dbInsertUser(email,password,username, karma)


  def test_getEmail(self):
    collection = self.mongo.conn['karma_test']['user']
    email = "staypuffed@marshmellow.com"
    karma = 2430
    password = "iaintafraidofnoghosts"
    self.assertEqual(getEmail(email)['email'], email)
    self.assertEqual(getEmail(email)['karma'],karma)

    instance.flush()
    instance.terminate()

  def test_getUserName(self):
    username = "stayPuffed"
    self.assertEqual(getUserName(username)['username'],username)
    instance.flush()
    instance.terminate()

  def test_validateUser(self):
    password = "iaintafraidofnoghosts"
    email = "staypuffed@marshmellow.com"
    self.assertTrue(validateUser(password,email))
    self.mongo.flush()
    nstance.flush()
    instance.terminate()

if __name__ == '__main__':
    unittest.main(verbosity=2)
