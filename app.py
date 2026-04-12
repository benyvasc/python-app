from flask import Flask, render_template_string
import socket
from datetime import datetime

app = Flask(__name__)

# Template HTML simples definido como string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Informações do Sistema</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f2f5; }
        .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; }
        p { font-size: 1.2rem; color: #333; }
        strong { color: #555; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Status do Servidor</h1>
        <p><strong>Data e Hora:</strong> {{ data_atual }}</p>
        <p><strong>Hostname:</strong> {{ hostname }}</p>
        <p><strong>Endereço IP:</strong> {{ ip_interno }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Coleta das informações
    hostname = socket.gethostname()
    ip_interno = socket.gethostbyname(hostname)
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    return render_template_string(HTML_TEMPLATE, 
                                 hostname=hostname, 
                                 ip_interno=ip_interno, 
                                 data_atual=data_atual)

if __name__ == '__main__':
    # O host '0.0.0.0' permite que a aplicação seja acessada por outros dispositivos na mesma rede
    app.run(host='0.0.0.0', port=5000)