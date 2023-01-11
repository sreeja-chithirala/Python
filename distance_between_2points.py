x1=int(input("Enter the x coordinate of the first point: ")) #taking the coordinates from the user
y1=int(input("Enter the y coordinate of the first point: "))
x2=int(input("Enter the x coordinate of the second point: "))
y2=int(input("Enter the y coordinate of the second point: "))
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5  #distance between two points
print("distance between two points with coordinates")
print("(",x1,",",y1,")  and  (",x2,",",y2,")  is  ",distance)

'''
Enter the x coordinate of the first point: 8
Enter the y coordinate of the first point: 5
Enter the x coordinate of the second point: 3
Enter the y coordinate of the second point: 1
distance between two points with coordinates
( 8 , 5 )  and  ( 3 , 1 )  is   6.4031242374328485
'''
