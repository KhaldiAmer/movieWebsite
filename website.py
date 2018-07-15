from movie import Movie
import fresh_tomatoes

ant_man = Movie("Ant-man and the wasp",
	"http://cdn.collider.com/wp-content/uploads/2018/04/ant-man-and-the-wasp-poster.jpg",
	"https://www.youtube.com/watch?v=8_rTIAOohas"
	)
spider_man = Movie("Spider-Man: Into the Spider-Verse",
	"https://upload.wikimedia.org/wikipedia/en/5/5e/Spider-Man_Into_the_Spider-Verse_poster.jpeg",
	"https://youtu.be/g4Hbz2jLxvQ"
	)

hotel_transylvania = Movie("Hotel Transylvania 3: Summer Vacation",
	"https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Hotel_Transylvania_3_%282018%29_Poster.jpg/220px-Hotel_Transylvania_3_%282018%29_Poster.jpg",
	"https://www.youtube.com/watch?v=Ku52zNnft8k"
	)

movies = [ant_man, spider_man, hotel_transylvania]
fresh_tomatoes.open_movies_page(movies)
