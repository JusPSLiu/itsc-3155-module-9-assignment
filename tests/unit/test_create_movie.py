import pytest
from src.repositories.movie_repository import get_movie_repository

from app import app as flask_app


# TODO: Feature 2

class TestCreateMovie:

    @classmethod
    def setup_class(cls):
        cls.movie_repository = get_movie_repository()


    def test_case_1(self):

        movie_name = 'Titanic'
        director_name = 'James Cameron'
        rating = 5
        
        #Case 1: movie rating is added to the database and is present inside of it
        movie = self.movie_repository.create_movie('Titanic', 'James Cameron', 5)

        #movie should be present in the database
        data_base_movie = self.movie_repository.get_movie_by_title("Titanic")
        assert (data_base_movie.title == 'Titanic' and data_base_movie.director == 'James Cameron' and data_base_movie.rating == 5)

        pass
    

        


    

   


