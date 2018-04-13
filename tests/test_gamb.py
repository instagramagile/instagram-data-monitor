import unittest
import os
from gambs.valor1 import ator_from_url

class TesteAtor(unittest.TestCase):
	def teste_nome(self):
		usuario=ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual('oimundoembr', usuario.nome)
		os.system("rm *.html")

	def teste_seguidores(self):
		usuario=ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual(0, usuario.seg)
		os.system("rm *.html")

	def teste_postagens(self):
		usuario=ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual(0, usuario.post)
		os.system("rm *.html")

