from flask import Flask, request, jsonify
import json
from extractor import valorant_extractor

app = Flask(__name__)

@app.route('/process_request', methods=['POST'])
def process_request():
    try:
        data = request.get_json()
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400

    client_address = request.remote_addr
    print(f"RECEBIDO DE {client_address}: {data} \n")
    
    if data.get('type') == "chat":
        response = valorant_extractor.getGPTRequest(data)
    elif data.get('uuid') is None:
        response = valorant_extractor.fullExtractor(data)
    else:
        response = valorant_extractor.singleExtractor(data)

    # Retorna a resposta como JSON
    print(f"RESPOSTA ENVIADA PARA: {client_address}\n")
    return jsonify(response)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8080
    print(f"\nSERVIDOR RODANDO EM: http://{HOST}:{PORT} \n")
    app.run(host=HOST, port=PORT)
