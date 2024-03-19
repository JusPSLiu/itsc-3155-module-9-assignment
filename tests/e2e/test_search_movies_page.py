# TODO: Feature 3
from flask.testing import FlaskClient

def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    
    assert b'<form action="/movies/search" method="GET"' in response.data

    response = test_app.get('/movies/search?title=Titanic')
    assert response.status_code == 200

    assert b'Titanic' in response.data
