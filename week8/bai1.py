class manufacturer:
    def __init__(self,identity,location):
        self.__identity = identity
        self.__location = location

    def describe(self):
        print(f'identity: {self.__identity}')
        print(f'location: {self.__location}')
        
class device(manufacturer):
    def __init__(self, name, price, identity, location):
        self.__name = name
        self.__price = price
        super().__init__(identity, location)
        self.__identity = identity
        self.__location = location
    
    def describe(self): 
        print(f'Name: {self.__name}')
        print(f'Price: {self.__price}')
        super().describe()

device1 = device("mouse", 2.5, 9725, "Vietnam")
device1.describe()