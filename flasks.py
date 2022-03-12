import os
from flask import Flask, jsonify, request
import random

class Car:
    def __init__(self,nome):
        self.nome=nome
        self.cavalos=random.randint(0,100)
    def addCavalo(self):
        return self.cavalos+1

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "hello Word"})

@app.route('/nome/<name>')
def nomes(name):
    car=Car(name)
    return jsonify({"nome": car.nome,"cavalos":car.cavalos,"cavalos+1":car.addCavalo()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
