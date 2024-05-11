# Your Python code goes here
#  library class 

class Books:
    def __init__(self):
        self.books=[] 

    def add_book(self,book):
        self.books.append(book)
        # self.count=0
    def info(self):
        print("Books in Library :")
        for book in self.books:
            print(book)
class NumberOfBooks(Books):
    def number(self):
        self.count=len(self.books)
        print(f"The Total number of books is {self.count}")
        
        

Library=NumberOfBooks()
Library.add_book("Atomic HAbits")
Library.add_book("Atomic HAbits")
Library.add_book("Atomic HAbits")
Library.add_book("Atomic HAbits")
Library.info() 
Library.number()
