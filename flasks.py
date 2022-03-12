import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hello Word"})

@app.route('/nome/<name>')
def nomes(name):
    return jsonify({"message": name})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
