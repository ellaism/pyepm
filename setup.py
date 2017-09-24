#!/usr/bin/env python

from setuptools import setup, find_packages

CONSOLE_SCRIPTS = ['pyepm=pyepm.pyepm:main']
LONG = """
Python-based EPM (Ethereum Package Manager) for Serpent 2 contract deployment using YAML for package definitions.
"""

setup(name="pyepm",
      packages=find_packages("."),
      description='Python Ethereum Package Manager',
      long_description=LONG,
      author="caktux",
      author_email="caktux@gmail.com",
      url='https://github.com/etherex/pyepm/',
      install_requires=[
          'pyyaml',
          'ethereum',
          'ethereum-serpent',
          'requests'
      ],
      entry_points=dict(console_scripts=CONSOLE_SCRIPTS),
      version="0.0.1",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "License :: OSI Approved :: MIT License",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7",
      ])
