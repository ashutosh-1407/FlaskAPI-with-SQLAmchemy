from flask import Flask
from werkzeug.wrappers import ResponseStreamMixin
from routes import configure_routes
from db import db, app
configure_routes(app, db)
client = app.test_client()

def test_base_route():  
    url = '/'
    response = client.get(url)
    assert response.get_data() == b'Flask API + SQLAlchemy + postgresql'
    assert response.status_code == 200

def test_review_route():
    url = '/review/1'
    response = client.get(url)
    assert response.status_code == 200

def test_product_route():
    url = '/product/1'
    response = client.get(url)
    assert response.status_code == 200

def test_user_route():
    url = '/user/1'
    response = client.get(url)
    assert response.status_code == 200