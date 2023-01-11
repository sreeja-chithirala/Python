list=[]
n=int(input("How many digits you want to enter: "))
print("Enter ",n," digits into the list: ")
for i in range(0,n,1):             #taking a list of numbers
    digit=int(input("Enter: "))
    list.append(digit)
print(list)
list.sort()    #sorting the list
print(list)
print("The 2nd smallest number in the list is ",list[1])  #printing the 2nd smallest
print("The 2nd largest number in the list is ",list[n-2])  #printing the 2nd largest


'''
How many digits you want to enter: 6
Enter  6  digits into the list: 
Enter: 2
Enter: 5
Enter: 12
Enter: 8
Enter: 15
Enter: 3
[2, 5, 12, 8, 15, 3]
[2, 3, 5, 8, 12, 15]
The 2nd smallest number in the list is  3
The 2nd largest number in the list is  12
'''
