from api.app import app
from flask import jsonify, request, send_from_directory
import srcs.plugin
import json
import os

@app.route('/plugins', methods=['GET'])
def get_script_plugin():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script_name' in request.args or not 'func' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.plugin.get_script_plugin(request.args['path'], request.args['project'],
            request.args['script_name'], json.loads(request.args['func']))
    if not 'status' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/plugins', methods=['POST'])
def add_script_plugin():
    if not request.json or not 'path' in request.json or not 'project' in request.json or not 'script' in request.json or not 'plugin' in request.json or not 'func' in request.json or not 'pos' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.plugin.add_script_plugin(request.json['path'], request.json['project'], request.json['script'], request.json['plugin'], request.json['func'], request.json['pos'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/plugins', methods=['DELETE'])
def remove_script_plugin():
    if not request.json or not 'path' in request.json or not 'project' in request.json or not 'script' in request.json or not 'plugin' in request.json or not 'func' in request.json or not 'pos' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.plugin.remove_script_plugin(request.json['path'], request.json['project'], request.json['script'], request.json['plugin'], request.json['func'], request.json['pos'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/plugin_widget', methods=['GET'])
def get_plugin_widget():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script' in request.args or not 'plugin' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    return send_from_directory(os.path.join('..', srcs.plugin.projects[os.path.join(request.args['path'], request.args['project'])]['plugins'][request.args['plugin']]['path'], request.args['plugin']), request.args['plugin'] + '.html')

@app.route('/plugins_param', methods=['GET'])
def get_script_plugin_param():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script' in request.args or not 'func' in request.args or not 'pos' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.plugin.get_script_plugin_param(request.args['path'], request.args['project'], request.args['script'], request.args['func'], request.args['pos'])
    if not 'status' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/plugins_param', methods=['PUT'])
def set_script_plugin_param():
    if not request.json or not 'path' in request.json or not 'project' in request.json or not 'script' in request.json or not 'func' in request.json or not 'pos' in request.json or not 'parameters' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.plugin.set_script_plugin_param(request.json['path'], request.json['project'], request.json['script'], request.json['func'], request.json['pos'], request.json['parameters'])
    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/front/plugins/png/<path:path>', methods=['GET'])
def get_plugin_image_path(path):
    ar = path.rsplit('/', 1)
    for key in srcs.plugin.projects.keys():
        if key.endswith(ar[0]):
            for c in key[:len(key) - len(ar[0])]:
                if not c in "./":
                    break
            else:
                return send_from_directory(os.path.join('..', srcs.plugin.projects[key]['plugins'][ar[1]]['path'], ar[1]), ar[1] + '.png')
    return '', 404
