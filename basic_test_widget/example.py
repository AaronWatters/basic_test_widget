import ipywidgets as widgets
from traitlets import Unicode
import traitlets

@widgets.register
class HelloWorld(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('HelloView').tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_module = Unicode('basic_test_widget').tag(sync=True)
    _model_module = Unicode('basic_test_widget').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Unicode('Hello World!').tag(sync=True)
    rendered = traitlets.Bool(False).tag(sync=True)
