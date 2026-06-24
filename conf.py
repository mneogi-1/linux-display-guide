# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ''

copyright = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx.ext.autosectionlabel', 'sphinx.ext.githubpages','sphinxcontrib.video','sphinx_design','linuxdoc.rstFlatTable','sphinx_tabs.tabs','sphinx_new_tab_link']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

exclude_patterns = ["topic\qli-display\displayport_panel_and_clock_information.rst", "topic\qli-display\dsi_panel_and_clock_information.rst", "topic\qli-display\regulator_and_clock_information copy.rst", "topic\qli-display\regulator_and_clock_information.rst", "topic\qli-display\bringup.rst", "topic\qli-display\snapdragon_display_manager_sdm_drm_architecture.rst", "topic\qli-display\drm_kms_adreno_dpu_driver_architecture.rst", "topic\qli-display\dsi_panel_and_clock_information.rst"]
 
latex_elements = {'figure_align': 'H'}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title =''

html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False