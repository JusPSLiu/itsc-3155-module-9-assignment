import pytest
from src.repositories.movie_repository import get_movie_repository

from app import app as flask_app
import pytest

class TestCreateMoviesPage:

    
    @pytest.fixture
    def app(self):
        yield flask_app


    #this function allows you to make requests to your application and test the responses without running the server.
    @pytest.fixture
    def client(self,app):
        return app.test_client()



    def test_clicking_on_create_movie_button_redirects_to_create_movie_page(self,client):
        response = client.get('/')
        
        # Simulate clicking on the create movie button
        response = client.get('/movies/new')
        

        
        # Assert that the response redirects to the create movie page
        assert response.status_code == 200

        # shouldn't redirect to any other page
        assert response.location == None

        pass


    def test_html_code_is_present_on_website(self,client):
        response = client.get('/')
        
        response = client.get('/movies/new')

        # Assert that the response contains most of the HTML code for the index page

        print(response.data)
        
        assert b'<form action="/movies" method="post">' in response.data
        assert b'<input type="text" class="form-control" id="movieName" name="movieName" required>' in response.data
        assert b'<label for="directorName" class="form-label">Director</label>' in response.data
        assert b'<input type="text" class="form-control" id="directorName" name="directorName" required>' in response.data
        assert b'<label for="rating" class="form-label">Rating</label>' in response.data
        assert b'<select class="form-select" id="rating" name="rating" required>' in response.data
        assert b'<button type="submit" class="btn btn-primary">Submit</button>' in response.data
    

        pass

    def test_valid_form_submission_is_accepted(self,client):
        response = client.get('/')
        
        response = client.get('/movies/new')

        response = client.post('/movies', data={
            'movieName': 'Titanic', 
            'directorName': 'James Cameron', 
            'rating': 5}
            )  


        
        
        # Assert that the response redirects to the list all movies page
        assert response.status_code == 302

        print(response.location)
        assert response.location == '/movies'
        
        
        pass



    def test_invalid_form_submission_is_rejected(self,client):
        response = client.get('/')

        response = client.get('/movies/new')
        
        response = client.post('/movies', data={'movieName': 'Titanic', 3: 'James Cameron', 'rating': 'invalid'})
        
        # Assert that the response redirects to the create movie page again
        assert response.status_code == 302
        assert response.location == '/movies/new'

        pass
    



