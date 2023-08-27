#2. Create a class to represent a book with attributes like title, author and publication year.
class book:
    def __init__(self, title, author, pubyear):
        self.title=title
        self.author=author
        self.pubyear=pubyear



book1=book('Tipping Point', 'MG', 2016)
print(book1.title)
print(book1.author)
print(book1.pubyear)
print(book1.__dict__)
#print(help(book1))

