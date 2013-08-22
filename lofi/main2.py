from flask import Flask, request
import json, os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(
        host=os.environ['HOST'],
        port=int(os.environ['PORT'])
    )