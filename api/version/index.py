import youtube_dl
from flask import Flask, Response, request, jsonify
app = Flask(__name__)

@app.route('/version')
def version():
  return jsonify(youtube_dl.version.__version__)
