from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
   name='chunkit',
   version='0.1.0',
   description='Convert URLs and files into LLM-friendly text chunks',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='genaitools',
   author_email='173556723+genaitools@users.noreply.github.com',
   url='https://github.com/genaitools/chunkit',
   project_urls={
      'Source Code': 'https://github.com/genaitools/chunkit'
   },
   packages=find_packages(),
   include_package_data=True,
   install_requires=[]
)
