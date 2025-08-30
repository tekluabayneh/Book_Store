
class Books: 
    def __init__(self):
        self.books = []  



    def get_books(self): 
        return self.books

    def  store_books(self, data): 
       self.books.append(data)
    
    def delete_book(self, item): 
        self.books = list(filter(lambda x: x != item, self.books))

    def get_single(self, item): 
        return [ i for i in self.books if i == item]



BookStore = Books()

