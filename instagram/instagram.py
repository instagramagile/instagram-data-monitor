from __future__ import absolute_import
import os
import json
import re
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class InstagramUser:

	def __init__(self,username):

		logging.debug('Retrieving valid access_token for API access')
		
		insta_user='instagramagile@gmail.com'
		insta_password='instagramagile12018'
		client_id='d92560af65cd4a86ba1a3b54bf6a4b57'
		redirect_uri='https://github.com/Douglasbraga94/instagram-data-monitor/blob/master/.gitignore'

		authorize_login_url = 'https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=token&scope=basic+public_content'	% (client_id, redirect_uri)

		options = Options()  
		options.add_argument("--headless")
		options.binary_location = '/usr/bin/google-chrome'

		driver = webdriver.Chrome(executable_path=os.path.abspath("drivers/linux-64/chromedriver"), options=options)
		driver.get(authorize_login_url)

		user_fld = driver.find_element_by_xpath('//*[@name="username"]')
		pass_fld = driver.find_element_by_xpath('//*[@name="password"]')
		login_btn = driver.find_element_by_xpath('//*[@value="Log in"]')
		user_fld.send_keys(insta_user)
		pass_fld.send_keys(insta_password)

		login_btn.click()
		current_url = driver.current_url

		access_token = re.match('.*#access_token=(.*)',current_url).group(1)

		logging.debug('access_token retrieved: %s' % access_token)

		# Buscar user_id a partir de um user_name.
		logging.debug('Retrieving %s\'s user id' % username)
		response = requests.get('https://www.instagram.com/%s/?__a=1' % username)
		user = response.json()
		user_id = user['user']['id']
		logging.debug('%s\'s id is %s' % (username,user_id))

		# Buscar o que interessa.
		logging.debug('Retrieving %s\'s user data' % username)
		response = requests.get('https://api.instagram.com/v1/users/%s/?access_token=%s' % (user_id,access_token))
		user = response.json()
		logging.debug('%s\'s user data: %s' % (username, user))

		self.id = user['data']['id']
		self.username = user['data']['username']
		self.name = 'oimundoembr'
