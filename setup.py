from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='bodine',
      version=version,
      description="Tool for writers.",
      long_description="""\
This is a tool for writers to write better writings.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='writing tool widget',
      author='greato',
      author_email='ricky@han.org',
      url='https://github.com/greato',
      license='GNU',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
