def manacher(s):
    """Longest palindrome in a string by Manacher

    :param s: string
    :requires: s is not empty
    :returns: i,j such that s[i:j] is the longest palindrome in s
    :complexity: O(len(s))
    """
    assert set.isdisjoint({'$', '^', '#'}, s)  # Forbidden letters
    if s == "":
        return (0, 1)
    t = "^#" + "#".join(s) + "#$"
    c = 1
    d = 1
    p = [0] * len(t)
    for i in range(2, len(t) - 1):
        #                        -- reflect index i with respect to c
        mirror = 2 * c - i         # = c - (i-c)
        p[i] = max(0, min(d - i, p[mirror]))
        #                        -- grow palindrome centered in i
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        #                        -- adjust center if necessary
        if i + p[i] > d:
            c = i
            d = i + p[i]
    (k, i) = max((p[i], i) for i in range(1, len(t) - 1))
    return ((i - k) // 2, (i + k) // 2)  # extract solution

def pluslong_palindrome(letters, debug=True):
	"""  letters contient une série de lettre
	"""
	print(letters)
	center_pos = 1
	lg = 0
	lens = len(letters)
	for i, car in enumerate(letters[1:-1], 1):

		lg_max = 0
		left = i - 1
		right = i + 1
		while left-lg_max >= 0 and right+lg_max < lens and letters[left-lg_max] == letters[right+lg_max]:
			if debug:
				print(f'{car = } / {lg_max = }, -> {letters[left-lg_max] = } - {letters[right+lg_max] = }')
			lg_max += 1
		else:
			if debug:
				print(f'Break on {car = } / {lg_max = }')
		if debug:
			print('-------')
		if lg_max > lg:
			if debug:
				print(f'update on {lg_max = } and {i = }')
			center_pos = i
			lg = lg_max
	# renvoie les 
	if debug:
		print(f'center in {center_pos} -> {letters[center_pos-lg:center_pos+lg+1]= }')
	return center_pos-lg, center_pos+lg


def test_pluslong_palindrome():
	"""
	"""
	tests = ( # words
			(('otot'), (1, 2)),
			(("ezearadararadau") , (1, 2)),
			)
	for letters, res in tests:
		print(pluslong_palindrome(letters) == manacher(letters))

test_pluslong_palindrome()