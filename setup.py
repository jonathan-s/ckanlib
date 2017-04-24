#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import unittest

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = [
    'requests'
]

test_requirements = []


def test_suite():
    test_loader1 = unittest.TestLoader()
    test_loader2 = unittest.TestLoader()
    integrationtests = test_loader2.discover('integrationtests', pattern='test_*.py')
    test_suite = test_loader1.discover('tests', pattern='test_*.py')
    test_suite.addTests(integrationtests)
    return test_suite


setup(
    name='ckanlib',
    version='0.1.0',
    description="A pof wrapper for ckan",
    long_description=readme,
    author="Jonathan Sundqvist",
    author_email='sundqvist.jonathan@gmail.com',
    url='https://github.com/jonathan-s/ckanlib',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ckanlib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='setup.test_suite',
    tests_require=test_requirements
)
