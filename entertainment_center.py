import media
import fresh_tomatoes

'''
This is the file where instances of the movie classes are
instantiated and fresh_tomatoes
receives the list to spin up the webpage
'''

goodfellas = media.Movie("Goodfellas",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/"
                         "Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=2ilzidi_J8Q")

a_goofy_movie = media.Movie("A Goofy Movie",
                            "https://upload.wikimedia.org/wikipedia/en/"
                            "thumb/f/f3/A_Goofy_Movie_poster.jpg/220"
                            "px-A_Goofy_Movie_poster.jpg",
                            "https://youtu.be/dHrzG5tHjJ0")

rocky = media.Movie("Rocky",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/"
                    "1/18/Rocky_poster.jpg/220px-Rocky_poster.jpg",
                    "https://www.youtube.com/watch?v=3VUblDwa648")

grease = media.Movie("Grease",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/"
                     "e/e2/Grease_ver2.jpg/220px-Grease_ver2.jpg",
                     "https://www.youtube.com/watch?v=f2CCEixOVVU")

# list of movies
movies = [goodfellas, a_goofy_movie, rocky, grease]

# page is opened
fresh_tomatoes.open_movies_page(movies)
