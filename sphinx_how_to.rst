Instructions on how to set-up Sphinx
====================================

Setting up Sphinx for documentation of your Python project is not as easy as it seems.
Well, if you want to do it properly. This document walks you through the basic setup.

Preparations
------------
First, make sure your dependencies are set-up properly. 
Download Sphinx with pip (`pip install sphinx`) and, while you're at it,
download the ReadTheDocs-theme (`pip install sphinx_rtd_theme`) - in my opinion
the nicest template (to see how it looks like, check e.g. skbold.readthedocs.io).

Sphinx-quickstart
-----------------
Once you're all set up, create a directory `docs` in the root of your package and run the command
`sphinx-quickstart` in your terminal. This will prompt you to set a couple of options.
I recommend going with the default values, except for the following options:
`autodoc`, `mathjax`, `ifconfig`, `viewcode`, and `Makefile` - set these to `y`.
(Set `Windows command file`, obviously, to `n`).

Now, this quickstart command created three files:

- conf.py: a file with settings for Sphinx
- index.rst: the 'master-doc' (kinda like a index.html file)
- Makefile: a makefile to create, once you have a bunch of .rst-files, html pages with a single command

Conf.py settings
----------------
You can customize you're entire Sphinx setup in the conf.py file. Here, I outline some recommended
settings.

- 

