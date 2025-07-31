from flask import Flask, render_template, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'hostname': socket.gethostname(),
        'version': '1.0.0'
    })

@app.route('/api/info')
def app_info():
    return jsonify({
        'app_name': 'Flask Interview Lab',
        'version': '1.0.0',
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'port': os.environ.get('PORT', 5000)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)