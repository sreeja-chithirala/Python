#function definition to check whether a no is perfect no or not
#a num is a perfect number if the sum of its proper divisors is equal to the num itself
def perfect_no(n):
    sum = 0
    for i in range(1,n):  #the proper factors are added to the sum in this loop
        if(n % i == 0):
            sum = sum + i
    if (sum == n):
        print("The number ",n," is a Perfect number.")
    else:
        print("The number ",n," is not a Perfect number.")

#main
n = int(input("Enter any number: "))
perfect_no(n)

'''
Enter any number: 42
The number  42  is not a Perfect number.
'''
