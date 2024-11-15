from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)
def timeget():
  dt = datetime.now()
  time = dt.strftime('%H:%M %P')
  return time
storage = [{'time': timeget()}]
@app.route('/', methods=['GET'])
def getstore():
  return jsonify(storage)
