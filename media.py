import webbrowser


class Movie():
    """This class stores information about a movie"""

    # init this class with 4 arguments:
    # movie title, poster image, youtube trailer, and story line
    def __init__(self, movie_title, story_line, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.story_line = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    # make a class method to show a trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)