from api.app import app
from flask import jsonify, request, send_from_directory
import srcs.settings_platform

@app.route('/projects_paths', methods=['GET'])
def get_projects_paths():
    return jsonify(srcs.settings_platform.get_projects_paths())

@app.route('/projects_paths', methods=['POST'])
def add_projects_paths():
    if not request.json or not 'path' in request.json:
        return jsonify({"status": "error",
                "message": "error in json"
        }), 400
    result = srcs.settings_platform.add_projects_paths(request.json['path'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/projects_paths', methods=['DELETE'])
def remove_projects_paths():
    if not request.json or not 'path' in request.json:
        return jsonify({"status": "error",
                "message": "error in json"
        }), 400
    result = srcs.settings_platform.remove_projects_paths(request.json['path'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/platform_list_widgets', methods=['GET'])
def get_platform_list_widgets():
    return jsonify(srcs.settings_platform.get_list_widgets())

@app.route('/platform_actu_widget', methods=['GET'])
def get_platform_actu_widget():
    return jsonify([srcs.settings_platform.get_actu_widget()])

@app.route('/get_platform_widget/<path:path>', methods=['GET'])
def get_platform_widget(path):
    return send_from_directory('front/platform', path + '.html'), 200
