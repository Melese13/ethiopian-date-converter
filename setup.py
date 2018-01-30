#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import setuptools

setuptools.setup(
    name='ethiopian-date-converter',
    version=__import__('ethiopian_date_converter').__version__,
    license='GNU General Public License (GPL), Version 3',

    provides=['ethiopian_date_converter'],

    description='Ethiopian date converter.',
    long_description=open('README.rst').read(),

    url='https://github.com/dimagi/ethiopian-date-converter',

    packages=['ethiopian_date_converter'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or '
        'Lesser General Public License (LGPL)',
        'Programming Language :: Python',
    ],
)
