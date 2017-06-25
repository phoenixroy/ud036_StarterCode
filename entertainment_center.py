import fresh_tomatoes
import media

""" create a list of some movies and pass this 
	list to be rendered on a webpage """

bhaag_milkha_bhaag = media.Movie("Bhaag Milkha Bhaag",
                                """The truth behind the ascension of Milkha 
                                'The Flying Sikh' Singh who was scarred 
                                because of the India-Pakistan partition.""",
                                "https://upload.wikimedia.org/wikipedia/"
                                "en/4/42/Bhaag_Milkha_Bhaag_poster.jpg",
                                "https://youtu.be/3uICXnnW86U")

dangal = media.Movie(	"Dangal",
                        """Former wrestler Mahavir Singh Phogat and his two 
                        wrestler daughters struggle towards glory at the 
                        Commonwealth Games in the face of societal 
                        oppression.""",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/9/99/Dangal_Poster.jpg",
                        "https://youtu.be/x_7YlGv9u1g")

pink = media.Movie (	"Pink",
                    	"""When three young women are implicated in a 
                    	crime, a retired lawyer steps forward to help 
                    	them clear their names.""",
                    	"https://upload.wikimedia.org/"
                    	"wikipedia/en/a/ae/Pinkmovieposter.jpg",
                    	"https://youtu.be/AL2TShb6fFs")
                    	
three_idiots = media.Movie("3 Idiots",
                        """Two friends are searching for their long lost 
                        companion. They revisit their college days and recall 
                        the memories of their friend who inspired them to 
                        think differently, even as the rest of the world 
                        called them 'idiots'.""",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/d/df/3_idiots_poster.jpg",
                        "https://youtu.be/xvszmNXdM4w")


chak_de_india = media.Movie("Chak De! India",
                    		"""Kabir Khan is the coach of the Indian Women's 
                    		National Hockey Team and his dream is to 
                    		make his all girls team emerge victorious 
                    		against all odds.""",
                    		"https://upload.wikimedia.org/"
                    		"wikipedia/en/0/0c/Chak_De%21_India.jpg",
                    		"https://youtu.be/6a0-dSMWm5g")

lagaan = media.Movie(	"Lagaan: Once Upon a Time in India",
                        """The people of a small village in Victorian India 
                        stake their future on a game of cricket against 
                        their ruthless British rulers.""",
                        "https://upload.wikimedia.org/wikipedia/"
                        "en/b/b6/Lagaan.jpg",
                        "https://youtu.be/oSIGQ0YkFxs")

zindagi_na_milegi_dobara = media.Movie(	"Zindagi Na Milegi Dobara",
                                       	"""Three friends decide to turn 
                                       	their fantasy vacation into reality 
                                       	after one of their number becomes 
                                       	engaged.""",
                                       	"https://upload.wikimedia.org/"
                                       	"wikipedia/en/3/3d/"
                                       	"Zindaginamilegidobara.jpg",
                                       	"https://youtu.be/ifIBOKCfjVs")


# create a list of all movies
movies = [bhaag_milkha_bhaag, dangal, pink, three_idiots,
          chak_de_india, lagaan, zindagi_na_milegi_dobara]

# pass movie list to fresh_tomatoes.py to render as a webpage
fresh_tomatoes.open_movies_page(movies)