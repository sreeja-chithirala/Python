num=input("Enter a number: ")
l=len(num)       #to know how many digits are there in the entered number 
sum=0            #initialized sum to 0
for i in range(0,l,1) :
    sum = sum + (int(num[i]))**3 #calculating the sum of cubes of digits of the entered number
if int(num) == sum :   #armstrong number is that whose value is equal to the sum of cubes of its digits
    print(num," is an armstrong number.")
else :
    print(num," is not an armstrong number")
'''
Enter a number: 456
456  is not an armstrong number
'''
