from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

@dataclass        
class Media(Product):
    format: str = ""   
    
    def getDescription(self):
        return self.format
    
@dataclass
class Book(Media):
    author:str = ""
    #format: str = ""   # add format ie..Hardcover, Paperback
    
    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author} {self.format} "

@dataclass        
class Movie(Media):
    year:int = 0
    #format: str = ""   # add format ie.. VHS, DVD
    
    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year}) {self.format} "
    
@dataclass        
class Album(Media):
    artist: str = 0
    #format: str = ""   # add format ie.. CD, DVD
    
    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.artist} {self.format} "


