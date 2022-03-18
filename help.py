'''
This code is propritory.
Property of the fat body prince.
'''

must_include = 'RAE'
must_not_include = 'HOUSCNTULIPHITCHFILTHPLSMGUMP'
letter_not_at = {
	'R': [2,4],
	'A': [3,4],
	'E': [2,3,5]
}
letter_be_at = {
	'R': [5]
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
