# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'Diskpop'
copyright = '2024, Alice Somigliana, Giovanni Rosotti, Leonardo Testi, Giuseppe Lodato, Marco Tazzari, Claudia Toci, Rossella Anania, Benoit Tabone'
authors = 'Alice Somigliana, Giovanni Rosotti, Leonardo Testi, Giuseppe Lodato, Marco Tazzari, Claudia Toci, Rossella Anania, Benoit Tabone'
copyright = '2021-%d, %s' % (datetime.now().year, authors)

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx_rtd_theme',
	'sphinx.ext.autodoc',
	'sphinx.ext.napoleon',
	'sphinx.ext.viewcode',
	'myst_parser',
	'sphinx.ext.intersphinx',
	'sphinx.ext.doctest',
    'sphinx-jsonschema',
]


#intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

autodoc_member_order = "bysource"
master_doc = "index"

napoleon_google_docstring = False
autodoc_preserve_defaults = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = {
	'.rst': 'restructuredtext',
	'.txt': 'markdown',
	'.md': 'markdown',
}


import re

def remove_default_value(app, what, name, obj, options, signature, return_annotation):
    if signature:
        search = re.findall(r"(\w*)=", signature)
        if search:
            signature = "({})".format(", ".join([s for s in search]))

    return (signature, return_annotation)

#def setup(app):
#    app.connect("autodoc-process-signature", remove_default_value)
    
def setup(app):
  app.add_css_file( "_static/pygments.css" )

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

man_pages = [
    (master_doc, 'Diskpop', u'Diskpop Documentation',
     [authors], 1)
]


html_logo = 'images/Logo_transparent.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}