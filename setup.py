'''
*python-slownie* provides routines to spell out numbers in Polish.
'''

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
'''.strip().split('\n')

import os
import distutils.core

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

from slownie import __version__

distutils.core.setup(
    name = 'python-slownie',
    version = __version__,
    license = 'MIT',
    description = 'Polish spelled-out numbers',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://jwilk.net/software/python-slownie',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    py_modules = ['slownie']
)

# vim:ts=4 sw=4 et
