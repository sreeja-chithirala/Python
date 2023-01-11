print("Press 0 when finished.Then I will give the sum.")
list={}
sum=0  #taking two variables sum and i and initializing them to 0
i=0
num=int(input("Enter a number: "))
list[0]=num
sum=sum+list[0]
while num != 0 :  #The loop executes continuously until the user enters 0
    i=i+1
    num=int(input("Enter a number: ")) 
    list[i]=num      #Also it copies the number entered by the user in to the list
    sum=sum+list[i]  #and calculates the sum then itself
print("Sum of the numbers entered by you is ",sum)

'''
Press 0 when finished.Then I will give the sum.
Enter a number: 23
Enter a number: 56
Enter a number: 81
Enter a number: 90
Enter a number: 66
Enter a number: 33
Enter a number: 0
Sum of the numbers entered by you is  349
'''
