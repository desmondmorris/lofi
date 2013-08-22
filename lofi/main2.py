from flask import Flask, request
import json, os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(
        #host=app.config['LOFI_HOST'],
        port=int(os.environ['PORT'])
    )