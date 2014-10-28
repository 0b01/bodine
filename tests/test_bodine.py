from bodine import Bodine

def test_bodine():
	test = ["a * situation",
			"a *blatant* attempt to",
			"more often than not"
			]
	testtype = ['WIC','SYN','EXP']
	for i,j in zip(test,testtype):
		print Bodine(i,j).result
if __name__ == '__main__':
	test_bodine()