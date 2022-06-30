def anagramme(words):
	"""  words contient une liste de mot
	"""
	res = []
	# il faut le même nombre de lettre
	# le tri des lettres du mot et on va comparer avec le tri des lettres d'un autre mot
	# creer un dictionnaire:
	# key: le mot trié par lettre sous la forme: tuple(sorted(word))
	# value: une liste de mots sous la forme [word1, word2, ...]
	dword = {}
	for word in words:
		pass

	# renvoie les values du dictionnaire si la longueur est supérieure à 1

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