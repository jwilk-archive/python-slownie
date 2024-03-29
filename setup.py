# encoding=UTF-8

# Copyright © 2010-2022 Jakub Wilk <jwilk@jwilk.net>
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
*python-slownie* lets you spell out numbers in Polish.
'''

import io
import os

# pylint: disable=deprecated-module
import distutils.core
import distutils.command.build_py
from distutils.command.sdist import sdist as distutils_sdist
# pylint: enable=deprecated-module

try:
    import distutils644
except ImportError:
    pass
else:
    distutils644.install()

type(b'')  # Python >= 2.6 is required
type(u'')  # Python 2.X or >= 3.3 is required

class cmd_sdist(distutils_sdist):

    def maybe_move_file(self, base_dir, src, dst):
        src = os.path.join(base_dir, src)
        dst = os.path.join(base_dir, dst)
        if os.path.exists(src):
            self.move_file(src, dst)

    def make_release_tree(self, base_dir, files):
        distutils_sdist.make_release_tree(self, base_dir, files)
        self.maybe_move_file(base_dir, 'LICENSE', 'doc/LICENSE')

def get_version():
    with io.open('doc/changelog', encoding='UTF-8') as fp:
        line = fp.readline()
    return line.split()[1].strip('()')

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

distutils.core.setup(
    name='python-slownie',
    version=get_version(),
    license='MIT',
    description='Polish spelled-out numbers',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='https://jwilk.net/software/python-slownie',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['slownie'],
    cmdclass=dict(
        sdist=cmd_sdist,
    ),
)

# vim:ts=4 sts=4 sw=4 et
