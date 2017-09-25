from api.app import app
from flask import jsonify, request, send_from_directory
import srcs.settings_project

@app.route('/plugins_paths', methods=['GET'])
def get_plugins_paths():
    if not request.args or not 'path' in request.args or not 'project' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json",
        }), 400
    return jsonify(srcs.settings_project.get_plugins_paths(request.args.get('path') + '/' + request.args.get('project')))

@app.route('/plugins_paths', methods=['POST'])
def add_plugins_paths():
    if not request.json or not 'path' in request.json or not 'project' in request.json or not 'plugin_path' in request.json:
        return jsonify({"status": "error",
                "message": "error in json"
        }), 400
    result = srcs.settings_project.add_plugins_paths(request.json['path'] + '/' + request.json['project'], request.json['plugin_path'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/plugins_paths', methods=['DELETE'])
def remove_plugins_paths():
    if not request.json or not 'path' in request.json or not 'project' in request.json or not 'plugin_path' in request.json:
        return jsonify({"status": "error",
                "message": "error in json"
        }), 400
    result = srcs.settings_project.remove_plugins_paths(request.json['path'] + '/' + request.json['project'], request.json['plugin_path'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/project_list_widgets', methods=['GET'])
def get_project_list_widgets():
    if not request.args or not 'path' in request.args or not 'project' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json",
        }), 400
    return jsonify(srcs.settings_project.get_project_list_widgets(request.args.get('path') + '/' + request.args.get('project')))

@app.route('/project_actu_widget', methods=['GET'])
def get_project_actu_widget():
    if not request.args or not 'path' in request.args or not 'project' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json",
        }), 400
    return jsonify([srcs.settings_project.get_project_actu_widget(request.args.get('path') + '/' + request.args.get('project'))])

@app.route('/get_project_widget/<path:path>', methods=['GET'])
def get_project_widget(path):
    return send_from_directory('front/project', path + '.html'), 200
