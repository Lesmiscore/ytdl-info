import youtube_dl
from flask import Flask, Response, request, jsonify
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def root(path):
  path=path[4:]
  if request.args.get('version'):
    return jsonify(youtube_dl.version.__version__)
  url=request.args.get('url') or path
  info=youtube_dl.YoutubeDL({}).extract_info(url, download=False)
  return info

#@app.route('/version')
#def version():
#  return jsonify(youtube_dl.version.__version__)
