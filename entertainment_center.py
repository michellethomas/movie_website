"""
Creates a list of favorite movies as movie objects.

Creates instances of the movie class and sends a movie list to fresh_tomatoes.py
 script to create the movies page.
"""

import fresh_tomatoes
import media

essm = media.Movie("Eternal Sunshine of the Spotless Mind",
      "A film about an estranged couple who have each other erased from their" \
        " memories",
      "http://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_" \
        "spotless_mind_ver3.jpg",
      "https://www.youtube.com/watch?v=yE-f1alkq9I")

amelie = media.Movie("Amelie",
				"It tells the story of a shy waitress who decides to change the lives" \
          " of those around her for the better.",
				"http://ia.media-imdb.com/images/M/MV5BMTYzNjkxMTczOF5BMl5BanBnXkFtZ" \
          "TgwODg5NDc2MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
				"https://www.youtube.com/watch?v=B-uxeZaM-VM")

tenenbaums = media.Movie("The Royal Tenenbaums",
					"It follows the lives of three gifted siblings who experience great" \
            " success in youth, and even greater disappointment and failure " \
            "after their eccentric father leaves them in their adolescent " \
            "years.",
					"http://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",
					"https://www.youtube.com/watch?v=8Eg6yIwP2vs")

godfather = media.Movie("The Godfather",
					"Traces the problems of Michael Corleone in 1958 and a young" \
            " immigrant Vito Corleone in 1917's Hell's Kitchen.",
					"http://upload.wikimedia.org/wikipedia/en/0/03/Godfather_part_ii.jpg",
					"https://www.youtube.com/watch?v=qJr92K_hKl0")

movie_list = [essm, amelie, tenenbaums, godfather]
fresh_tomatoes.open_movies_page(movie_list)
