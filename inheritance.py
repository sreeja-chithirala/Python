class rectangle:     #parent class rectangle has attributes length and breadth
    def __init__(self):
        self.length=int(input("Enter the length of rectangle: "))
        self.breadth=int(input("Enter the breadth of rectangle: "))

class colour_rectangle(rectangle):   #child class colour_rectangle has attributes colour and area also inherits rectangle calss
    def __init__(self):
        super().__init__()
        self.col=input("Enter the colour of rectangle: ")
        self.area=(self.length)*(self.breadth)
        print("Area is: ",self.area)
        
n=int(input("Enter no of rectangles you would like to enter: "))
l=[]
for i in range(n):  
    obj=colour_rectangle()
    l.append(obj)   #appending each colour_rectangle object into the list l
    
min_area=l[0].area
obj=l[0]
for i in range(1,n): #finding the object that has minimum area
    if l[i].area<min_area:
        min_area=l[i].area
        obj=l[i]
        
print()
print(obj.col," colour rectangle has minimum area")   #printing the colour of the minimum area's object

'''
Enter no of rectangles you would like to enter: 4
Enter the length of rectangle: 30
Enter the breadth of rectangle: 10
Enter the colour of rectangle: red
Area is:  300
Enter the length of rectangle: 20
Enter the breadth of rectangle: 5
Enter the colour of rectangle: blue
Area is:  100
Enter the length of rectangle: 40
Enter the breadth of rectangle: 10
Enter the colour of rectangle: green
Area is:  400
Enter the length of rectangle: 30
Enter the breadth of rectangle: 15
Enter the colour of rectangle: yellow
Area is:  450

blue  colour rectangle has minimum area
'''
