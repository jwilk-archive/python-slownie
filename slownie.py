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
__version__ = '0.%s+py3k' % __date__.replace('-', '')

__doc__ = r'''
Polish text representation of numbers.

>>> slownie(0)
'zero'
>>> slownie(1)
'jeden'
>>> slownie(2)
'dwa'
>>> slownie(4)
'cztery'
>>> slownie(8)
'osiem'
>>> slownie(16)
'szesnaście'
>>> slownie(17)
'siedemnaście'
>>> slownie(23)
'dwadzieścia trzy'
>>> slownie(32)
'trzydzieści dwa'
>>> slownie(37)
'trzydzieści siedem'
>>> slownie(42)
'czterdzieści dwa'
>>> slownie(64)
'sześćdziesiąt cztery'
>>> slownie(69)
'sześćdziesiąt dziewięć'
>>> slownie(105)
'sto pięć'
>>> slownie(128)
'sto dwadzieścia osiem'
>>> slownie(256)
'dwieście pięćdziesiąt sześć'
>>> slownie(512)
'pięćset dwanaście'
>>> slownie(666)
'sześćset sześćdziesiąt sześć'
>>> slownie(1024)
'tysiąc dwadzieścia cztery'
>>> slownie(1024, jeden=True)
'jeden tysiąc dwadzieścia cztery'
>>> slownie(1 << 11)
'dwa tysiące czterdzieści osiem'
>>> slownie(1 << 12)
'cztery tysiące dziewięćdziesiąt sześć'
>>> slownie(1 << 13)
'osiem tysięcy sto dziewięćdziesiąt dwa'
>>> slownie(1 << 14)
'szesnaście tysięcy trzysta osiemdziesiąt cztery'
>>> slownie(1 << 15)
'trzydzieści dwa tysiące siedemset sześćdziesiąt osiem'
>>> slownie(1 << 16)
'sześćdziesiąt pięć tysięcy pięćset trzydzieści sześć'
>>> slownie(1 << 17)
'sto trzydzieści jeden tysięcy siedemdziesiąt dwa'
>>> slownie(1 << 18)
'dwieście sześćdziesiąt dwa tysiące sto czterdzieści cztery'
>>> slownie(1 << 19)
'pięćset dwadzieścia cztery tysiące dwieście osiemdziesiąt osiem'
>>> slownie(1 << 20)
'milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'
>>> slownie(1 << 20, jeden=True)
'jeden milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'
>>> slownie(10 ** 9)
'miliard'
>>> slownie(17 ** 17)
'osiemset dwadzieścia siedem trylionów dwieście czterdzieści biliardów dwieście sześćdziesiąt jeden bilionów osiemset osiemdziesiąt sześć miliardów trzysta trzydzieści sześć milionów siedemset sześćdziesiąt cztery tysiące sto siedemdziesiąt siedem'
>>> slownie(10 ** 66 - 1)
'dziewięćset dziewięćdziesiąt dziewięć decyliardów dziewięćset dziewięćdziesiąt dziewięć decylionów dziewięćset dziewięćdziesiąt dziewięć noniliardów dziewięćset dziewięćdziesiąt dziewięć nonilionów dziewięćset dziewięćdziesiąt dziewięć oktyliardów dziewięćset dziewięćdziesiąt dziewięć oktylionów dziewięćset dziewięćdziesiąt dziewięć septyliardów dziewięćset dziewięćdziesiąt dziewięć septylionów dziewięćset dziewięćdziesiąt dziewięć sekstyliardów dziewięćset dziewięćdziesiąt dziewięć sekstylionów dziewięćset dziewięćdziesiąt dziewięć kwintyliardów dziewięćset dziewięćdziesiąt dziewięć kwintylionów dziewięćset dziewięćdziesiąt dziewięć kwadryliardów dziewięćset dziewięćdziesiąt dziewięć kwadrylionów dziewięćset dziewięćdziesiąt dziewięć tryliardów dziewięćset dziewięćdziesiąt dziewięć trylionów dziewięćset dziewięćdziesiąt dziewięć biliardów dziewięćset dziewięćdziesiąt dziewięć bilionów dziewięćset dziewięćdziesiąt dziewięć miliardów dziewięćset dziewięćdziesiąt dziewięć milionów dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć'

>>> slownie(10 ** 66)
Traceback (most recent call last):
...
ValueError: i >= 10 ** 66
>>> slownie(-1)
Traceback (most recent call last):
...
ValueError: i < 0
'''

SLOWNIE_1X = '''
#        jeden      dwa       trzy       cztery      pięć       sześć      siedem       osiem       dziewięć
dziesięć jedenaście dwanaście trzynaście czternaście piętnaście szesnaście siedemnaście osiemnaście dziewiętnaście
'''.split()

SLOWNIE_10X = '''
# # dwadzieścia trzydzieści czterdzieści
'''.split() + ['%sdziesiąt' % SLOWNIE_1X[i] for i in range(5, 10)]

SLOWNIE_100X = '''
# sto dwieście trzysta czterysta
'''.split() + ['%sset' % SLOWNIE_1X[i] for i in range(5, 10)]

SLOWNIE_1X[0] = SLOWNIE_10X[0] = SLOWNIE_10X[1] = SLOWNIE_100X[0] = None

PREFIXES = 'mi bi try kwadry kwinty seksty septy okty noni decy'.split()

SLOWNIE_1000XX = \
    [None, ('tysiąc', 'tysiące', 'tysięcy')] + \
    [(base, base + 'y', base + 'ów') for i in range(2 * len(PREFIXES)) for base in [PREFIXES[i >> 1] + (i & 1 and 'liard' or 'lion')]]

SLOWNIE_0 = 'zero'

UNIT_ZLOTY = tuple('złot' + suffix for suffix in ('y', 'e', 'ych'))
UNIT_GROSZ = tuple('grosz' + suffix for suffix in ('', 'e', 'y'))

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
    return ' '.join(word for word in words if word)

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
    return ' '.join(word for word in words if word)

__all__ = 'slownie', 'UNIT_ZLOTY', 'UNIT_GROSZ'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# vim:ts=4 sw=4 et
