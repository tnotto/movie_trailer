import media
import fresh_tomatoes


def build_movie_instances():
    #Build all Movie instances here: title, description, poster img, youtube lnk
    #Looks long, but basically media.Movie(TITLE, DESCRIPTION, COVER_IMAGE,
    #YOUTUBE_TRAILER) repeated 6 times
    print 'adding its a wonderful life'
    IAWL = media.Movie("It's a Wonderful Life",
                       ("An angel helps a compassionate but despairingly frustrated"
                        " businessman by showing what life would have been like if "
                        "he never existed."),
                       "https://upload.wikimedia.org/wikipedia/en/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=LJfZaT8ncYk")

    print 'adding dark corner'
    TDC = media.Movie("The Dark Corner",
                      ("Secretary tries to help her boss, who is framed for a "
                       "murder."),
                      "https://upload.wikimedia.org/wikipedia/en/d/dd/Dark_Corner_1946.JPG",  # NOQA
                      "https://www.youtube.com/watch?v=_HZS1dEhrx0")

    print 'adding blue skies'
    BS = media.Movie("Blue Skies",
                     ("Jed Potter looks back on a love triangle conducted over the "
                      "course of years and between musical numbers. Dancer Jed "
                      "loves showgirl Mary, who loves compulsive nightclub-opener "
                      "Johnny, who can't stay committed to anything in life for "
                      "very long."),
                     "https://upload.wikimedia.org/wikipedia/en/f/fe/Blue_skiesmp.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=kEc16BjfrvI")

    print 'adding the stranger'
    TS = media.Movie("The Stranger",
                     ("An investigator from the War Crimes Commission travels to "
                      "Connecticut to find an infamous Nazi."),
                     "https://upload.wikimedia.org/wikipedia/en/d/dc/The_Stranger_%28film%29.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=G4cxvrXTOc8")

    print 'adding Notorious'
    NO = media.Movie("Notorious",
                     ("A woman is asked to spy on a group of Nazi friends in South "
                      "America. How far will she have to go to ingratiate herself "
                      "with them?"),
                     "https://upload.wikimedia.org/wikipedia/en/6/63/Notorious_1946.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=H8f4UOtLf5Q")

    print 'adding the big sleep'
    TBS = media.Movie("The Big Sleep",
                      ("Private detective Philip Marlowe is hired by a rich family."
                       " Before the complex case is over, he's seen murder, "
                       "blackmail, and what might be love."),
                      "https://upload.wikimedia.org/wikipedia/en/d/d3/Bigsleep2.JPG",  # NOQA
                      "https://www.youtube.com/watch?v=VjJlBnfyiI4")

    movies = [IAWL, TDC, BS, TS, NO, TBS]

    return movies


def build_html(movies):
    # uses fresh_tomatoes to build html code
    print 'building html'
    fresh_tomatoes.open_movies_page(movies)


def main():
    movies = build_movie_instances()
    build_html(movies)

if __name__ == '__main__':
    main()
