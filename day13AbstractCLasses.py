from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass


class MyBook(Book):
    # Write your constructor here
    def __init__(self, title, author, price):
        self.title =title
        self.author =author
        self.price = price

    # Write your function here
    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))




title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

