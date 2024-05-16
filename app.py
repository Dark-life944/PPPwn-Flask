# -*- coding: utf-8 -*-
# app.py

from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    # Retorna a página HTML com o botão
     return render_template('index.html')

@app.route('/start_exploit', methods=['POST'])
def start_exploit():
    # Configuração padrão para executar o pppwn
    command = [
        "/usr/local/bin/pppwn",
        "--interface", "en0",
        "--fw", "1100",
        "--stage1", "/data/stage1.bin",
        "--stage2", "/data/stage2.bin",
        "--auto-retry"
    ]
    try:
        # Executa o comando pppwn
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return jsonify({'status': 'success', 'output': result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'output': e.stderr}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

