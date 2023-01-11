class polygon:  #polygon class to input lengths  
    def __init__(self,num):
        if num==1:
            self.h=int(input("Enter height: "))
            self.ba=int(input("Enter base: "))
        elif num==2:
            self.l=int(input("Enter length: "))
            self.br=int(input("Enter breadth: "))
        elif num==3:
            self.s=int(input("Enter side: "))

    
class triangle(polygon): #derived class triangle
    def __init__(self,num):
        super().__init__(num)
    def output(self):
        print("Area of triangle is ",(self.h*self.ba)/2)
        
class rectangle(polygon):  #derived class rectangle
    def __init__(self,num):
        super().__init__(num)
    def output(self):
        print("Area of rectangle is ",(self.l*self.br))
    
class square(polygon): #derived class square
    def __init__(self,num):
        super().__init__(num)
    def output(self):
        print("Area of square is ",(self.s*self.s))

n=int(input("Enter no of polygons you would like to enter: "))
for i in range(n):
    print("which polygon you would like to enter: 1. triangle  2. rectangle  3. square")
    choice=int(input("Enter no: "))
    if choice==1:
        obj=triangle(1)
        obj.output()
    elif choice==2:
        obj=rectangle(2)
        obj.output()
    elif choice==3:
        obj=square(3)
        obj.output()
        
        
 '''
 Enter no of polygons you would like to enter: 4
which polygon you would like to enter: 1. triangle  2. rectangle  3. square
Enter no: 2
Enter length: 20
Enter breadth: 10
Area of rectangle is  200
which polygon you would like to enter: 1. triangle  2. rectangle  3. square
Enter no: 1
Enter height: 30
Enter base: 15
Area of triangle is  225.0
which polygon you would like to enter: 1. triangle  2. rectangle  3. square
Enter no: 3
Enter side: 30
Area of square is  900
which polygon you would like to enter: 1. triangle  2. rectangle  3. square
Enter no: 1
Enter height: 25
Enter base: 11
Area of triangle is  137.5
'''
