from datetime import datetime

project = 'quickDB'
release = '0.0.5'
templates_path = ['_templates']
source_suffix = ".rst"
master_doc = "index"
year = datetime.now().year
copyright = "{} Py-Contributors".format(year)
extensions = ['sphinx.ext.autosectionlabel']
releases_github_path = "Py-Contributors/python-db"
autosectionlabel_prefix_document = True
html_theme = 'sphinx_rtd_theme'  # 'pydata_sphinx_theme' 'alabaster'
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}
