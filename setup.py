#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = '1.0.0'

install_requires = [
      'zeep'
]

setup(name='pyriksbankapi',
      version=version,
      description="python api to the riksbanken.se currency and exchangerates api",
      long_description=README,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      ],
      keywords='currency rates wsdl soap',
      author='Leif Johansson',
      author_email='leifj@sunet.se',
      url='http://www.sunet.se',
      license='BSD',
      setup_requires=['nose>=1.0'],
      tests_require=['nose>=1.0', 'mock'],
      test_suite="nose.collector",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
          'console_scripts': ['currencyrates=riksbankapi:currencyrates']
      },
      message_extractors={'src': [
          ('**.py', 'python', None),
          ('**/templates/**.html', 'mako', None),
      ]},
)
