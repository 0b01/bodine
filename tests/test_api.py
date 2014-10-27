from bodine.api import GoogleBooks
from pprint import pprint

def test_query():
	words = ['a difficult situation','an awkward situation','a serious situation','an embarassing situation','a delicate situation']
	print [GoogleBooks(i).items for i in words]

if __name__ == '__main__':
	test_query()