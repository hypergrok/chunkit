import os
from setuptools import (
   setup,
   find_packages,
)

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(
   name='chunkit',
   version='0.1.9',
   description='Convert URLs and files into LLM-friendly markdown chunks',
   long_description=long_desc,
   long_description_content_type='text/markdown',
   author='hypergrok',
   author_email='173556723+hypergrok@users.noreply.github.com',
   url='https://github.com/hypergrok/chunkit',
   project_urls={
      'Source Code': 'https://github.com/hypergrok/chunkit'
   },
   packages=find_packages(),
   include_package_data=True,
   install_requires=[
      'requests'
   ]
)
