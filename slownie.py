# encoding=UTF-8

SLOWNIE_1X = u'''
#        jeden      dwa       trzy       cztery      pięć       sześć      siedem       osiem       dziewięć
dziesięć jedenaście dwanaście trzynaście czternaście piętnaście szesnaście siedemnaście osiemnaście dziewiętnaście
'''.split()

SLOWNIE_10X = u'''
# # dwadzieścia trzydzieści czterdzieści
'''.split() + [u'%sdziesiąt' % SLOWNIE_1X[i] for i in xrange(5, 10)]

SLOWNIE_100X = u'''
# sto dwieście trzysta czterysta
'''.split() + ['%sset' % SLOWNIE_1X[i] for i in xrange(5, 10)]

SLOWNIE_1X[0] = SLOWNIE_10X[0] = SLOWNIE_10X[1] = SLOWNIE_100X[0] = None

PREFIXES = 'mi bi try kwadry kwinty seksty septy okty noni decy'.split()

SLOWNIE_1000XX = [None, u'tysiąc'] + [PREFIXES[i >> 1] + (i & 1 and 'liard' or 'lion') for i in xrange(2 * len(PREFIXES))]

SLOWNIE_0 = 'zero'

del i

def inflect(i, base):
	if base is None:
		return None
	if i == 1:
		suffix = ''
		return base
	i = i % 100
	if i in (2, 3, 4) or (i > 20 and i % 10 in (2, 3, 4)):
		if base[-1] == 'c':
			suffix = 'e'
		else:
			suffix = 'y'
	else:
		if base[-2:] == u'ąc':
			base = base[:-2]
			suffix = u'ęcy'
		else:
			suffix = u'ów'
	return base + suffix

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
