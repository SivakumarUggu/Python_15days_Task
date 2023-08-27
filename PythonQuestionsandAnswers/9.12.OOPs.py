#10. Create a class to represent a movie with attributes like title, director and rating.
class Movie:
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.rating=rating

    def display_info(self):
        return self.title, self.director, self.rating


movie1=Movie('OMG','Pruthvi','4/5')
movie2=Movie('Rocky','OM','4.5/5')

print(movie1.display_info())
print(movie2.display_info())