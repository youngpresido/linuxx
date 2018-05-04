#!/usr/bin/env python
import os
from setuptools import setup, find_packages
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
setup(name='myscrumy',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      license='BSD License',  # example license
      description='A linuxjobber project',
      author='Bamidele Emmanuel Segun',
      author_email='youngpresido94@gmail.com',
      classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],      
      scripts=['manage.py'])