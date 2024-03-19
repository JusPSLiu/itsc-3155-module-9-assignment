# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_existing_title():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    movie_repository.create_movie('Titanic', 'James Cameron', 5)
    
    found_movie = movie_repository.get_movie_by_title('Titanic')
    assert found_movie is not None
    assert found_movie.title == 'Titanic'
    assert found_movie.director == 'James Cameron'
    assert found_movie.rating == 5

def test_get_movie_by_non_existing_title():
    movie_repository = get_movie_repository()
    not_found_movie = movie_repository.get_movie_by_title('No Movie')
    assert not_found_movie is None