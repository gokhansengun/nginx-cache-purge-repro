from flask import Flask, request, make_response
from datetime import datetime
import os
import time

app = Flask(__name__)

sleep_time = os.getenv('SLEEP_TIME', 0.001)

@app.route('/')
def home_page():
    time.sleep(sleep_time)

    response = make_response(f'This is home page response {datetime.now()}')
    response.headers['Cache-Control'] = 'private, no-cache, no-store, max-age=0, must-revalidate'

    return response

@app.route('/category/<category_name>')
def category_page(category_name):
    time.sleep(sleep_time)

    response = make_response(f'This is category {category_name} response {datetime.now()}')
    response.headers['Cache-Control'] = 'private, no-cache, no-store, max-age=0, must-revalidate'

    return response

@app.route('/api/<path:path>')
def api(path):
    time.sleep(sleep_time)

    response = make_response(f'This is an API response from {path}! {datetime.now()}')

    return response

@app.route('/test/api/<path:path>')
def test_api(path):
    time.sleep(sleep_time)

    response = make_response(f'This is an API response from test/api/{path}! {datetime.now()}')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
