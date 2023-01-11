#insertion sort
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
for i in range(1,n):
    temp=num[i]
    for j in range(i-1,-1,-1):   #an element in the unsorted part is taken and placed in its position in the sorted part
        if temp<num[j] :
            num[j+1]=num[j]
        else:
            break
    num[j+1]=temp
print("The sorted order is: ",end=' ')
for i in range(0,n):
    print(num[i],end=' ')   
    
'''
Enter no of elements: 7
Enter: -3
Enter: 20
Enter: 53
Enter: 0
Enter: 12
Enter: 90
Enter: 73
The sorted order is:  -3 0 12 20 53 73 90
'''
