import os

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def reroute(*, path=None):
    return redirect(os.environ.get('url'), code=302)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
