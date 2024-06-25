from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
   name='chunkit',
   version='0.1.1',
   description='Convert URLs into LLM-friendly text chunks',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='hypergrok',
   author_email='173556723+hypergrok@users.noreply.github.com',
   url='https://github.com/hypergrok/chunkit',
   project_urls={
      'Source Code': 'https://github.com/hypergrok/chunkit'
   },
   packages=find_packages(),
   include_package_data=True,
   install_requires=[]
)
