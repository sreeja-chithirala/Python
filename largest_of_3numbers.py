print("Enter 3 numbers to find the largest among them")
n1=int(input("1st number= "))      #taking three numbers from the user
n2=int(input("2nd number= "))
n3=int(input("3rd number= "))
if n1>n2 :                         #first num is compared with the second one 
    if n1>n3 :          #first num is again compared with third one 
        print(n1," is the largest")
    else :
        print(n3," is the largest")
else :
    if n2>n3 :
        print(n2," is the largest")
    else :
        print(n3," is the largest")
 
'''
Enter 3 numbers to find the largest among them
1st number= -18
2nd number= 20
3rd number= 11
20  is the largest
'''

