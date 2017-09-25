(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (factory((global.globals = global.globals || {}))); //changer ici le nom du module
}(this, (function (exports) {

  var vue = 'platform';

  var edit_path = '';
  var edit_name = '';

  var project_path = '';
  var project = '';
  var func = 'import';
  var position = {};
  var editors = {};

  exports.vue = vue;
  exports.edit_path = edit_path;
  exports.edit_name = edit_name;
  exports.project_path = project_path;
  exports.project = project;
  exports.func = func;
  exports.position = position;
  exports.editors = editors;

  Object.defineProperty(exports, '__esModule', { value: true });
})));