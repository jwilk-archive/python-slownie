# encoding=UTF-8

# Copyright © 2008-2019 Jakub Wilk <jwilk@jwilk.net>
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

'''
Polish spelled-out numbers
'''

type(b'')  # Python >= 2.6 is required
type(u'') # Python 2.X or >= 3.3 is required

__author__ = 'Jakub Wilk <jwilk@jwilk.net>'
__version__ = '1.1'

SLOWNIE_1X = u'''
#        jeden      dwa       trzy       cztery      pięć       sześć      siedem       osiem       dziewięć
dziesięć jedenaście dwanaście trzynaście czternaście piętnaście szesnaście siedemnaście osiemnaście dziewiętnaście
'''.split()

SLOWNIE_10X = u'''
# # dwadzieścia trzydzieści czterdzieści
'''.split() + list(u'{n}dziesiąt'.format(n=SLOWNIE_1X[i]) for i in range(5, 10))

SLOWNIE_100X = u'''
# sto dwieście trzysta czterysta
'''.split() + list(u'{n}set'.format(n=SLOWNIE_1X[i]) for i in range(5, 10))

SLOWNIE_1X[0] = SLOWNIE_10X[0] = SLOWNIE_10X[1] = SLOWNIE_100X[0] = None

PREFIXES = u'mi bi try kwadry kwinty seksty septy okty noni decy'.split()

SLOWNIE_1000XX = (
    [None, (u'tysiąc', u'tysiące', u'tysięcy')] +
    list(
        (base, base + u'y', base + u'ów')
        for i in range(2 * len(PREFIXES))
        for base in [PREFIXES[i >> 1] + (i & 1 and u'liard' or u'lion')]
    )
)

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
    words += [SLOWNIE_100X[i // 100]]
    i = i % 100
    if i < 20:
        words += [SLOWNIE_1X[i]]
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
    words += [inflect(i, unit)]
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
                raise ValueError('i >= 10 ** {n}'.format(n=3 * len(SLOWNIE_1000XX)))
        m += 1
    return u' '.join(word for word in words if word)

__all__ = ['slownie', 'UNIT_ZLOTY', 'UNIT_GROSZ']

# vim:ts=4 sts=4 sw=4 et
