import requests
import re


class GoogleBooks():
	'''Calls Google Books unauthorized API and return results
:items  - count of found search terms
:snippets  - returns 10 of the search terms as a preview'''
	searchterm = ''
	items = 0
	snippets=[]
	def __init__(self, searchterm):
		self.searchterm = '"' + searchterm + '"'
		self.url = 'https://www.googleapis.com/books/v1/volumes?q=allintext:%s&maxResults=10&filter=partial' % self.searchterm
		self.__call()
	def __call(self):
		r = requests.get(self.url)
		response = r.json()
		self.items = response['totalItems']
		if 'items' in response.keys():
			for item in response['items']:
				try:
					self.snippets.append( item['searchInfo']['textSnippet'] )
				except KeyError:
					pass
class GoogleBooksWildcard():
	'''i.e.
	it is perfectly * to
:items  - count of found search terms
:snippets  - returns 10 of the search terms as a preview'''
	searchterm = ''
	items = 0
	snippets=[]
	matches=[]
	def __init__(self, searchterm):
		self.searchterm = searchterm
		self.max = 5
		self.url = 'https://www.googleapis.com/books/v1/volumes?q=allintext:"%s"&maxResults=%d&filter=partial' % (self.searchterm, self.max)
		if self.__call():
			self.__sort()
	def __call(self):
		r = requests.get(self.url)
		response = r.json()
		self.items = response['totalItems']
		if 'items' in response.keys():
			for item in response['items']:
				try:
					self.snippets.append( item['searchInfo']['textSnippet'] )
				except KeyError:
					pass
			return True
		return False
	def __sort(self):
		highlights = []
		self.regex = re.compile( 
					'.*?(' + \
						self.searchterm.replace('*','(\w*?)')\
						.replace('.','\.') + \
					').+' ) # .+(a rather (.*?) situation).+
		for snippet in [snippet.encode('utf-8').replace('<br>\n','').replace('<b>','').replace('</b>','') for snippet in self.snippets]:
			try:
				bold = self.regex.match(snippet, re.I).group(1) # -> a rather manageable situation
			except Exception:
				continue
			if bold.lower() not in highlights: # who likes undulating recurrances?
				self.matches.append([bold,snippet])
				highlights.append(bold.lower())
	#TODO: regex match to only 1 word perw

class Google():
	'''Search Google unauthorized API and return results
:items  - count of found search terms'''
	searchterm = ''
	items = 0
	def __init__(self, searchterm):
		self.searchterm = '"' + searchterm + '"'
		self.url = 'https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s' % self.searchterm
		self.__call()
	def __call(self):
		r = requests.get(self.url)
		response = r.json()
		self.items = int(response['responseData']['cursor']['estimatedResultCount'])
class Synonyms(object):
	"""returns synonyms of words"""
	def __init__(self, arg):
		self.arg = arg

class Bodine(object):
	"""sorts out the formats and functions to use"""
	def __init__(self, input):
		self.input = input
		self.task()
	def task(self):
		pass