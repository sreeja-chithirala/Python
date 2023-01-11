#function to print the sum of odd numbers from 1 to n
def sum_n_odd(n):
    sum=0
    for i in range(1,n+1,2): #sum of the odd numbers is added in the loop
        sum=sum+i
    print("The sum of the odd numbers from 1 to ",n," is ",sum)

#main
n=int(input("Enter the value of n: "))
sum_n_odd(n)

'''
Enter the value of n: 15
The sum of the odd numbers from 1 to  15  is  64
'''
