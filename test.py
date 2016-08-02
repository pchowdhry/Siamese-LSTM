from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


def test(ss):
    kk = ss+'yyyy'
    return kk

@app.route('/', methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    kr = request_data.get('input')

    return test(test(kr))