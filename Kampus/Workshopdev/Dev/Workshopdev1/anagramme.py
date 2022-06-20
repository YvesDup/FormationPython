def anagramme(words):
	"""  words contient une liste de mot
	"""
	res = []



	# renvoie les 
	return res


def test_anagramme():
	"""
	"""
	tests = (
			(("ecrue", "uni", "nue") , 									[]),
			(("les", "sel", "sell"), 									[["les", "sel"]]),
			(("line", "steres", "stress", "tres", "lien", "restes"), 	[["lien", "line"], ["restes", "steres", "stress"]])
	)
	for words, res in :
		print(anagramme(words) == res) 

test_anagramme()