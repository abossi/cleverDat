from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('front', 'index.html')

@app.route('/front/<path:path>', methods=['GET'])
def get_extern(path):
    return send_from_directory('front', path)
