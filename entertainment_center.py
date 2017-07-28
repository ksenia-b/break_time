import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an planet",
                     "https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D0%B0%D1%82%D0%B0%D1%80_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2009)#/media/File:Avatar-2009.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

zootopia = media.Movie("Zootopoa",
                       "Some motivetion movie",
                       "https://en.wikipedia.org/wiki/Zootopia#/media/File:Zootopia.jpg",
                       "https://www.youtube.com/watch?v=VCDQRy1od30")
#print(zootopia.show_trailer())

school_of_rock = media.Movie("School of rock",
                             "School movie rock",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=oP7kExN8LFA")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Romantic story",
                                "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%87%D1%8C_%D0%B2_%D0%9F%D0%B0%D1%80%D0%B8%D0%B6%D0%B5#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

toy_story2 = media.Movie("Toy Story2",
                        "A story of a boy and his toys2",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",     
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
movies = [toy_story, avatar, zootopia, school_of_rock, midnight_in_paris, toy_story2]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)