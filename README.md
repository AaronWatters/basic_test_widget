basic_test_widget
===============================

Basic jupyter widget for testing widget deployment.

Installation
------------

To install use pip:

    $ pip install basic_test_widget
    $ jupyter nbextension enable --py --sys-prefix basic_test_widget


For a development installation (requires npm),

    $ git clone https://github.com/AaronWatters/basic_test_widget.git
    $ cd basic_test_widget
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix basic_test_widget
    $ jupyter nbextension enable --py --sys-prefix basic_test_widget

For jupyterlab also do

    $ jupyter labextension install js

The following must have been run once at sometime in the past:

    $ jupyter labextension install @jupyter-widgets/jupyterlab-manager
