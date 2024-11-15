from flask import Flask, jsonify, request
app = Flask(__name__)
store = {'hello': 'hello'}
@app.route('/', methods=['GET'])
def return_store():
  return jsonify(store)
