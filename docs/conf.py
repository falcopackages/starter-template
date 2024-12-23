# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'falco-starter-template'
copyright = '2024, Tobi DEGNON'
author = 'Tobi DEGNON'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.extlinks",
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_docsearch",
]

todo_include_todos = True
extlinks = {
    "pull": ("https://github.com/falcopackages/starter-template/pull/%s", "pull request #%s"),
    "issue": ("https://github.com/falcopackages/starter-template/issues/%s", "issue #%s"),
    "repo": ("https://github.com/falcopackages/starter-template", "github repository"),
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']
html_baseurl = "https://falco.oluwatobi.dev"
html_title = "Falco"

# -- Shibuya theme options ---------------------------------------------------
html_context = {
    "source_type": "github",
    "source_user": "falcopackages",
    "source_repo": "falco-app",
}
html_theme_options = {
    "mastodon_url": "https://fosstodon.org/@tobide",
    "github_url": "https://github.com/falcopackages/starter-template",
    "twitter_url": "https://twitter.com/tobidegnon",
    "discussion_url": "https://github.com/falcopackages/falco-app/discussions",
    "accent_color": "blue",
    "globaltoc_expand_depth": 1,
}
html_logo = "https://raw.githubusercontent.com/falcopackages/falco/refs/heads/main/docs/_static/logo_with_text.svg"
html_favicon = "https://raw.githubusercontent.com/falcopackages/falco/refs/heads/main/docs/_static/falco-logo.svg"