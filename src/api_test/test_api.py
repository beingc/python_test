from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/test', methods=['POST'])
def api_test():
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
