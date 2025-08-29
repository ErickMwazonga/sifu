'''
A movie club contains many movies.
Each movie has a title and one or more directors.
A movie may be borrowed and returned from the club.

Write a class Movie and another class MovieClub with appropriate
instance variables and methods to implement the scenario. 
Also, write a method to return the current number of movies in the club
'''


from typing import Union


class Movie:

    def __init__(self, title: str, directors: Union[str, list]):
        self.title = title
        self.directors = []

        if isinstance(directors, list):
            self.directors.extend(directors)
        else:
            self.directors.append(directors)

    def __str__(self):
        return f'A movie with title: {self.title} has been created'

    def add_director(self, director_name: str):
        if director_name in self.directors:
            return(f'The Director {director_name} already exists')

        self.directors.append(director_name)
        return(
            f'The Director {director_name} has been added to movie {self.title}'
        )

    def get_directors(self):
        for key, director in self.directors.enumerate():
            print(f'{key}: {director}')


class MovieClub:

    def __init__(self, name: str):
        self.name = name
        self.movies: dict = {}
        self.no_of_movies = 0

    def add_movie_instance(self, movie: Movie):
        title = movie.title

        if title in self.movies.keys():
            return(f'The movie {title} already exists')

        self.movies[title] = movie
        self.no_of_movies += 1

    def add_movie(self, title: str, directors: Union[str, list]):
        movie = Movie(title, directors)
        self.add_movie_instance(movie)

    def get_no_of_movies(self):
        return self.no_of_movies

    def get_movies(self):
        if not self.movies:
            return('There are no movies')

        for key, title in self.movies.keys():
            print(f'{key}: {title}')


movie_club = MovieClub('TIMBERLAND')
assert movie_club.get_no_of_movies() == 0
assert movie_club.get_movies() == 'There are no movies'

fast_n_furious = Movie('Fast n Furious', 'Stingo')
assert fast_n_furious.directors == ['Stingo']
fast_n_furious.add_director('Mambo')
assert fast_n_furious.directors == ['Stingo', 'Mambo']

# Existing Director
fast_n_furious.add_director('Mambo') == 'The Director Mambo already exists'

movie_club.add_movie_instance(fast_n_furious)
assert movie_club.no_of_movies == 1

movie_club.add_movie('Django', 'Them Brother')
assert movie_club.no_of_movies == 2

# Existing Movie
movie_club.add_movie_instance(
    fast_n_furious) == 'The movie Fast n Furious already exists'

assert movie_club.no_of_movies == 2
