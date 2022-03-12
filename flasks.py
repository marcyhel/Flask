import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    return jsonify({"message": "hello Word"})

@app.route('/nome/<name>')
def nao_entre_em_panico(nome):
    return jsonify({"message": nome})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
