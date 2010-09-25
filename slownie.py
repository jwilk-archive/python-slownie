# encoding=UTF-8
#
# Copyright © 2008, 2009, 2010 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = 'Jakub Wilk <jwilk@jwilk.net>'
__date__ = '2010-09-25'
__version__ = '0.%s' % __date__.replace('-', '')

__doc__ = ur'''
Polish text representation of numbers.

>>> slownie(0)
u'zero'
>>> slownie(1)
u'jeden'
>>> slownie(2)
u'dwa'
>>> slownie(4)
u'cztery'
>>> slownie(8)
u'osiem'
>>> slownie(16)
u'szesnaście'
>>> slownie(17)
u'siedemnaście'
>>> slownie(23)
u'dwadzieścia trzy'
>>> slownie(32)
u'trzydzieści dwa'
>>> slownie(37)
u'trzydzieści siedem'
>>> slownie(42)
u'czterdzieści dwa'
>>> slownie(64)
u'sześćdziesiąt cztery'
>>> slownie(69)
u'sześćdziesiąt dziewięć'
>>> slownie(105)
u'sto pięć'
>>> slownie(128)
u'sto dwadzieścia osiem'
>>> slownie(256)
u'dwieście pięćdziesiąt sześć'
>>> slownie(512)
u'pięćset dwanaście'
>>> slownie(666)
u'sześćset sześćdziesiąt sześć'
>>> slownie(1024)
u'tysiąc dwadzieścia cztery'
>>> slownie(1024, jeden=True)
u'jeden tysiąc dwadzieścia cztery'
>>> slownie(1 << 11)
u'dwa tysiące czterdzieści osiem'
>>> slownie(1 << 12)
u'cztery tysiące dziewięćdziesiąt sześć'
>>> slownie(1 << 13)
u'osiem tysięcy sto dziewięćdziesiąt dwa'
>>> slownie(1 << 14)
u'szesnaście tysięcy trzysta osiemdziesiąt cztery'
>>> slownie(1 << 15)
u'trzydzieści dwa tysiące siedemset sześćdziesiąt osiem'
>>> slownie(1 << 16)
u'sześćdziesiąt pięć tysięcy pięćset trzydzieści sześć'
>>> slownie(1 << 17)
u'sto trzydzieści jeden tysięcy siedemdziesiąt dwa'
>>> slownie(1 << 18)
u'dwieście sześćdziesiąt dwa tysiące sto czterdzieści cztery'
>>> slownie(1 << 19)
u'pięćset dwadzieścia cztery tysiące dwieście osiemdziesiąt osiem'
>>> slownie(1 << 20)
u'milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'
>>> slownie(1 << 20, jeden=True)
u'jeden milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'
>>> slownie(10 ** 9)
u'miliard'
>>> slownie(17 ** 17)
u'osiemset dwadzieścia siedem trylionów dwieście czterdzieści biliardów dwieście sześćdziesiąt jeden bilionów osiemset osiemdziesiąt sześć miliardów trzysta trzydzieści sześć milionów siedemset sześćdziesiąt cztery tysiące sto siedemdziesiąt siedem'
>>> slownie(10 ** 66 - 1)
u'dziewięćset dziewięćdziesiąt dziewięć decyliardów dziewięćset dziewięćdziesiąt dziewięć decylionów dziewięćset dziewięćdziesiąt dziewięć noniliardów dziewięćset dziewięćdziesiąt dziewięć nonilionów dziewięćset dziewięćdziesiąt dziewięć oktyliardów dziewięćset dziewięćdziesiąt dziewięć oktylionów dziewięćset dziewięćdziesiąt dziewięć septyliardów dziewięćset dziewięćdziesiąt dziewięć septylionów dziewięćset dziewięćdziesiąt dziewięć sekstyliardów dziewięćset dziewięćdziesiąt dziewięć sekstylionów dziewięćset dziewięćdziesiąt dziewięć kwintyliardów dziewięćset dziewięćdziesiąt dziewięć kwintylionów dziewięćset dziewięćdziesiąt dziewięć kwadryliardów dziewięćset dziewięćdziesiąt dziewięć kwadrylionów dziewięćset dziewięćdziesiąt dziewięć tryliardów dziewięćset dziewięćdziesiąt dziewięć trylionów dziewięćset dziewięćdziesiąt dziewięć biliardów dziewięćset dziewięćdziesiąt dziewięć bilionów dziewięćset dziewięćdziesiąt dziewięć miliardów dziewięćset dziewięćdziesiąt dziewięć milionów dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć'

>>> slownie(10 ** 66)
Traceback (most recent call last):
...
ValueError: i >= 10 ** 66
>>> slownie(-1)
Traceback (most recent call last):
...
ValueError: i < 0
'''
__doc__ = '\n'.join(line.encode('unicode-escape') for line in __doc__.splitlines())

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
'''.split() + [u'%sset' % SLOWNIE_1X[i] for i in xrange(5, 10)]
del i

SLOWNIE_1X[0] = SLOWNIE_10X[0] = SLOWNIE_10X[1] = SLOWNIE_100X[0] = None

PREFIXES = u'mi bi try kwadry kwinty seksty septy okty noni decy'.split()

SLOWNIE_1000XX = \
    [None, (u'tysiąc', u'tysiące', u'tysięcy')] + \
    [(base, base + u'y', base + u'ów') for i in xrange(2 * len(PREFIXES)) for base in [PREFIXES[i >> 1] + (i & 1 and u'liard' or u'lion')]]
del i, base

SLOWNIE_0 = u'zero'

UNIT_ZLOTY = tuple(u'złot' + suffix for suffix in (u'y', u'e', u'ych'))
UNIT_GROSZ = tuple(u'grosz' + suffix for suffix in (u'', u'e', u'y'))

def inflect(i, forms):
    if forms is None:
        return None
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
    return u' '.join(word for word in words if word)

def slownie(i, jeden=False, unit=None):

    i = int(i)
    if i < 0:
        raise ValueError('i < 0')
    if i == 0:
        words = [SLOWNIE_0]
    elif i == 1:
        words = [SLOWNIE_1X[1]]
    else:
        words = []
    words += inflect(i, unit),
    if i == 1:
        i = 0
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
    return u' '.join(word for word in words if word)

__all__ = 'slownie', 'UNIT_ZLOTY', 'UNIT_GROSZ'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# vim:ts=4 sw=4 et
