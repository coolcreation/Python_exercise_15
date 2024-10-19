#  Jeff Bohn
#  10/17/2024
#  Chapter 15 - Inheritance
#  SWDV210 Python
#  main.py

#######################################################
###########  Exercise 15-2 Authors Program  ########### 
#######################################################

from objects import Book, Author, Authors

def main():
    print("\nThe Authors Tester program")
    print()
    
    author1 = Author("Mark", "Twain")
    author2 = Author("Charles", "Warner")
    authors = Authors()
    authors.add(author1)
    authors.add(author2)

    book = Book("The Gilded Age", authors)

    # display the book data
    print("BOOK DATA - SINGLE LINE")
    print(book)
    print()

    print("BOOK DATA - MUTLIPLE LINES")
    print("Title:   ", book.title)
    print("Authors: ",  book.authors)
    
    if authors.count < 2:
        print("\nAUTHOR")
    else:
        print("\nAUTHORS")
        
    for author in authors:
        print(f"{author}")
     
    print()    
    
if __name__ == "__main__":
    main()
