import unittest
from instagram.instagram import InstagramUser

class TestInstagramUser(unittest.TestCase):
	def test_isonline(self):
		user = InstagramUser('oimundoembr')

	def test_name_retrieval(self):
		user = InstagramUser('oimundoembr')
		self.assertEqual('oimundoembr', user.name)

	def test_id_retrieval(self):
		user = InstagramUser('oimundoembr')
		self.assertEqual('7343684346', user.id)
		

if __name__ == '__main__':
    unittest.main()