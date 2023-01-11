#function to dislay the fibonacci series
def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fib(n - 2) + fib(n - 1))


#main
n=int(input("Enter the number of terms of fibonacci series to be printed: "))
for i in range(0,n):
    print(fib(i),end=' ')

'''
Enter the number of terms of fibonacci series to be printed: 10
0 1 1 2 3 5 8 13 21 34 
'''
