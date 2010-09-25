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
import sys

import distutils.core
import distutils.command.build_py

if sys.version_info >= (3,):
    build_py = distutils.command.build_py.build_py_2to3
else:
    build_py = distutils.command.build_py.build_py

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

def get_version():
    d = {}
    file = open('slownie.py')
    try:
        for line in file:
            if line.startswith(('__date__ = ', '__version__ =')):
                exec(line, d)
    finally:
        file.close()
    try:
        return d['__version__']
    except LookupError:
        raise IOError('Unexpected end-of-file')

distutils.core.setup(
    name = 'python-slownie',
    version = get_version(),
    license = 'MIT',
    description = 'Polish spelled-out numbers',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://jwilk.net/software/python-slownie',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    py_modules = ['slownie'],
    cmdclass = dict(build_py=build_py),
)

# vim:ts=4 sw=4 et
