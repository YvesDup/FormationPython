def anagramme(words):
	"""  words contient une liste de mot
	"""
	res = []



	# renvoie les 
	return res


def test_anagramme():
	"""
	"""
	tests = ( # words														res
			(("ecrue", "uni", "nue") , 									[]),
			(("les", "sel", "sell"), 									[["les", "sel"]]),
			(("line", "steres", "tresse", "tres", "lien", "restes"), 	[["lien", "line"], ["restes", "steres", "tresse"]])
	)
	for words, res in tests:
		print(anagramme(words) == res) 

test_anagramme()