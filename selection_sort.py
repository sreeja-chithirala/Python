#selection sort
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
for i in range(0,n):
    min=num[i]
    k=i
    for j in range(i+1,n):     #in every iteration the smallest element in placed in its position first
        if min>num[j] :
            min=num[j]
            k=j
    temp=num[k]
    num[k]=num[i]
    num[i]=temp
print("The sorted order is: ",end=' ')
for i in range(0,n):
    print(num[i],end=' ') 
    
    
'''
Enter no of elements: 7
Enter: 30
Enter: 52
Enter: 10
Enter: -7
Enter: 40
Enter: 3
Enter: 22
The sorted order is:  -7 3 10 22 30 40 52 
'''
