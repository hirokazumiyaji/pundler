# coding: utf-8
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


setup(
    name='pundler',
    version='0.0.1',
    description='Python Package Manager using pip',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='pip virtualenv',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['PyYAML'],
    author='Hirokazu Miyaji',
    author_email='hirokazu.miyaji@gmail.com',
    url='https://github.com/hirokazumiyaji/pundler',
    license='MIT',
    entry_points={
        'console_scripts': [
            'pundle=pundler:main',
        ],
    },
    zip_safe=False,
)
