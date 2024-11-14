from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)
def timeget():
  datenow = datetime.now()
  timenow = datenow.strftime('%I:%M %P')
  return timenow
storage = [{'time': timeget()}]
@app.route('/', methods=['GET'])
def time():
  return jsonify(storage)
