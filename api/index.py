from youtube_dl import YoutubeDL
from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  url=request.args.get('url') or path
  info=YoutubeDL({}).extract_info(url, download=False)
  return info
