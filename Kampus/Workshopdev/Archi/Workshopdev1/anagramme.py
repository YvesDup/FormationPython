def anagramme(words):
	"""  words contient une liste de mot
	"""
	# il faut le même nombre de lettre
	# le tri des lettres du mot et on va comparer avec le tri des lettres d'un autre mot
	# creer un dictionnaire:
	# key: le mot trié par lettre sous la forme: tuple(sorted(word))
	# value: une ensemble de mots sous la forme {word1, word2, ...} - l'ensemble ca evite les doublons
	dwords = {}
	for word in words:
		key = tuple(sorted(word))

		# key is in dwords ?
		if key not in dwords:
			# key does not exist so
			dwords[key] = {word}
		else:
			dwords[key].add(word)

	# renvoie les values du dictionnaire si la longueur est supérieure à 1
	"""
	res = []
	for v in dwords.values():
		if len(v) > 1:
			res.append(sorted(v))

	return res
	"""
	return [sorted(v) for v in dwords.values() if len(v) > 1 ]


def test_anagramme():
	"""
	"""
	tests = ( # words														res
			(("ecrue", "uni", "nue") , 									[]),
			(("les", "sel", "sell"), 									[["les", "sel"]]),
			(("les", "sel", "sel"), 									[["les", "sel"]]),
			(("line", "steres", "tresse", "tres", "lien", "restes"), 	[["lien", "line"], ["restes", "steres", "tresse"]])
	)
	for words, res in tests:
		print(anagramme(words), '->', anagramme(words) == res)

test_anagramme()