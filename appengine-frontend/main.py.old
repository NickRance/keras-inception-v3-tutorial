import config
import logging
from flask import current_app, Flask, render_template, request
import urllib2
import storage
import base64
import json

app = Flask(__name__)
app.config.from_object(config)

logging.basicConfig(level=logging.INFO)


def upload_image_file(stream, filename, content_type):
    if not stream:
        return None

    public_url = storage.upload_file(
        stream,
        filename,
        content_type
    )

    current_app.logger.info(
        "Uploaded file %s as %s.", filename, public_url)

    return 'https://storage.cloud.google.com' + public_url


def fetch_predictions(img_stream):
    predictions = {}
    server_url = current_app.config['PREDICTION_SERVICE_URL']
    req = urllib2.Request(server_url, json.dumps({'data': base64.b64encode(img_stream)}),
                          {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
        predictions = json.loads(f.read())
    except urllib2.HTTPError as e:
        current_app.logger.exception(e)

    current_app.logger.info('Predictions: %s', predictions)
    return predictions


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        img = request.files.get('image')

        img_stream = img.read()
        filename = img.filename
        content_type = img.content_type
        img_url = upload_image_file(img_stream, filename, content_type)

        predictions = fetch_predictions(img_stream=img_stream)

        return render_template('view.html', image_url=img_url, predictions=predictions['predictions'])
    return render_template('form.html')


@app.errorhandler(500)
def server_error(e):
    current_app.logger.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
