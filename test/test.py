# encoding=UTF-8
#
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
python-slownie test suite
'''

import io
import os
import unittest

import slownie

# pylint: disable=line-too-long
data = {
    0: 'zero',
    1: 'jeden',
    2: 'dwa',
    4: 'cztery',
    8: 'osiem',
    16: 'szesnaście',
    17: 'siedemnaście',
    23: 'dwadzieścia trzy',
    32: 'trzydzieści dwa',
    37: 'trzydzieści siedem',
    42: 'czterdzieści dwa',
    64: 'sześćdziesiąt cztery',
    69: 'sześćdziesiąt dziewięć',
    105: 'sto pięć',
    128: 'sto dwadzieścia osiem',
    256: 'dwieście pięćdziesiąt sześć',
    512: 'pięćset dwanaście',
    666: 'sześćset sześćdziesiąt sześć',
    1024: ('tysiąc dwadzieścia cztery', 'jeden tysiąc dwadzieścia cztery'),
    1 << 11: 'dwa tysiące czterdzieści osiem',
    1 << 12: 'cztery tysiące dziewięćdziesiąt sześć',
    1 << 13: 'osiem tysięcy sto dziewięćdziesiąt dwa',
    1 << 14: 'szesnaście tysięcy trzysta osiemdziesiąt cztery',
    1 << 15: 'trzydzieści dwa tysiące siedemset sześćdziesiąt osiem',
    1 << 16: 'sześćdziesiąt pięć tysięcy pięćset trzydzieści sześć',
    1 << 17: 'sto trzydzieści jeden tysięcy siedemdziesiąt dwa',
    1 << 18: 'dwieście sześćdziesiąt dwa tysiące sto czterdzieści cztery',
    1 << 19: 'pięćset dwadzieścia cztery tysiące dwieście osiemdziesiąt osiem',
    1 << 20: ('milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć', 'jeden milion czterdzieści osiem tysięcy pięćset siedemdziesiąt sześć'),
    10 ** 9: ('miliard', 'jeden miliard'),
    17 ** 17: 'osiemset dwadzieścia siedem trylionów dwieście czterdzieści biliardów dwieście sześćdziesiąt jeden bilionów osiemset osiemdziesiąt sześć miliardów trzysta trzydzieści sześć milionów siedemset sześćdziesiąt cztery tysiące sto siedemdziesiąt siedem',
    10 ** 66 - 1: 'dziewięćset dziewięćdziesiąt dziewięć decyliardów dziewięćset dziewięćdziesiąt dziewięć decylionów dziewięćset dziewięćdziesiąt dziewięć noniliardów dziewięćset dziewięćdziesiąt dziewięć nonilionów dziewięćset dziewięćdziesiąt dziewięć oktyliardów dziewięćset dziewięćdziesiąt dziewięć oktylionów dziewięćset dziewięćdziesiąt dziewięć septyliardów dziewięćset dziewięćdziesiąt dziewięć septylionów dziewięćset dziewięćdziesiąt dziewięć sekstyliardów dziewięćset dziewięćdziesiąt dziewięć sekstylionów dziewięćset dziewięćdziesiąt dziewięć kwintyliardów dziewięćset dziewięćdziesiąt dziewięć kwintylionów dziewięćset dziewięćdziesiąt dziewięć kwadryliardów dziewięćset dziewięćdziesiąt dziewięć kwadrylionów dziewięćset dziewięćdziesiąt dziewięć tryliardów dziewięćset dziewięćdziesiąt dziewięć trylionów dziewięćset dziewięćdziesiąt dziewięć biliardów dziewięćset dziewięćdziesiąt dziewięć bilionów dziewięćset dziewięćdziesiąt dziewięć miliardów dziewięćset dziewięćdziesiąt dziewięć milionów dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć',
}
# pylint: enable=line-too-long

here = os.path.dirname(__file__)

class Test(unittest.TestCase):

    def test_normal(self):
        for key, expected in data.items():
            if isinstance(expected, tuple):
                expected0, expected1 = expected
            else:
                expected0 = expected1 = expected
            if str is bytes:
                expected0 = expected0.decode('UTF-8')
                expected1 = expected1.decode('UTF-8')
            self.assertEqual(slownie.slownie(key), expected0)
            self.assertEqual(slownie.slownie(key, jeden=True), expected1)

    def test_limits(self):
        def f_max():
            slownie.slownie(10 ** 66)
        def f_min():
            slownie.slownie(-1)
        self.assertRaises(ValueError, f_max)
        self.assertRaises(ValueError, f_min)

    def test_version(self):
        path = os.path.join(here, os.pardir, 'doc', 'changelog')
        with io.open(path, 'rt', encoding='UTF-8') as fp:
            line = fp.readline()
        changelog_version = line.split()[1].strip('()')
        self.assertEqual(changelog_version, slownie.__version__)

if __name__ == '__main__':
    unittest.main()

# vim:ts=4 sts=4 sw=4 et
