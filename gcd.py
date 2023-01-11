print("Enter two numbers to get their GCD")  #GCD is the highest common factor that can divide bothe the numbers
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
while n1 != 0  and  n2 != 0  :    #We will execute the loop until one of them becomes 0
    if n1 > n2 :                 #GCD of two numbers does not change even if we divide the smallest from the largest
        n1=n1-n2                
    else :
        n2=n2-n1
if n1 == 0 :                     ##When one of the numbers become 0 the other becomes the GCD.
    print(n2," is the GCD of the two numbers")
else :
    print(n1," is the GCD of the two numbers")
'''
Enter two numbers to get their GCD
Enter n1: 32
Enter n2: 90
2  is the GCD of the two numbers
'''
