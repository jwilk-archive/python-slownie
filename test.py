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

import unittest

import slownie

data = {
    0: u'zero',
    1: u'jeden',
    2: u'dwa',
    4: u'cztery',
    8: u'osiem',
    16: u'szesnaście',
    17: u'siedemnaście',
    23: u'dwadzieścia trzy',
    32: u'trzydzieści dwa',
    37: u'trzydzieści siedem',
    42: u'czterdzieści dwa',
    64: u'sześćdziesiąt cztery',
    69: u'sześćdziesiąt dziewięć',
    105: u'sto pięć',
    128: u'sto dwadzieścia osiem',
    256: u'dwieście pięćdziesiąt sześć',
    512: u'pięćset dwanaście',
    666: u'sześćset sześćdziesiąt sześć',
    1024: (u'tysiąc dwadzieścia cztery', u'jeden tysiąc dwadzieścia cztery'),
    1 << 11: u'dwa tysiące czterdzieści osiem',
    1 << 12: u'cztery tysiące dziewięćdziesiąt sześć',
    1 << 13: u'osiem tysięcy sto dziewięćdziesiąt dwa',
    1 << 14: u'szesnaście tysięcy trzysta osiemdziesiąt cztery',
    1 << 15: u'trzydzieści dwa tysiące siedemset sześćdziesiąt osiem',
    1 << 16: u'sześćdziesiąt pięć tysięcy pięćset trzydzieści sześć',
    1 << 17: u'sto trzydzieści jeden tysięcy siedemdziesiąt dwa',
    1 << 18: u'dwieście sześćdziesiąt dwa tysiące sto czterdzieści cztery',
    1 << 19: u'pięćset dwadzieścia cztery tysiące dwieście osiemdziesiąt osiem',
    1 << 20: (u'milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć', u'jeden milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'),
    10 ** 9: (u'miliard', u'jeden miliard'),
    17 ** 17: u'osiemset dwadzieścia siedem trylionów dwieście czterdzieści biliardów dwieście sześćdziesiąt jeden bilionów osiemset osiemdziesiąt sześć miliardów trzysta trzydzieści sześć milionów siedemset sześćdziesiąt cztery tysiące sto siedemdziesiąt siedem',
    10 ** 66 - 1: u'dziewięćset dziewięćdziesiąt dziewięć decyliardów dziewięćset dziewięćdziesiąt dziewięć decylionów dziewięćset dziewięćdziesiąt dziewięć noniliardów dziewięćset dziewięćdziesiąt dziewięć nonilionów dziewięćset dziewięćdziesiąt dziewięć oktyliardów dziewięćset dziewięćdziesiąt dziewięć oktylionów dziewięćset dziewięćdziesiąt dziewięć septyliardów dziewięćset dziewięćdziesiąt dziewięć septylionów dziewięćset dziewięćdziesiąt dziewięć sekstyliardów dziewięćset dziewięćdziesiąt dziewięć sekstylionów dziewięćset dziewięćdziesiąt dziewięć kwintyliardów dziewięćset dziewięćdziesiąt dziewięć kwintylionów dziewięćset dziewięćdziesiąt dziewięć kwadryliardów dziewięćset dziewięćdziesiąt dziewięć kwadrylionów dziewięćset dziewięćdziesiąt dziewięć tryliardów dziewięćset dziewięćdziesiąt dziewięć trylionów dziewięćset dziewięćdziesiąt dziewięć biliardów dziewięćset dziewięćdziesiąt dziewięć bilionów dziewięćset dziewięćdziesiąt dziewięć miliardów dziewięćset dziewięćdziesiąt dziewięć milionów dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć',
}


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_normal(self):
        for key, expected in data.iteritems():
            if isinstance(expected, tuple):
                expected0, expected1 = expected
            else:
                expected0 = expected1 = expected
            slownie.slownie(key) == expected0
            slownie.slownie(key, jeden=True) == expected1

    def test_limits(self):
        def f_max():
            slownie.slownie(10 ** 66)
        def f_min():
            slownie.slownie(-1)
        self.assertRaises(ValueError, f_max)
        self.assertRaises(ValueError, f_min)

if __name__ == '__main__':
    unittest.main()

# vim:ts=4 sw=4 et
