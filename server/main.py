from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Server Up!</h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=9874)          