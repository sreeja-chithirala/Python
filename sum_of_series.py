print("Let us print the sum of the series 1/2 + 1/3 + 1/4....1/n")
n=int(input("Enter the value for n: "))
sum=0  #first initializing the sum to 0
for i in range(2,n+1,1):
    sum=sum+(1/i)    #Adding i/i at every iteration
print("The sum of series is",round(sum,3))

'''
Let us print the sum of the series 1/2 + 1/3 + 1/4....1/n
Enter the value for n: 7
The sum of series is 1.593
'''
