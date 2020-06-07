import webbrowser

'''
Movie class that contains all information about movie to be displayed
'''


class Movie():
    """Construct a new movie object

    :param movie_title: The name of the movie
    :param poster_image_url: url containing movie poster image
    :param trailer_youtube_url: url to youtube vidoe of movie trailer
    """
    def __init__(self, movie_title, poster_image_url,
                 trailer_youtube_url):

        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
