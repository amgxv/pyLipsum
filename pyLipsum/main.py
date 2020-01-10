from flask import Flask, request
from ipsum import chiquito_output
from simple_chiquito import simple_chiquito
from dicts.chiquitoDict import chiquitoDict
from dicts.ipsumDict import ipsumDict

app = Flask(__name__)

@app.route('/')
def paragraph():
    dic = chiquitoDict
    if request.args.get('dict') == 'ipsumDict':
        dic = ipsumDict
    par = request.args.get('par', default=1, type=int)
    lorem = request.args.get('lorem', default=False, type=bool)
    return chiquito_output(dic, par, lorem)

@app.route('/simple')
def phrase():
    return simple_chiquito()

if __name__ == "__main__":
    app.run()
    