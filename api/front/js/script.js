(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (factory((global.script = global.script || {}))); //changer ici le nom du module
}(this, (function (exports) {

  var loadPluginsFunctions = function(){
    api.getPlugins(globals.project_path, globals.project, globals.script, ['imp', 'proc', 'exp']).then(function(a){
      $('#function_import_list_plugin').html('');
      var result = '<a href="#" class="list-group-item disabled" style="cursor:default;">plugins list</a>';
      for (var i = 0 ; i < a['imp'].length ; i++){
        result += '<a href="#" class="list-group-item plugin" onmouseenter="platform.showRemovePath(this);" onmouseleave="platform.hideRemovePath(this);" onclick="script.load_plugin_widget(\'imp\', \'' + a['imp'][i] + '\', this, ' + i + ')"';
        if (globals.position['imp'] == i)
          result += 'style="background-color:#ccc;"';
        result += '>' + a['imp'][i] + ' <span class="glyphicon glyphicon-remove" onclick="event.stopPropagation();script.removePlugin(\'imp\', ' + i + ');" aria-hidden="true" style="cursor:pointer;visibility:hidden;"></span></a>';
      }
      result += '<a class="list-group-item plugin list-group-item-success add-plugin" aria-hidden="true" data-toggle="modal" data-target="#new_plugin" onclick="script.setListPlugins(\'imp\')"><i class="fa fa-plus" aria-hidden="true"></i></a>'
      $('#function_import_list_plugin').html(result);
      $('#function_process_list_plugin').html('');
      var result = '<a href="#" class="list-group-item disabled" style="cursor:default;">plugins list</a>';
      for (var i = 0 ; i < a['proc'].length ; i++){
        result += '<a href="#" class="list-group-item plugin" onmouseenter="platform.showRemovePath(this);" onmouseleave="platform.hideRemovePath(this);" onclick="script.load_plugin_widget(\'proc\', \'' + a['proc'][i] + '\', this, ' + i + ')"';
        if (globals.position['proc'] == i)
          result += 'style="background-color:#ccc;"';
        result += '>' + a['proc'][i] + ' <span class="glyphicon glyphicon-remove" onclick="event.stopPropagation();script.removePlugin(\'proc\', ' + i + ');" aria-hidden="true" style="cursor:pointer;visibility:hidden;"></span></a>';
      }
      result += '<a class="list-group-item plugin list-group-item-success add-plugin" aria-hidden="true" data-toggle="modal" data-target="#new_plugin" onclick="script.setListPlugins(\'proc\')"><i class="fa fa-plus" aria-hidden="true"></i></a>'
      $('#function_process_list_plugin').html(result);
      $('#function_export_list_plugin').html('');
      var result = '<a href="#" class="list-group-item disabled" style="cursor:default;">plugins list</a>';
      for (var i = 0 ; i < a['exp'].length ; i++){
        result += '<a href="#" class="list-group-item plugin" onmouseenter="platform.showRemovePath(this);" onmouseleave="platform.hideRemovePath(this);" onclick="script.load_plugin_widget(\'exp\', \'' + a['exp'][i] + '\', this, ' + i + ')"';
        if (globals.position['exp'] == i)
          result += 'style="background-color:#ccc;"';
        result += '>' + a['exp'][i] + ' <span class="glyphicon glyphicon-remove" onclick="event.stopPropagation();script.removePlugin(\'exp\', ' + i + ');" aria-hidden="true" style="cursor:pointer;visibility:hidden;"></span></a>';
      }
      result += '<a class="list-group-item plugin list-group-item-success add-plugin" aria-hidden="true" data-toggle="modal" data-target="#new_plugin" onclick="script.setListPlugins(\'exp\')"><i class="fa fa-plus" aria-hidden="true"></i></a>'
      $('#function_export_list_plugin').html(result);
      $('#header').text(globals.project + ' ' + globals.script);
      $('#project').hide();
      $('#function').show();
      globals.vue = 'function';
    })
  }

  var showRemovePlugin = function(el){
    list_span = el.getElementsByTagName('span');
    for (var i = 0 ; i < list_span.length ; i++){
      list_span[i].style.visibility = 'visible';
    }
  }

  var hideRemovePlugin = function(el){
    list_span = el.getElementsByTagName('span');
    for (var i = 0 ; i < list_span.length ; i++){
      list_span[i].style.visibility = 'hidden';
    }
  }

  var change_view = function(func){
  	$('#function_' + globals.func).css('display', 'none');
  	globals.func = func;
  	$('#function_' + globals.func).css('display', 'block');
  }

  var load_plugin_widget = function(func, plugin, el, pos){
    if (el !== null){
  	 $(el).parent().children(".plugin").css('background-color', '');
  	 $(el).css('background-color', '#ccc');
    }
  	globals.position[func] = pos;
  	globals.plugin = plugin;
  	//TODO: load the plugin widget like a boss
    var div = '';
    switch(func){
    case 'imp':
      div = '#import_widget_plugin';
      break;
    case 'proc':
      div = '#process_widget_plugin';
      break;
    case 'exp':
      div = '#export_widget_plugin';
      break;
    }
    $(div).html('');
    if (pos == -1){
      api.getContentFunction(globals.project_path, globals.project, globals.script, func).then(function(a){
        globals.editors[func] = CodeMirror($(div).get(0), {
          value: a.message,
          lineNumbers: true
        });
        $(div).append('<button type="button" class="btn btn-primary" style="margin: 1vh;float: right;font-size: 2vh;" onclick="script.writeContentFunction(\'' + func + '\')">Write <span class="glyphicon glyphicon-save" aria-hidden="true"></span></button>');
      })
    }
    else{
		api.getHtmlPluginWidget(globals.project_path, globals.project, globals.script, plugin).then(function(c){
			$(div).html('');
			$(div).html(c);
		})
    }
  }

  var setListPlugins = function(func){
  	api.getPluginsProject(globals.project_path, globals.project, func).then(function(a){
		$('#select_plugin').html('');
		result = '';
		for (i in a){
			result += '<option value="' + a[i] + '">' + a[i] + '</option>';
		}
		$('#select_plugin').html(result);
		$('#select_plugin').selectpicker('refresh');
		set_select_plugin();
    	$('#position_plugin').prop('value', 0);
		switch(func){
		case 'imp':
			$('#position_plugin').prop('max', $('#function_import_list_plugin').children().length - 2);
			break;
		case 'proc':
			$('#position_plugin').prop('max', $('#function_process_list_plugin').children().length - 2);
			break;
		case 'exp':
			$('#position_plugin').prop('max', $('#function_export_list_plugin').children().length - 2);
			break;
		}
  	})
  }

  var set_select_plugin = function(){
	  $('#select-plugin-image').attr("src","/front/plugins/png/" + globals.project_path.replace(/^\//, '') + '/' + globals.project + '/' + $('#select_plugin').val());
  }

  var addPlugin = function(){
  	var func = '';
    var max = 0;
  	switch(globals.func){
  	case 'import':
  		func = 'imp';
      max = $('#function_import_list_plugin').children().length - 2;
  		break;
  	case 'process':
  		func = 'proc';
      max = $('#function_process_list_plugin').children().length - 2;
  		break;
  	case 'export':
  		func = 'exp';
      max = $('#function_export_list_plugin').children().length - 2;
  		break;
  	}
  	api.addScriptPlugin(globals.project_path, globals.project, globals.script, $('#select_plugin').val(), func, max - $('#position_plugin').val()).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
  		  loadPluginsFunctions();
        if (globals.position[func] >= $('#position_plugin').val())
          globals.position[func]++;
        $('#new_plugin').modal('hide');
  	})
  }

  var removePlugin = function(func, pos){
  	if (globals.position[func] === undefined)
  		return ;
  	if (confirm("Are you sure that you want to remove this plugin?")){
  		api.removeScriptPlugin(globals.project_path, globals.project, globals.script, globals.plugin, func, pos).then(function(a){
        $.toaster({ message : a['message'], priority : 'success' });
        if (pos == globals.position[func]){
          globals.position[func] = -1;
          switch(func){
          case 'imp':
            $('#import_widget_plugin').html('');
            break;
          case 'proc':
            $('#process_widget_plugin').html('');
            break;
          case 'exp':
            $('#export_widget_plugin').html('');
            break;
          }
        }
        else if (pos < globals.position[func])
          globals.position[func]--;
        loadPluginsFunctions();
  		})
  	}
  }

  var writeContentFunction = function(func){
    var str = globals.editors[func].getValue().replace(/\n(?!$)/g, '\n            ').replace(/^/, '            ');
    if (!str.match(/\n$/))
      str += '\n';
    if (str.match(/^\s*$/))
      str = '            pass\n'
    api.setContentFunction(globals.project_path, globals.project, globals.script, func, str).then(function(a){
      $.toaster({ message : a['message'], priority : 'success' });
      load_plugin_widget(func, null, null, -1);
    })
  }

  var runScript = function(script){
    api.runScript(globals.project_path, globals.project, script, ['imp', 'proc', 'exp']).then(function(a){
      result = ''
      if (a.__stdout__ !== undefined && a.__stdout__['imp'] !== '' && a.__stdout__['imp'] !== undefined){
        a.__stdout__['imp'] = '<div class="well well-sm"><div>' + a.__stdout__['imp'] + '</div></div>';
        a.__stdout__['imp'] = a.__stdout__['imp'].replace(/\n/g, '</div><div>');
        result += '<div>Import function</div>' + a.__stdout__['imp'];
      }
      if (a.__stdout__ !== undefined && a.__stdout__['proc'] !== '' && a.__stdout__['proc'] !== undefined){
        a.__stdout__['proc'] = '<div class="well well-sm"><div>' + a.__stdout__['proc'] + '</div></div>';
        a.__stdout__['proc'] = a.__stdout__['proc'].replace(/\n/g, '</div><div>');
        result += '<div>Process function</div>' + a.__stdout__['proc'];
      }
      if (a.__stdout__ !== undefined && a.__stdout__['exp'] !== '' && a.__stdout__['proc'] !== undefined){
        a.__stdout__['exp'] = '<div class="well well-sm"><div>' + a.__stdout__['exp'] + '</div></div>';
        a.__stdout__['exp'] = a.__stdout__['exp'].replace(/\n/g, '</div><div>');
        result += '<div>Export function</div>' + a.__stdout__['exp'];
      }
      if (a['status'] === 'danger'){
        a['error'] = '<div class="well well-sm"><div>' + a['error'] + '</div></div>';
        a['error'] = a['error'].replace(/\n/g, '</div><div>');
        result += '<div>ERROR</div>' + a['error'];
      }
      if (result !== '')
        $.toaster({title: a['script'] + ' script' , message : result, priority : a['status'], settings: {timeout: 8000}});
    })
  }

  exports.loadPluginsFunctions = loadPluginsFunctions;
  exports.change_view = change_view;
  exports.load_plugin_widget = load_plugin_widget;
  exports.set_select_plugin = set_select_plugin;
  exports.setListPlugins = setListPlugins;
  exports.addPlugin = addPlugin;
  exports.removePlugin = removePlugin;
  exports.writeContentFunction = writeContentFunction;
  exports.runScript = runScript;
  
  Object.defineProperty(exports, '__esModule', { value: true });
})));