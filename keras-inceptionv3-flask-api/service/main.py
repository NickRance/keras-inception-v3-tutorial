from flask import Flask, current_app, request, jsonify
import io
import model
import base64
from pprint import pprint

app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    data = {}
    try:
        #print(request.get_json()['data'])
        data = request.get_json()
        pprint(data)
        data = data['data']
    except KeyError:
        return jsonify(status_code='400', msg='Bad Request'), 400

    data = base64.b64decode(data)
    # print("Decoded Data: "+ data)
    image = io.BytesIO(data)
    predictions = model.predict(image)
    current_app.logger.info('Predictions: %s', predictions)
    return jsonify(predictions=predictions)

# @app.route('/', methods=['GET'])
# def noRoute():
#     return("Try again with a POST")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
