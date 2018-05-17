var basic_test_widget = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'basic_test_widget',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'basic_test_widget',
          version: basic_test_widget.version,
          exports: basic_test_widget
      });
  },
  autoStart: true
};

