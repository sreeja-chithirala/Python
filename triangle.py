A1=int(input("1st angle:"))   #taking the three angles from the user
A2=int(input("2nd angle:"))
A3=int(input("3rd angle:"))
sum=A1+A2+A3
if sum==180 :         #for a triangle to be valid the sum of its three angles should be 180
    print("The three angles you entered can form a triangle")
else :
    print("The three angles you entered cannot form a valid triangle")
    if sum<180 :
        print("The sum of the angles is ",sum,".So the sum should be increased by ",180-sum," for the triangle to be valid")
        print("The angles can therefore be",A1+(180-sum)/3,",",A2+(180-sum)/3,",",A3+(180-sum)/3)
    else :
        print("The sum of the angles is ",sum,".So the sum should be decreased by ",sum-180," for the triangle to be valid")
        print("The angles can therefore be",A1-(sum-180)/3,",",A2-(sum-180)/3,",",A3-(sum-180)/3)
'''
1st angle:50
2nd angle:90
3rd angle:60
The three angles you entered cannot form a valid triangle
The sum of the angles is  200 .So the sum should be decreased by  20  for the triangle to be valid
The angles can therefore be 43.333333333333336 , 83.33333333333333 , 53.333333333333336
'''
