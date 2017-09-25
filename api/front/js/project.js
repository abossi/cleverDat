(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (factory((global.project = global.project || {}))); //changer ici le nom du module
}(this, (function (exports) {

  var getPluginsPaths = function(){
    api.getPluginsPaths(globals.project_path, globals.project).then(function(a){
      $('#plugins_paths').html('');
      result = '';
      for (i in a){
        result += '<li onmouseenter="platform.showRemovePath(this);" onmouseleave="platform.hideRemovePath(this);">' + a[i] + ' <span class="glyphicon glyphicon-remove" onclick="project.removePluginsPaths(this)" aria-hidden="true" style="cursor:pointer;visibility:hidden;"></span></li>';
      }
      result += '<li><div class="input-group" style="display:inline-flex;left:-5px;width:60%">' +
                '  <input type="text" id="add_plugin_path_text" class="form-control" placeholder="enter the path..." style="height:22px;padding:0px 0px 0px 5px;">' +
                '  <span class="input-group-btn">' +
                '    <button class="btn btn-success" type="button" style="padding:0px 10px;" onclick="project.addPluginsPaths()"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button>' +
                '  </span>' +
                '</div></li>'
      $('#plugins_paths').html(result);
      $('#select_path_new_proj').html('');
      result = '';
      for (i in a){
        result += '<option value="' + a[i] + '">' + a[i] + '</option>';
      }
      $('#select_path_new_proj').html(result);
      $('#select_path_new_proj').selectpicker('refresh');

      $('#add_plugin_path_text').keypress(function(event) {
        if (event.keyCode == 13) {
          project.addPluginsPaths();
        }
      });
    })
  }

  var addPluginsPaths = function(){
    new_path = $('#add_plugin_path_text').val();
    api.addPluginsPaths(globals.project_path, globals.project, new_path).then(function(a){
      $.toaster({ message : a['message'], priority : 'success' });
      getPluginsPaths(globals.project_path, globals.project);
    })
  }

  var removePluginsPaths = function(el){
    path = $(el.parentElement.childNodes[0]).text().replace(' ', '');
    if (confirm("Are you sure that you want to remove this path?")){
      api.removePluginsPaths(globals.project_path, globals.project, path).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        getPluginsPaths(globals.project_path, globals.project);
      })
    }
  }

  var createNewScript = function(){
    api.createNewScript(globals.project_path, globals.project, $('#name_new_script').val()).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        widget_project.show_scripts_proj();
        $('#new_script').modal('hide');
    })
  }

  var editScr = function(script){
    globals.edit_script = script;
    $('#name_edit_script').val(script);
  }

  var editScript = function(){
    api.editScript(globals.project_path, globals.project, globals.edit_script, $('#name_edit_script').val()).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        widget_project.show_scripts_proj();
        $('#edit_script').modal('hide');
    })
  }

  var openScript = function(scr){
    $('#import_widget_plugin').html('');
    $('#process_widget_plugin').html('');
    $('#export_widget_plugin').html('');
    globals.script = scr;
    $('#functions_tabs a').click(function (e) {
      e.preventDefault()
      $(this).tab('show')
    })
    script.loadPluginsFunctions();
  }

  exports.getPluginsPaths = getPluginsPaths;
  exports.addPluginsPaths = addPluginsPaths;
  exports.removePluginsPaths = removePluginsPaths;
  exports.createNewScript = createNewScript;
  exports.editScr = editScr;
  exports.editScript = editScript;
  exports.openScript = openScript;

  Object.defineProperty(exports, '__esModule', { value: true });
})));
