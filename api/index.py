from youtube_dl import YoutubeDL
from flask import Flask, Response, request, jsonify
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def root(path):
  url=request.args.get('url') or path
  info=YoutubeDL({}).extract_info(url, download=False)
  return info

@app.route('/version')
def version():
  return jsonify(youtube_dl.version.__version__)
