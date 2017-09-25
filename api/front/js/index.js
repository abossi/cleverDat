$(document).ready(function(){
	$('#project').hide();
	$('#function').hide();
	$('#back').hide();
	api.getPlatformWidgets().then(function(a){
      $('#select_platform_widget').html('');
      result = '';
      for (i in a){
        result += '<option value="' + a[i] + '">' + a[i] + '</option>';
      }
      $('#select_platform_widget').html(result);
		api.getPlatformActuWidget().then(function(b){
		    $('#select_platform_widget').val(b[0]);
		    $('#select_platform_widget').selectpicker('refresh');
			api.getHtmlPlatformWidget(b).then(function(c){
				$('#list_proj').html('');
				$('#list_proj').html(c);
			})
		})
	});

	$('#name_new_proj').keypress(function(event) {
	    if (event.keyCode == 13) {
	        platform.createNewProject();
	    }
	});

	$('#name_edit_proj').keypress(function(event) {
	    if (event.keyCode == 13) {
	        platform.editProject();
	    }
	});

	$('#name_new_script').keypress(function(event) {
	    if (event.keyCode == 13) {
	        project.createNewScript();
	    }
	});

	$('#name_edit_script').keypress(function(event) {
	    if (event.keyCode == 13) {
	        project.editScript();
	    }
	});
});

var backVue = function(){
	switch (globals.vue){
	case 'platform':
		break;
	case 'project':
		globals.vue = 'platform';
		$('#back').hide();
		$('#project').hide();
		$('#list_proj').show();
    	$('#header').text('list of projects');
    	show_list_proj();
		break;
	case 'function':
		globals.vue = 'project';
		globals.position['imp'] = -1;
		globals.position['proc'] = -1;
		globals.position['exp'] = -1;
		$('#function').hide();
		$('#project').show();
    	$('#header').text(globals.project);
    	widget_project.show_scripts_proj();
		break;
	default:
		break;
	}
}