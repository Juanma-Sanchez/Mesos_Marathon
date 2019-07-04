from flask import Flask, json, request

from mesos.client import MarathonClient

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_applications():
    marathon_response = MarathonClient().get()

    response = app.response_class(
        response=json.dumps(marathon_response.json()),
        status=marathon_response.status_code,
        mimetype='application/json'
    )
    return response


@app.route('/', methods=['POST'])
def create_application():
    payload = request.get_json()
    app_id = payload.get('id')
    basic_json = open('basic.json', 'r')
    app_data = json.load(basic_json)
    app_data['id'] = app_id

    marathon_response = MarathonClient().post(
        json=app_data
    )

    response = app.response_class(
        response=json.dumps(marathon_response.json()),
        status=marathon_response.status_code,
        mimetype='application/json'
    )
    return response


@app.route('/<app_id>/', methods=['GET'])
def get_details(app_id):
    relative_url = '/' + app_id
    marathon_response = MarathonClient().get(
        relative_url=relative_url
    )

    response = app.response_class(
        response=json.dumps(marathon_response.json()),
        status=marathon_response.status_code,
        mimetype='application/json'
    )
    return response


@app.route('/<app_id>/', methods=['DELETE'])
def remove_application(app_id):
    relative_url = '/' + app_id
    marathon_response = MarathonClient().delete(
        relative_url=relative_url
    )

    response = app.response_class(
        response=json.dumps(marathon_response.json()),
        status=marathon_response.status_code,
        mimetype='application/json'
    )
    return response
