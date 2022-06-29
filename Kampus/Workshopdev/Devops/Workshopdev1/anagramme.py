def anagramme(words):
	"""  words contient une liste de mot
	"""
	# pour chaque de la liste, il faut
	dwords = {}

	# emiliner les doublons de mots
	for word in set(words):
		# 1 - calculer son le mot 'triée' 
		sorted_w = tuple(sorted(word))
	
		# je mets à jour dans un dictionnaire
		# donc la clé est le mot-trie
		# la valeur la liste des mots
		if sorted_w not in dwords:
			dwords[sorted_w] = []
		dwords[sorted_w].append(word)

	# renvoie les les liste ou il y a plus de 1 mot
	res  = []
	for v in dwords.values():
		if len(v) > 1:
			res.append(v)

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
		print(anagramme(words))
		print(anagramme(words) == res) 

test_anagramme()