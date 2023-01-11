#recursive function to find the factorial of a number
def factorial_of(num):
    if num==1 or num==0 :
        return 1
    else :
        return (num*(factorial_of(num-1)))

#main
num=int(input("Enter a number to find its factorial."))
print("factorial of ",num," is ",factorial_of(num))

'''
Enter a number to find its factorial.8
factorial of  8  is  40320
'''
