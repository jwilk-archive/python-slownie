# encoding=UTF-8

# Copyright © 2010-2015 Jakub Wilk <jwilk@jwilk.net>
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
*python-slownie* provides routines to spell out numbers in Polish.
'''

from __future__ import with_statement

classifiers = '''
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: Polish
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Text Processing :: Linguistic
'''.strip().splitlines()

import sys

import distutils.core
import distutils.command.build_py

if sys.version_info >= (3,):
    build_py = distutils.command.build_py.build_py_2to3
else:
    build_py = distutils.command.build_py.build_py

def get_version():
    d = {}
    enc = {}
    if sys.version_info >= (3,):
        enc.update(encoding='UTF-8')
    with open('slownie.py', **enc) as file:
        for line in file:
            if line.startswith('__version__ ='):
                exec(line, d)
    return d['__version__']

distutils.core.setup(
    name='python-slownie',
    version=get_version(),
    license='MIT',
    description='Polish spelled-out numbers',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-slownie',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['slownie'],
    cmdclass=dict(build_py=build_py),
)

# vim:ts=4 sts=4 sw=4 et
