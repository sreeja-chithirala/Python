list=[1,4,6,3,4,7,4,3,4,7,8,3,7,7,9,7,10]    #the list
c=0
num=int(input("Enter the value to be searched: "))
if num in list:
    print(num," is present at the indices ",end=' ')
    for i in range(0,len(list)):     #if the list has the 'num' the we increment the count variable and print the index of it
        if num==list[i]:
            c=c+1
            print(i,end=' ')
    print()
    print("The count is ",c)
else:                               #else we print that the list does not have that element
    print(num," is not present in the list.")
    
'''
Enter the value to be searched: 7
7  is present at the indices  5 9 12 13 15 
The count is  5
'''
