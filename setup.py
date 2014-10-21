#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

module_path = os.path.join(os.path.dirname(__file__), 'flask_storage', '__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]
__version__ = eval(version_line.split('__version__ = ')[-1])

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'wheel==0.23.0',
    'Flask>=0.10.1',
    'six>=1.7.3',
    'apache-libcloud==0.15.1',
    'siilo==0.1.0',
]

test_requirements = [
    'coverage',
    'pep8',
    'pylint',
    'flake8',
    'pyflakes',
    'mccabe',
    'pytest',
    'pytest-cov',
    'tox',
    'coveralls',
    'mock',
]

setup(
    name='flask_storage',
    version=__version__,
    description='A simple storage for Flask.',
    long_description=readme + '\n\n' + history,
    author='Jindřich Smitka',
    author_email='smitka.j@gmail.com',
    url='https://github.com/s-m-i-t-a/flask_storage',
    packages=[
        'flask_storage',
    ],
    package_dir={'flask_storage':
                 'flask_storage'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='flask_storage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
