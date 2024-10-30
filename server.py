from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import argparse

from gpt_api import Gptapi

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<p>API funcionando</p>"

@app.route('/agentes', methods=['GET',])
def agentes():
    print("requisição: ", request)
    uuid = request.args.get('uuid')

    header = "https://valorant-api.com/v1/"

    if not uuid:
        url = f"{header}agents?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])
    else:
        url = f"{header}agents/{uuid}?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])

@app.route('/mapas', methods=['GET',])
def mapas():
    print("requisição: ", request)
    uuid = request.args.get('uuid')

    header = "https://valorant-api.com/v1/"

    if not uuid:
        url = f"{header}maps?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])
    else:
        url = f"{header}maps/{uuid}?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])

@app.route('/armas', methods=['GET',])
def armas():
    print("requisição: ", request)
    uuid = request.args.get('uuid')

    header = "https://valorant-api.com/v1/"

    if not uuid:
        url = f"{header}weapons?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])
    else:
        url = f"{header}weapons/{uuid}?language=pt-BR&isPlayableCharacter=true"
        response = requests.get(url).json()
        return jsonify(response["data"])
    
@app.route('/chat', methods=['POST', ])
def chat():
    print("requisição: ", request)
    print(request.get_json("msg"))
    print(request.get_data())

    data = request.get_json()
    msg = data.get("msg")

    gpt = Gptapi()
    return gpt.send_message(msg)

parser = argparse.ArgumentParser(description='valorant wiki server')
parser.add_argument('port', nargs='?', default=5000)
args = parser.parse_args()

app.run(port=args.port, debug=True)
