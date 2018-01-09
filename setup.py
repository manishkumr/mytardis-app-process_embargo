import os
from setuptools import setup, find_packages

version = '0.0.1'

setup(name='anstoProcessEmbargo',
      version=version,
      description="MyTardis app to process embargo",
      long_description="""\
Mytardis app to make experiments public after embargo expiry period of 1095 days(3 Years)\
""",
      classifiers=[],
      keywords='ansto embargo process',
      author='Manish Kumar',
      author_email='manish.kumar@monash.edu',
      url='',
      license='',
      packages=find_packages(),
      )