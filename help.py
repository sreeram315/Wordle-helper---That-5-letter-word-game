'''
This code is propritory.
Property of the fat body prince.
'''

must_include = 'AEPL'
must_not_include = 'CRHOUSNJOKYTUIDR'
letter_not_at = {
	'A': [1,4],
	'L': [3],
	'P': [5],
	'E': [4]
}
letter_be_at = {
	'E': [5]
}

words = [x.strip().upper() for x in open('words.txt', 'r').readlines()]
must_include = list(set([l for l in must_include]))
must_not_include = list(set([l for l in must_not_include]))

for word in words:
	c1 = any([True if letter not in word else False for letter in must_include])
	c2 = any([True if letter in word else False for letter in must_not_include])
	c3 = any([True if any([word[p-1]==k for p in pos]) else False for k,pos in letter_not_at.items()])
	c4 = any([True if any([word[p-1]!=k for p in pos]) else False for k,pos in letter_be_at.items()])
	if not any([c1, c2, c3, c4]):
		print(word)
