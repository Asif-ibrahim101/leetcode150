#define class and object
class Trader:
    #constractor
    def __init__(self, name:str):
        self.name = name
    
    #method
    def greet(self)-> str:
        return f"Trader: {self.name}"
    

t = Trader("Asif")
print(t.greet())