def anagramme(words):
	"""  words contient une liste de mot
	"""

	# - eliminer les doublons
	swords = set(words)

	# - creer des couples (lettres-triees, mot) pour chaque mot
	# - creer un doct dont la cle est lettres-triees et les valeurs list de mots
	dword = {} # k = lettre-triees, v = list des mots
	for word in swords:
		# fabrique la clé
		k = tuple(sorted(word))

		# verifie si la cle est dans le dict dword
		if k not in dword:
			dword[k] = []
		dword[k].append(word)

	# renvoie les lists ou il y a plus de 1 mot
	res = []
	for l in dword.values():
		if len(l) > 1:
			res.append(sorted(l))

	return res


def test_anagramme():
	"""
	"""
	tests = ( # words														res
			(("ecrue", "uni", "nue") , 									[]),
			(("les", "sel", "sell", 'les'), 							[["les", "sel"]]),
			(("line", "steres", "tresse", "tres", "lien", "restes"), 	[["lien", "line"], ["restes", "steres", "tresse"]])
	)
	for words, res in tests:
		print(anagramme(words))
		assert(anagramme(words) == res) 

test_anagramme()