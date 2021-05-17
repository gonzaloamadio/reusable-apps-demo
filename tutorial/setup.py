#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = "0.1.0"

setup(
    name='tutorial',
    version=version,
    description="""Tutorial reusable app""",
    long_description="long description",
    author="Gonzalo Amadio",
    author_email='gonzalo@magoya.com',
    url='https://gitlab.com/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django', 'djangorestframework'],
    license="MIT",
    zip_safe=False,
    keywords='tutorial',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

