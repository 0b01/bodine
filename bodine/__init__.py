from api import *


class Bodine(object):
	"""sorts out the formats and functions to use"""
	def __init__(self, query, task):
		'''	query:	the selected words
			type:	NOR	(# of results)
					SC	(SPELL CHECK, AUTO)
					EX	(EXAMPLES)
					WIC	(WORDS IN CONTEXT)
					SYN	(SYNONYMS IN CONTEXT)'''
		self.query = query
		self.task = task # self.__judge()
		self.result = self.__do()
	def __judge(self):
		'''Returns the type based on the query. Doesn't work very well.'''
		if ' * ' in self.query:
			return 'WIC'
		elif '*' in self.query and any(map(lambda x: x[0]==x[-1]=='*',self.query.split(' '))):
			return 'SYN'
	def __do(self):
		if self.task == 'NOR':
			return Google(self.query).items
		elif self.task == 'SC':
			raise Exception, 'NOT YET IMPLEMENTED'
		elif self.task == 'EX':
			return GoogleBooks(self.query).snippets
		elif self.task == 'WIC':
			return GoogleBooksWildcard(self.query).matches
		elif self.task == 'SYN':
			raise Exception, 'NOT YET IMPLEMENTED'
		else:
			raise Exception, 'Unspecified task. {REFRAIN}'