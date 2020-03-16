import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # print 'request host: {host}'.format(request.host)
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
