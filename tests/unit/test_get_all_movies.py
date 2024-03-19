# TODO: Feature 1
from flask import render_template_string
import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope='module')
def test_app():
    with app.app_context():
        yield app.test_client()

def test_list_movies(test_app: FlaskClient):
    #add movie
    get_movie_repository().create_movie("mov", "dir", 2)

    #checc if movie ther
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    print(response_data)

    #i expect that the movie, the director, and two stars will show up
    #idk if github will allow all these qhitespaces but i refuse to change
    #the spacing in the jinja stuff for readability
    expectedStuf = '''<td>mov</td>
            <td>dir</td>
            <td>
            
                
                    <img src="https://pluspng.com/img-png/star-png-star-png-image-2156.png" style="height:15px;">
                
            
                
                    <img src="https://pluspng.com/img-png/star-png-star-png-image-2156.png" style="height:15px;">
                
            
                
                    <img src="https://cdn.onlinewebfonts.com/svg/img_548678.png" style="height:17px">'''
    print("Expected:")
    print(expectedStuf)
    assert expectedStuf in response_data