(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (factory((global.platform = global.platform || {}))); //changer ici le nom du module
}(this, (function (exports) {

  var getProjectsPaths = function(){
    api.getProjectsPaths().then(function(a){
      $('#projects_paths').html('');
      result = '';
      for (i in a){
        result += '<li onmouseenter="platform.showRemovePath(this);" onmouseleave="platform.hideRemovePath(this);">' + a[i] + ' <span class="glyphicon glyphicon-remove" onclick="platform.removeProjectsPaths(this)" aria-hidden="true" style="cursor:pointer;visibility:hidden;"></span></li>';
      }
      result += '<li><div class="input-group" style="display:inline-flex;left:-5px;width:60%">' +
                '  <input type="text" id="add_proj_path_text" class="form-control" placeholder="enter the path..." style="height:22px;padding:0px 0px 0px 5px;">' +
                '  <span class="input-group-btn">' +
                '    <button class="btn btn-success" type="button" style="padding:0px 10px;" onclick="platform.addProjectsPaths()"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button>' +
                '  </span>' +
                '</div></li>'
      $('#projects_paths').html(result);
      $('#select_path_new_proj').html('');
      result = '';
      for (i in a){
        result += '<option value="' + a[i] + '">' + a[i] + '</option>';
      }
      $('#select_path_new_proj').html(result);
      $('#select_path_new_proj').selectpicker('refresh');

      $('#add_proj_path_text').keypress(function(event) {
        if (event.keyCode == 13) {
          addProjectsPaths();
        }
      });
    })
  }

  var addProjectsPaths = function(){
    new_path = $('#add_proj_path_text').val();
    api.addProjectsPaths(new_path).then(function(a){
      $.toaster({ message : a['message'], priority : 'success' });
      show_list_proj();
    })
  }

  var removeProjectsPaths = function(el){
    path = $(el.parentElement.childNodes[0]).text().replace(' ', '');
    if (confirm("Are you sure that you want to remove this path?")){
      api.removeProjectsPaths(path).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        show_list_proj();
      })
    }
  }

  var showRemovePath = function(el){
    list_span = el.getElementsByTagName('span');
    for (var i = 0 ; i < list_span.length ; i++){
      list_span[i].style.visibility = 'visible';
    }
  }

  var hideRemovePath = function(el){
    list_span = el.getElementsByTagName('span');
    for (var i = 0 ; i < list_span.length ; i++){
      list_span[i].style.visibility = 'hidden';
    }
  }

  var createNewProject = function(){
    path = $('#select_path_new_proj').val();
    name = $('#name_new_proj').val();
    api.createNewProject(path, name).then(function(a){
      api.createNewScript($('#select_path_new_proj').val(), $('#name_new_proj').val(), "universe").then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        show_list_proj();
        $('#new_project').modal('hide');
      })
    })
  }

  var editProj = function(path, proj){
    globals.edit_path = path;
    globals.edit_name = proj;
    api.getProjectsPaths().then(function(a){
      $('#select_path_edit_proj').html('');
      result = '';
      for (i in a){
        result += '<option value="' + a[i] + '">' + a[i] + '</option>';
      }
      $('#select_path_edit_proj').html(result);
      $('#select_path_edit_proj').val(path);
      $('#select_path_edit_proj').selectpicker('refresh');
    })
    $('#name_edit_proj').val(proj);
  }

  var editProject = function(){
    path = $('#select_path_edit_proj').val();
    name = $('#name_edit_proj').val();
    api.editProject(globals.edit_path, globals.edit_name, path, name).then(function(a){
      $.toaster({ message : a['message'], priority : 'success' });
      show_list_proj();
      $('#edit_project').modal('hide');
    })
  }

  var setNewProj = function(el){
    $('#select_path_new_proj').val($(el).attr('path'));
    $('#select_path_new_proj').selectpicker('refresh');
  }

  var changeWidget = function(){
    api.getHtmlPlatformWidget($('#select_platform_widget').val()).then(function(c){
      $('#list_proj').html('');
      $('#list_proj').html(c);
    })
  }

  var openProject = function(project_path, proj){
    globals.project_path = project_path;
    globals.project = proj;
    $('#header').text(proj);
    $('#list_proj').hide();
    $('#project').show();
    globals.vue = 'project';
    $('#back').show();
    api.getProjectWidgets(globals.project_path, globals.project).then(function(a){
        $('#select_project_widget').html('');
        result = '';
        for (i in a){
          result += '<option value="' + a[i] + '">' + a[i] + '</option>';
        }
        $('#select_project_widget').html(result);
        api.getProjectActuWidget(globals.project_path, globals.project).then(function(b){
            $('#select_project_widget').val(b[0]);
            $('#select_project_widget').selectpicker('refresh');
            api.getHtmlProjectWidget(b).then(function(c){
              $('#project').html('');
              $('#project').html(c);
              widget_project.show_scripts_proj();
              project.openScript('universe');
            })
        })
    });
  }

  exports.getProjectsPaths = getProjectsPaths;
  exports.addProjectsPaths = addProjectsPaths;
  exports.removeProjectsPaths = removeProjectsPaths;
  exports.showRemovePath = showRemovePath;
  exports.hideRemovePath = hideRemovePath;
  exports.createNewProject = createNewProject;
  exports.editProj = editProj;
  exports.editProject = editProject;
  exports.setNewProj = setNewProj;
  exports.changeWidget = changeWidget;
  exports.openProject = openProject;

  Object.defineProperty(exports, '__esModule', { value: true });
})));