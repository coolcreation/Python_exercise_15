#  Jeff Bohn
#  10/18/2024
#  Chapter 15 - Inheritance
#  SWDV210 Python
#  main.py

######################################################
###########  Exercise 15-1 Prodcut Viewer  ########### 
######################################################

from objects import Product, Media, Book, Movie, Album

def validate(count, products):
    # print("count value: ", count)
    while True:
        try:
            count = int(count)  # try to convert
            if 1 <= count and count <= len(products):
                return products[count - 1]
            else:
                print(f"Please enter a number between 1 and {len(products)}")
                count = input("Enter product number: ") 
        except ValueError:
            print(f"Please enter a number between 1 and {len(products)}")
            count = input("Enter product number: ")  
            

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()

def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")

    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
        # print(f"{'Format:':{w}}{product.format}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
        # print(f"{'Format:':{w}}{product.format}")
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
        # print(f"{'Format:':{w}}{product.format}")
    if isinstance(product, Media):   # media takes care of all format types
        print(f"{'Format:':{w}}{product.format}")
        
    print(f"{'Discount price:':{w}}${product.getDiscountPrice():.2f}")
    print()

def main():
    
    print("\nThe Product Viewer program\n")
    
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Hardcover", "Michael Lewis"),
                Book("Python 2nd Edition", 54.95, 12, "Paperback", "Joel Murach"),
                Movie("The Holy Grail", 14.99, 68, "DVD", 1975),
                Movie("Rambo", 21.99, 54, "VHS", 1987),
                Album("Rubber Soul", 20.00, 50, "CD", "The Beatles"),
                Album("Houses of the Holy", 19.99, 33, "Vinyl", "Led Zepplin"))
    
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        
        num = validate(input("Enter product number: "), products)
        print()
        show_product(num)
            
        choice = input("View another product? (y/n): ")
        print()

    print("Bye!\n")

if __name__ == "__main__":
    main()
