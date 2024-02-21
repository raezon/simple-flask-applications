from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/info')
def info():
    return jsonify({'application': 'Simple Python Flask App', 'version': '1.0'})

@app.route('/api/data')
def data():
    # Exemple de données retournées, vous pouvez personnaliser cela
    return jsonify({'data': [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
