# Your Python code goes here
# excercise 6 solution
class Library:
    def __init__(self) -> None:
        self.noBooks=0
        self.books=[]
        
    def addBooks(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
        
    def info(self):
        print(f" The library has {self.noBooks} books and books are ")
        for book in self.books:
            print(book)
        
l1=Library()
l1.addBooks("Harry Potters1")
l1.addBooks("Harry Potters2")
l1.addBooks("Harry Potters3")
l1.info()