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

Add path
~~~~~~~~ 
To make sure Sphinx can find your source files, modify `sys.path`::

    `sys.path.insert(0, os.path.abspath('.'))
    sys.path.insert(0, os.path.abspath('../'))`
 
Enable Numpy-docstrings
~~~~~~~~~~~~~~~~~~~~~~~
To enable Numpy-docstrings (the legible alternative to regular Python docstrings), add the following:

- `sphinx_ext_napoleon` to the `extensions` list;
- set `napoleon_use_ivar = True`; this enables attributes to be documented;
- set `napoleon_include_init_with_doc`; this enables parsing of `__init__` methods (if desired);

Some settings to make the documentation look nicer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- set `add_function_parentheses = False`;
- set `add_module_names = False`;

HTML options
~~~~~~~~~~~~
To enable the RTD-theme, add the following::

	import sphinx_rtd_theme
	html_theme = "sphinx_rtd_theme"
	html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

Also add `suppress_warnings = ['image.nonlocal_uri']`.

Makefile settings
-----------------
You can modify your Makefile to add a `make latex` command that builds a PDF-version of your documentation;
there are plenty of resources on how to do that online.

Run apidoc
----------
Sphinx-apidoc is a Sphinx tool that automatically parses your \*.py files and generates
documentation for them in the format of .rst files. Before running this, let's first create a directory, `source`,
in which to store the to-be-created .rst file (assuming that you're in `docs`)::

        $ mkdir source

Then, when invoking apidoc, you want to run something along the following command::

        $ sphinx-apidoc -o source [opts] [packagedir] [patterns_to_exclude]

To make life easier, I created a short bash-script that does this (with some recommended options): `run_apidoc.sh`.
After running this, you'll see that Sphinx created a bunch of rst-files in the `source/` directory.

Now, in a final step, let's transform the rst-files to html using the makefile::

        $ make html

Check out the `_build/html` directory - this should contain (amongst other files) an `index.html`.
Click it and check out your brand new documentation!

Tips & tricks
-------------
I often like to include my README.rst of my main repository in my documentation (keeps the info
from Github, PyPI, and your documentation in sync). This is very easy to do: just open your
index.rst, remove the first line ("Welcome to {package}'s documentation!"), and add::

.. include:: ../README.rst

Now, in this document, you also see a "toctree" definition. This is a table-of-contents object,
which we'd like to list our code documentation. To do so, simply add `source/src` underneath it
(watch the indentation!). Now, rebuild your html, and you'll see a nice list of our code!
(You can adjust the 'depth' of the toctree with the argument `maxdepth`.
 
Serve your documentation!
-------------------------
As a very last step, we need to upload and host our newly created documentation software. 
For this, there are two (main) choices: ReadTheDocs.org or using github-pages. 
ReadTheDocs is basically a plugin for Github, that looks for a docs/ 
directory and then will build the documentation. This can be done for any branch
(or even multiple branches simultaneously) and can also output latex-rendered PDFs.
For most packages/projects, this is somewhat overkill though, so I generally
recommend just using github-pages. For more info on RTD, check `http://ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/`.

To use github-pages to serve your documentation, simply create your html-files (`make html`),
create a new branch - `gh-pages` - and put those html-files (found under docs/_build/html) at the root-directory.
*Make sure to remove all other directories and include a .nojekyll file* (this is used by Github internally to
include files/directories with an underscore). Now, push your gh-pages branch to github. If you now go to the
settings tab of your repo, then you'll find a GitHub Pages section in which you can set the 'Source' to the
gh-pages branch. After you've done this, you can go to {your-github-name.github.io/{packagename} to check
out your documentation!

(I automated the creation/updating of the documentation with a script: update_docs_and_push.sh. Invoking this script will
call `make html` and transfer it to the gh-pages branch and then push that branch, with some housekeeping in between. You
can also choose for a regular push to your current brain on origin; in that case, append 'rtd' to your call to the function.)
