num=input("Enter a number: ") #storing the entered number into 'num'
l=len(num)      #calculated the length of the entered number
p=num[0]        #stored the 1st digit in p
q=num[l-1]      #stored the last digit in q
swap=""         #this is the that stores the number after swapping of digits
for i in range(0,l,1) :  
    if i == 0 :    
        swap+=q     #copied the last digit of 'num' as the first digit of the 'swap'
    elif i == l-1 :  
        swap+=p     #copied the first digit of 'num' as the last digit of the 'swap'
    else :
        swap+=num[i]  #for the other digits,copied the same digits of 'num' into 'swap'
print("After swapping the first and last digits the number is ",swap) #printing the number after swapping of digits

'''
Enter a number: 45636535
After swapping the first and last digits the number is  55636534
'''
