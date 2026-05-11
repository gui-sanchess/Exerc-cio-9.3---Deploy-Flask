from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # O host 0.0.0.0 é fundamental para funcionar na nuvem
    app.run(host='0.0.0.0', port=8000)