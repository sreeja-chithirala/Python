#bubble sort
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
for i in range(0,n):  
    for j in range(0,n-i-1):
        if num[j]>num[j+1] :   #adjacent elements are compared repetatively 
            temp=num[j]                  #in every iteration largest element is placed in its position first
            num[j]=num[j+1]
            num[j+1]=temp
print("The sorted order is: ",end=' ')
for i in range(0,n):
    print(num[i],end=' ')
    
'''
Enter no of elements: 7
Enter: -8
Enter: 10
Enter: -2
Enter: 38
Enter: 0
Enter: 56
Enter: 77
The sorted order is:  -8 -2 0 10 38 56 77 
'''
