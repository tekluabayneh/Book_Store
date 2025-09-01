import requests

url = "https://openlibrary.org/search.json?q=python"
from books.book import BookStore




res = requests.get(url)
data = res.json()


for book in data["docs"]: 
  title = book.get("title", "No title") 
  author   = book.get("author_name", ["Knowen"])
  year = book.get("first_publish_year", "Not found")
  data = (title, author, year)
  BookStore.store_books(data)

# print(data)

#
# print(BookStore.get_books())
# print("this is the filter data single data", BookStore.delete_book('data5'))
# print("this is deltting file man", BookStore.delete_book('data3'))
print(BookStore.get_books())
print(BookStore.search_book("python"))

