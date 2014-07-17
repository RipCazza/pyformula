#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'sympy'
]

test_requirements = [
    # TODO: put package test requirements here
]

def get_version(filename):
    import re

    here = os.path.dirname(__file__)
    with open(os.path.join(here, filename)) as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='pyformula',
    version=get_version(os.path.join("pyformula", "__init__.py")),
    description='PyFormula is a small algebraic calculator app.',
    long_description=readme + '\n\n' + history,
    author='Stefan Bakker',
    author_email='s.bakker777@gmail.com',
    url='https://github.com/RipCazza/pyformula',
    packages=[
        'pyformula',
        'pyformula.formulae',
    ],
    package_dir={'pyformula':
                 'pyformula'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords='pyformula',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
