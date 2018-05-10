basic_test_widget
===============================

Basic jupyter widget for testing.

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
