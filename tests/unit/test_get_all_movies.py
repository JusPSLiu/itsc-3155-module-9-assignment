# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository

def test_list_movies():
    #add movie
    movie_repo = get_movie_repository()
    new_movie = movie_repo.create_movie("mov", "dir", 2)

    #assert its there
    assert new_movie.movie_id in movie_repo.get_all_movies()

    #assert its got stuff
    assert "mov" is new_movie.title
    assert "dir" is new_movie.director
    assert 2 is new_movie.rating

    #take it back
    new_movie = movie_repo.get_all_movies()[new_movie.movie_id]
    #make sure its still got stuff
    assert "mov" is new_movie.title
    assert "dir" is new_movie.director
    assert 2 is new_movie.rating