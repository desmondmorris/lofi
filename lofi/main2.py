from flask import Flask, request
import json, os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.environ.get('PORT', 33507))
    )