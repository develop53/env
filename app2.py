from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    response = Response('Sunucu 2')
    response.headers['cache-control'] = 'max-age=10'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)    