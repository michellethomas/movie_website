"""
Creates a movie object.

Arguments:
title - the title of the movie
storyline - a description of the movie
poster_image_url - a url of the movie poster
tailer_youtube_url - the youtube trailer url
"""
class Movie(object):
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

