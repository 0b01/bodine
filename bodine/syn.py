from textblob import Word, TextBlob
import requests
from api import Wordnik, GoogleBooks
from itertools import chain
class Synonyms(object):
	"""returns synonyms of words"""
	def __init__(self, query):
		'''currently only support 1 synonym search per query'''
		if not query:
			raise Exception, 'Empty input.'
		self.query = query
		print query
		self.word = filter(lambda x: x[0]==x[-1]=='*', query.split(' '))[0].replace('*','')

		# find the index of the highlighted word
		index = query.split(' ').index('*'+self.word+'*')
		self.index = index

		blob = TextBlob(query.replace('*',''))
		tags = blob.tags

		potential_synonyms = dict([[i['relationshipType'],i['words']] for i in Wordnik(self.word).result])	
		self.potential_synonyms = list(set(chain(*map(lambda wordtype: potential_synonyms[wordtype], filter( # looks up in dict by mapcatting and drops repeated ones
									lambda key: key in potential_synonyms.keys(), ['synonym','equivalent','same-context'] # if in keys
								))))) # sorry for the expedient code
	def google(self):
		"""Search google for occurences of synonyms"""
		retl = []
		for syn in self.potential_synonyms:
			templ = self.query.split(' ')
			templ[self.index] = syn
			if syn[0] in ['a','e','i','o','u'] and templ[self.index - 1] == 'a':
				templ[self.index - 1] = 'an'
			# print ' '.join(templ)
			retl.append(GoogleBooks(' '.join(templ)).items)
		return sorted(zip(self.potential_synonyms,retl),key = lambda x:x[1],reverse=1)
	def format(self):
		txt = self.google()
		templ = self.query.split(' ')
		retl = []
		for i in txt:
			templ[self.index] = i[0]
			retl.append(' '.join(templ) + '    : %d results' % i[1])
		return '\n'.join(retl)