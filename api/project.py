from api.app import app
from flask import jsonify, request, redirect, url_for, Flask
from werkzeug.utils import secure_filename
import srcs.project
import os

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(srcs.project.get_proj())

@app.route('/projects', methods=['POST'])
def create_projects():
    if not request.json or not 'path' in request.json or not 'name' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.project.create_proj(request.json['path'], request.json['name'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/projects', methods=['DELETE'])
def delete_projects():
    if not request.json or not 'path' in request.json or not 'name' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.project.delete_proj(request.json['path'], request.json['name'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/projects', methods=['PUT'])
def edit_projects():
    if not request.json or not 'path' in request.json or not 'name' in request.json \
        or not 'old_path' in request.json or not 'old_name' in request.json:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    result = srcs.project.edit_proj(request.json['old_path'], request.json['old_name'],
            request.json['path'], request.json['name'])
    if result['status'] == 'success':
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/plugins_project', methods=['GET'])
def get_plugins_project():
    if not request.args or not 'path' in request.args or not 'project' in request.args \
        or not 'func' in request.args:
        return jsonify({
                "status": "error",
                "message": "error in json"
        }), 400
    project = request.args['path'] + '/' + request.args['project']
    return jsonify(srcs.project.get_plugins_project(project, request.args['func']))

@app.route('/load_file/<path:path>', methods=['POST'])
def load_file(path):
    print(dict(request.files)['file_data'][0].filename)
    file = dict(request.files)['file_data'][0]
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(path, filename))
    return jsonify(['OK']), 200
