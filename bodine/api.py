import requests

class GoogleBooks():
	'''Calls Google Books unauthorized API and return results
:items  - count of found search terms
:snippets  - returns 10 of the search terms as a preview'''
	searchterm = ''
	items = 0
	snippets=[]
	def __init__(self, searchterm):
		self.searchterm = '"' + searchterm.replace(' ','+') + '"'
		self.__call()
	def __call(self):
		r = requests.get('https://www.googleapis.com/books/v1/volumes?q=%s&maxResults=5&filter=partial' % self.searchterm)
		response = r.json()
		self.items = response['totalItems']
		if 'items' in response.keys():
			for i in response['items']:
				try:
					self.snippets.append( i['searchInfo']['textSnippet'] )
				except KeyError:
					pass

class Google():
	'''Search Google unauthorized API and return results
:items  - count of found search terms'''
	searchterm = ''
	items = 0
	def __init__(self, searchterm):
		self.searchterm = '"' + searchterm + '"'
		self.__call()
	def __call(self):
		r = requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s' % self.searchterm)
		response = r.json()
		self.items = int(response['responseData']['cursor']['estimatedResultCount'])