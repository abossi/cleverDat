(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (factory((global.api = global.api || {}))); //changer ici le nom du module
}(this, (function (exports) {

  var getPlatformWidgets = function(){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/platform_list_widgets',
      type : 'GET',
      dataType : 'json',
      success : function(json){
        
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
        error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getPlatformActuWidget = function(){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/platform_actu_widget',
      type : 'GET',
      dataType : 'json',
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getHtmlPlatformWidget = function(widget){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/get_platform_widget/' + widget,
      type : 'GET',
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getProjectWidgets = function(path, project){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/project_list_widgets',
      type : 'GET',
      data: {
        path: path,
        project: project
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getProjectActuWidget = function(path, project){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/project_actu_widget',
      type : 'GET',
      data: {
        path: path,
        project: project
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
        error : function(resultat, statut, erreur){
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getHtmlProjectWidget = function(widget){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/get_project_widget/' + widget,
      type : 'GET',
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getProjects = function(){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects',
      type : 'GET',
      dataType : 'json',
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get project list!');
      }
    });

    return deferred.promise();
  }

  var getProjectsPaths = function(){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects_paths',
      type : 'GET',
      dataType : 'json',
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get projects paths!');
      }
    });

    return deferred.promise();
  }

  var addProjectsPaths = function(new_path){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects_paths',
      type : 'POST',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': new_path}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var removeProjectsPaths = function(path){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects_paths',
      type : 'DELETE',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var createNewProject = function(path, name){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects',
      type : 'POST',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'name': name}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var removeProject = function(path, name){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects',
      type : 'DELETE',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'name': name}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var editProject = function(old_path, old_name, path, name){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/projects',
      type : 'PUT',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'old_path': old_path, 'old_name': old_name, 'path': path, 'name': name}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var getPluginsPaths = function(path, project){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_paths',
      type : 'GET',
      data : {
        path: path,
        project: project
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get projects paths!');
      }
    });

    return deferred.promise();
  }

  var addPluginsPaths = function(path, project, plugin_path){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_paths',
      type : 'POST',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'plugin_path': plugin_path}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var removePluginsPaths = function(path, project, plugin_path){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_paths',
      type : 'DELETE',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'plugin_path': plugin_path}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var getPluginsProject = function(path, project, func){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_project',
      type : 'GET',
      data : {
        path: path,
        project: project,
        func: func
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        alert('Impossible to get projects paths!');
      }
    });

    return deferred.promise();
  }

  var getScript = function(path, name){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/script',
      type : 'GET',
      data : {
        path: path,
        name: name
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve({'result': json, 'path': path, 'name': name}); //affectation du json dans une variable global
        return {'result': json, 'path': path, 'name': name};
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var createNewScript = function(path, name, script){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/script',
      type : 'POST',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'name': name, 'script': script}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var deleteScript = function(path, name, script){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/script',
      type : 'DELETE',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'name': name, 'script': script}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var editScript = function(path, name, old_script, script){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/script',
      type : 'PUT',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'name': name, 'old_script': old_script, 'script': script}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var getPlugins = function(path, project, script_name, functions){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script_name: script_name,
        func: '["imp","proc","exp"]'
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var addScriptPlugin = function(path, project, script, plugin, func, pos){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins',
      type : 'POST',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'script': script, 'plugin': plugin, 'func': func, 'pos': pos}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var removeScriptPlugin = function(path, project, script, plugin, func, pos){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins',
      type : 'DELETE',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'script': script, 'plugin': plugin, 'func': func, 'pos': pos}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var getScriptPluginParam = function(path, project, script, func, pos){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_param',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script: script,
        func: func,
        pos: pos
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var setScriptPluginParam = function(path, project, script, func, pos, parameters){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugins_param',
      type : 'PUT',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'script': script, 'func': func, 'pos': pos, 'parameters': parameters}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var getHtmlPluginWidget = function(path, project, script, plugin){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/plugin_widget',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script: script,
        plugin: plugin,
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : 'No widget for this plugin. Just make one! ;)', priority : 'warning', settings : { 'timeout' : 5000 } });
      }
    });

    return deferred.promise();
  }

  var getContentFunction = function(path, project, script_name, func){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/content_function',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script_name: script_name,
        func: func
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var setContentFunction = function(path, project, script_name, func, content){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/content_function',
      type : 'PUT',
      contentType: "application/json; charset=utf-8",
      dataType : 'json',
      data: JSON.stringify({'path': path, 'project': project, 'script_name': script_name, 'func': func, 'content': content}),
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var runScript = function(path, project, script_name, functions){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/run_script',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script_name: script_name,
        func: '["imp","proc","exp"]'
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  var runScriptReturn = function(path, project, script_name, functions, api, pos){
    var deferred = new $.Deferred();
    $('#loading-wrapper').toggleClass('transform-active');
    $.ajax({
      url : '/run_script_return',
      type : 'GET',
      data : {
        path: path,
        project: project,
        script_name: script_name,
        func: '["imp","proc","exp"]',
        api: api,
        pos: pos
      },
      success : function(json){
        $('#loading-wrapper').toggleClass('transform-active');
        deferred.resolve(json); //affectation du json dans une variable global
        return json;
      },
      error : function(resultat, statut, erreur){
        $('#loading-wrapper').toggleClass('transform-active');
        $.toaster({ message : JSON.parse(resultat.responseText)['message'], priority : 'danger' });
        console.log(resultat)
      }
    });

    return deferred.promise();
  }

  exports.getPlatformWidgets = getPlatformWidgets;
  exports.getPlatformActuWidget = getPlatformActuWidget;
  exports.getHtmlPlatformWidget = getHtmlPlatformWidget;
  exports.getProjectWidgets = getProjectWidgets;
  exports.getProjectActuWidget = getProjectActuWidget;
  exports.getHtmlProjectWidget = getHtmlProjectWidget;
  exports.getProjects = getProjects;
  exports.getProjectsPaths = getProjectsPaths;
  exports.addProjectsPaths = addProjectsPaths;
  exports.removeProjectsPaths = removeProjectsPaths;
  exports.createNewProject = createNewProject;
  exports.removeProject = removeProject;
  exports.editProject = editProject;
  exports.getPluginsPaths = getPluginsPaths;
  exports.addPluginsPaths = addPluginsPaths;
  exports.removePluginsPaths = removePluginsPaths;
  exports.getPluginsProject = getPluginsProject;
  exports.getScript = getScript;
  exports.createNewScript = createNewScript;
  exports.deleteScript = deleteScript;
  exports.editScript = editScript;
  exports.getPlugins = getPlugins;
  exports.addScriptPlugin = addScriptPlugin;
  exports.removeScriptPlugin = removeScriptPlugin;
  exports.getScriptPluginParam = getScriptPluginParam;
  exports.setScriptPluginParam = setScriptPluginParam;
  exports.getHtmlPluginWidget = getHtmlPluginWidget;
  exports.getContentFunction = getContentFunction;
  exports.setContentFunction = setContentFunction;
  exports.runScript = runScript;
  exports.runScriptReturn = runScriptReturn;

  Object.defineProperty(exports, '__esModule', { value: true });
})));
