import spacy

nlp = spacy.load('en_core_web_md')


def compare_movies(movie_to_compare: str, movie_list) -> str:

    movie_to_compare = nlp(movie_to_compare)

    best_movie = ""
    best_similarity = 0.0

    for movie in movie_list:

        similarity = nlp(movie).similarity(movie_to_compare)
        
        if similarity > best_similarity:

            best_movie = movie
            best_similarity = similarity
            
    return best_movie


movie_to_compare = (
    "Planet Hulk :" +
    "Will he save their world or destroy it? " +
    "When the Hulk becomes too dangerous for the " +
    "Earth, the Illuminati trick Hulk into a shuttle " +
    "and launch him into space to a planet where the " +
    "Hulk can live in peace. Unfortunately, Hulk lands " +
    "on the planet Sakaar where he is sold into " +
    "slavery and trained as a gladiator"
)

with open("movies.txt","r") as f:
    movies = f.readlines()

print()
print()
print(f"The recommended movie is: {compare_movies(movie_to_compare, movies).split(' :')[0]}")
print()
print()