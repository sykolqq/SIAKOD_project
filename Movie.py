class Movie:
    titleId = -1
    title = "none"
    region = "none"
    director = "none"
    rating = -1
    genres = []

    def __init__(self, title_id, title, region, director, rating, genres):
        self.titleId = title_id
        self.title = title
        self.region = region
        self.genres = genres
        self.director = director
        self.rating = rating

    def print(self):
        print(self.titleId, self.title, self.region, self.genres, self.director, self.rating)