from ast import Num


class calculator:
    def __init__(self , num):
        self.number = num
    
    def square(self ):
        print(f"Square of the {self.number} is {self.number**2}")


    def cube(self ):
        print(f"Cube of the {self.number} is {self.number**3}")
        
    def squareroot(self ):
        print(f"Squareroot of the {self.number} is {self.number**0.2}")
        
    def addition(self ):
        print(f"Addition of the {self.number} is {self.number+10}")

f1 = calculator(2)


f1.square()
f1.cube()
f1.squareroot()
f1.addition()