exampleproject
==============
.. image:: https://travis-ci.org/lukassnoek/exampleproject.svg?branch=master
  :target: https://travis-ci.org/lukassnoek/exampleproject

.. image:: https://coveralls.io/repos/github/lukassnoek/exampleproject/badge.svg?branch=master
  :target: https://coveralls.io/github/lukassnoek/exampleproject?branch=master

Example project for testing / documentation tutorial. This repo contains some standard files to perform
testing (with py.test and continuous integration with Travis CI) and files/scripts for automating documentation.

Branches
--------
The master branch represents a fully set-up package with testing (and continuous integration),
automatic documentation generation, and coverage reporting; the `tryout` branch can be used
to "practice" setting up Sphinx, tests, etc.

Dependencies
------------
To integrate all tools/functionality, make sure you have the following installed:

- Python 2.7 or 3.5
- sphinx (`pip install sphinx`)
- sphinx ReadTheDocs theme (`pip install sphinx_rtd_theme`)
- pytest (`pip install pytest`)
- pytest-cov (`pip install pytest-cov`)
- pytest-pep8 (`pip install pytest-pep8`)
- coveralls (`pip install coveralls`)






