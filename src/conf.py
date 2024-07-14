# Configuration file for the Sphinx documentation builder.

# Standard Python Libraries
import os
import sys
import re

# Optional Imports
# import shutil  # Uncomment if needed

# Path Setup
sys.path.insert(0, os.path.abspath("./_ext"))

# -- Project Information -----------------------------------------------------
project = 'Tudat Developer'
copyright = '2023, Tudat Space'
release = '0.1.4.dev7'

# Retrieve authors from the AUTHORS file
with open("../AUTHORS", "r") as f:
    author = ', '.join(list(re.findall(r"^\*\s(.*)", f.read(), re.MULTILINE)))

# -- General Configuration ---------------------------------------------------
extensions = [
    "sphinxcontrib.bibtex",
    "sphinx_copybutton",
    "sphinx.ext.graphviz",
    "sphinx_design",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.contentui",
    "furocontrib.mermaid",
    "helloworld",
    "sphinxcontrib.imagesvg",
    "sphinxext.rediraffe",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Extension Settings ------------------------------------------------------
bibtex_bibfiles = ['primer/primer.bib']
bibtex_default_style = 'unsrt'

# Sphinx Mermaid Extension
# Uncomment below for specific Mermaid.js configurations
# mermaid_params = {
#     'init': {'startOnLoad': False},
#     # ... other Mermaid.js configurations ...
# }

graphviz_output_format = 'svg'

rediraffe_redirects = {
    "guides/hybrid_modules.rst": "how-to-guides/create-hybrid-tudatpy-modules.rst",
    "guides/new_forge_feedstock.rst": "how-to-guides/create-a-conda-feedstock.rst",
    "primer/devops/versioning.rst": "how-to-guides/version-package-releases.rst",
    "guides/defining_environment_variables.rst": "how-to-guides/define-program-environment-variables.rst",
    "guides/contribution_checklists.rst": "reference/contribution-checklists.rst",
    "resources/commands.rst": "reference/commands.rst",
    "resources/tools.rst": "reference/tools.rst"
}

# -- HTML Output Options -----------------------------------------------------
html_theme = "furo"
html_title = f'{project}'
html_static_path = ['_static']
html_logo = "_static/cover_modified.png"

html_css_files = [
    'custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
]

html_js_files = [
    'custom.js',
    # 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js',
]

# -- Customizations and Features ---------------------------------------------
panels_add_fontawesome_latex = True
todo_include_todos = False
