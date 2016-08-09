class Movie():
    # Movie contains basic, static information about movies
    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer):
        #Instantiates a Movie instance with variables title, storyline,
        #poster_image_url, and trailer_youtube_url
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
