#!/usr/bin/python

import imdb
import sys

new = imdb.IMDb()

movie_name = ''
for arg in sys.argv[1:]:
    movie_name += arg + ' '

try:
    movie_name = movie_name[:len(movie_name) - 1]

    movies = new.search_movie(movie_name)
    # # print(dir(movies[0]))
    movie_code = movies[0].movieID

    new_movie = new.get_movie(movie_code)
    # dictionary created from object

    # print the keys available
    # print(new_movie.infoset2keys)
    # {u'plot': [u'plot', u'synopsis'], u'main': [u'production managers', u'rating', u'special effects companies', u'casting directors', u'distributors', u'music department', u'runtimes', u'special effects', u'thanks', u'year', u'production companies', u'color info', u'composers', u'costume designers', u'votes', u'visual effects', u'title', u'writer', u'editors', u'languages', u'cinematographers', u'writers', u'camera department', u'certificates', u'country codes', u'language codes', u'production designers', u'casting department', u'editorial department', u'assistant directors', u'sound mix', u'location management', u'genres', u'miscellaneous', u'producers', u'director', u'set decorators', u'original air date', u'costume departmen', u'akas', u'aspect ratio', u'sound department', u'stunts', u'kind', u'make up department', u'other companies', u'art department', u'countries', u'transportation department', u'plot outline', u'cast', u'directors', u'art directors', u'cover url']}

    # print(new_movie.current_info)
    # print('taglines' in new_movie)
    print(new_movie['title'])
    print(new_movie['year'])
    print('\nGenres: ')
    for genre in new_movie['genres']:
        print(genre)
    print('\nIMDb Rating: ' + str(new_movie['rating']) + '\n')

    print('Cast: ')
    for actor in new_movie['cast'][0:5]:
        print(actor)
    print('\n' + new_movie['plot outline'])
except IndexError:
    print('Movie not found!')
