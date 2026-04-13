class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"

comedy_instance = Comedy()
result_comedy = comedy_instance.add_movie('Эйс Винтура')
print(result_comedy)

drama_instance = Drama()
result_drama = drama_instance.add_movie('Вечное сияние чистого разума')
print(result_drama)