from bodine.api import *
from pprint import pprint

def test_resultcount():
	words = ['a difficult situation','an awkward situation','a serious situation','an embarassing situation','a delicate situation']
	print words
	print [GoogleBooks(i).items for i in words]
def test_googleresultcount():
	words = ['a difficult situation','an awkward situation','a serious situation','an embarassing situation','a delicate situation']
	print words
	print [Google(i).items for i in words]
def test_wildcard():
	for i,j in GoogleBooksWildcard('a rather * situation').matches:
		print i, '|' ,j
if __name__ == '__main__':
	test_wildcard()