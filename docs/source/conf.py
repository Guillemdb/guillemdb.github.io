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
from importlib.machinery import SourceFileLoader
import os
from pathlib import Path
import sys

from invoke import run


sys.path.insert(0, os.path.abspath("../../"))
sys.setrecursionlimit(1500)


def read_version() -> str:
    """Load the project configuration from the target path."""
    version = SourceFileLoader(
        "retrospective.version",
        str(Path(__file__).parent / "retrospective" / "version.py"),
    ).load_module()
    return version.__version__


def symlink_project_folders():
    source_dir = Path(__file__).parent
    if (source_dir.parent / "build").exists():
        run(f"rm -rf {source_dir.parent / 'build'}")
    if (source_dir / "retrospective").exists():
        run(f"rm -rf {source_dir / 'retrospective'}")
    run(f"ln -sr {source_dir.parent.parent / 'src' / 'retrospective'} {source_dir}")


symlink_project_folders()
# -- Project information -----------------------------------------------------

project = "Guillem Duran Ballester"
copyright = "2021, Guillem Duran Ballester"
author = "Guillem Duran"

# The short X.Y version


__version__ = read_version()
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__
# -- General configuration ---------------------------------------------------
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
# The master toctree document.
master_doc = "index"
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinx.ext.githubpages",
]
# suppress_warnings = ["image.nonlocal_uri"]
autodoc_typehints = "description"


# Ignore sphinx-autoapi warnings on multiple target description
# suppress_warnings.append("ref.python")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# myst_parser options
myst_heading_anchors = 2
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
