print("Let the quadratic equation be ax^2+bx+c")
print("Give the values for a,b,c: ");
a=int(input("a= "))    #taking the coefficients of the quadratic equation
b=int(input("b= "))
c=int(input("c= "))
dis=b**2-4*a*c    #calculating the discriminent
if dis==0 :   #based on the discriminent the roots are displaced
    print("The quadratic equation ",a,"x^2+","(",b,"x",")","+",c ," has real and equal roots")
    print("and the roots are ", -b/(2*a) , "," , -b/(2*a))
elif dis>0 :
    x1=(-b+(dis)**0.5)/(2*a)
    x2=(-b-(dis)**0.5)/(2*a)
    print("The quadratic equation ",a,"x^2+","(",b,"x",")","+",c ," has real and distinct roots")
    print("and the roots are ",x1,",",x2)
else :
    print("The quadratic equation ",a,"x^2+","(",b,"x",")","+",c ," has imaginary roots")

'''
Let the quadratic equation be ax^2+bx+c
Give the values for a,b,c: 
a= 8
b= 5
c= 1
The quadratic equation  8 x^2+ ( 5 x ) + 1  has imaginary roots
'''
