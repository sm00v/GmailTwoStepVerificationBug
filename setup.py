#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='GmailTwoStepVerificationBug',
    version='1.0',
    description="This package checks if two step verification exists on a Gmail id without sending the user an SMS or any kind of notification.. :D",
    long_description=readme + '\n\n' + history,
    author="Shantanu Khandelwal",
    author_email='shantanu561993@gmail.com',
    url='https://github.com/shantanu561993/GmailTwoStepVerificationBug',
    packages=[
        'GmailTwoStepVerificationBug',
    ],
    package_dir={'GmailTwoStepVerificationBug':
                 'GmailTwoStepVerificationBug'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='GmailTwoStepVerificationBug',
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