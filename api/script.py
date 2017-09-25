from api.app import app
from flask import jsonify, request
import srcs.script
import json

@app.route('/script', methods=['GET'])
def get_script():
    if not request.args or not 'path' in request.args or not 'name' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    return jsonify(srcs.script.get_script(request.args.get('path'), request.args.get('name')))

@app.route('/script', methods=['POST'])
def create_script():
    if not request.json or not 'path' in request.json or not 'name' in request.json or not 'script' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.create_script(request.json['path'], request.json['name'], request.json['script'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/script', methods=['DELETE'])
def delete_script():
    if not request.json or not 'path' in request.json or not 'name' in request.json or not 'script' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.delete_script(request.json['path'], request.json['name'], request.json['script'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/script', methods=['PUT'])
def edit_script():
    if not request.json or not 'path' in request.json or not 'name' in request.json \
        or not 'old_script' in request.json or not 'script' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.edit_script(request.json['path'], request.json['name'],
            request.json['old_script'], request.json['script'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/content_function', methods=['GET'])
def get_content_function():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script_name' in request.args or not 'func' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.get_content_function(request.args['path'], request.args['project'],
            request.args['script_name'], request.args['func'])
    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/content_function', methods=['PUT'])
def set_content_function():
    if not request.json or not 'path' in request.json or not 'project' in request.json \
        or not 'script_name' in request.json or not 'func' in request.json or not 'content' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.set_content_function(request.json['path'], request.json['project'],
            request.json['script_name'], request.json['func'], request.json['content'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/run_script', methods=['GET'])
def run_script():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script_name' in request.args or not 'func' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.run_script(request.args['path'], request.args['project'],
            request.args['script_name'], json.loads(request.args['func']))
    return jsonify(result), 200

@app.route('/run_script_return', methods=['GET'])
def run_script_return():
    if not request.args or not 'path' in request.args or not 'project' in request.args or not 'script_name' in request.args or not 'func' in request.args or not 'api' in request.args or not 'pos' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.script.run_script_return(request.args['path'], request.args['project'],
            request.args['script_name'], json.loads(request.args['func']), request.args['api'], int(request.args['pos']))
    return jsonify(result), 200
