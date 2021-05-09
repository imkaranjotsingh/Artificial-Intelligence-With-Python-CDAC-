class Shape:
    def __init__(self,n):
        self.n = n
        self.sides = [0 for i in range(n)]
    def inputSides(self):
        for i in range(self.n):
            n = float(input("Enter Sides "+str(i+1)+":"))
            self.sides[i] = n
    def showSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

s = Shape(2)
s.inputSides()
s.showSides()

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self,2)
    def area(self):
        l,b = self.sides
        a = l * b
        print("Area is:",a)
r = Rectangle()
r.inputSides()
r.showSides()
r.area()

class Square(Shape):
    def __init__(self):
        #super.__init__(self,1)
        Shape.__init__(self,1)
    def area(self):
        s = self.sides
        a = s[0]*s[0]
        print("Area is:",a)
s = Square()
s.inputSides()
s.showSides()
s.area()

print(issubclass(Square,Shape))
print(isinstance(r,Square))
    
