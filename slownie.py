# encoding=UTF-8

SLOWNIE_1X = u'''
#        jeden      dwa       trzy       cztery      pięć       sześć      siedem       osiem       dziewięć
dziesięć jedenaście dwanaście trzynaście czternaście piętnaście szesnaście siedemnaście osiemnaście dziewiętnaście
'''.split()

SLOWNIE_10X = u'''
# # dwadzieścia trzydzieści czterdzieści
'''.split() + [u'%sdziesiąt' % SLOWNIE_1X[i] for i in xrange(5, 10)]
del i

SLOWNIE_100X = u'''
# sto dwieście trzysta czterysta
'''.split() + ['%sset' % SLOWNIE_1X[i] for i in xrange(5, 10)]
del i

SLOWNIE_1X[0] = SLOWNIE_10X[0] = SLOWNIE_10X[1] = SLOWNIE_100X[0] = None

PREFIXES = 'mi bi try kwadry kwinty seksty septy okty noni decy'.split()

SLOWNIE_1000XX = \
	[None, (u'tysiąc', u'tysiące', u'tysięcy')] + \
	[(base, base + 'y', base + u'ów') for i in xrange(2 * len(PREFIXES)) for base in [PREFIXES[i >> 1] + (i & 1 and 'liard' or 'lion')]]
del i, base

SLOWNIE_0 = 'zero'

def inflect(i, forms):
	if forms is None:
		return None
	print forms
	form_1, form_2, form_5 = forms
	if i == 1:
		return form_1
	i = i % 100
	if i in (2, 3, 4) or (i > 20 and i % 10 in (2, 3, 4)):
		return form_2
	else:
		return form_5

def slownie999(i):
	i = int(i)
	if i < 1:
		raise ValueError
	if i > 999:
		raise ValueError
	words = []
	words += SLOWNIE_100X[i // 100],
	i = i % 100
	if i < 20:
		words += SLOWNIE_1X[i],
	else:
		words += (SLOWNIE_10X[i // 10], SLOWNIE_1X[i % 10])
	return ' '.join(word for word in words if word)

def slownie(i, jeden=False):

	i = int(i)
	if i < 0:
		raise ValueError('i < 0')
	if i == 0:
		return SLOWNIE_0
	if i == 1:
		return SLOWNIE_1X[1]
	words = []
	m = 0
	while i > 0:
		i, j = divmod(i, 1000)
		if j > 0:
			if j != 1 or jeden or m == 0:
				t = slownie999(j)
			else:
				t = None
			try:
				words = [t, inflect(j, SLOWNIE_1000XX[m])] + words
			except IndexError:
				raise ValueError('i >= 10 ** %d' % (3 * len(SLOWNIE_1000XX)))
		m += 1
	return ' '.join(word for word in words if word)

__all__ = 'slownie',

# vim:ts=4 sw=4 noet
