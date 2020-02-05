from setuptools import setup
import os 
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(name='print-function',
      version='1.0.2',
      description='Best python print function',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/raywu60kg/print-function',
      author='raywu60kg',
      author_email='wuhaohsiang1992@gmail.com',
      packages=['___future___'],
      license="MIT",
      python_requires=">=3.4",
      classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
      ])