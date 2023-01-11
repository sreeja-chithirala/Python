#merge sort
def mergesort(num,s,e):   #dividing the array into two parts
    if(e-s>1):
        m=(s+e)//2
        mergesort(num,s,m)
        mergesort(num,m,e)
        merge(num,s,m,e)

def merge(num,s,m,e):   #combining two arrays
    left=num[s:m]
    right=num[m:e]
    k=s
    i=0
    j=0
    while(s+i<m  and  m+j<e):
        if(left[i]<=right[j]):
            num[k]=left[i]
            i=i+1
        else:
            num[k]=right[j]
            j=j+1
        k=k+1
    if(s+i<m):
        while(k<e):
            num[k]=left[i]
            i=i+1
            k=k+1
    else:
        while(k<e):
            num[k]=right[j]
            j=j+1
            k=k+1

            
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
mergesort(num,0,n)
print("The sorted order is: ",end=' ')
for i in range(0,n):
    print(num[i],end=' ') 
    
    
'''
Enter no of elements: 7
Enter: 12
Enter: 90
Enter: 34
Enter: -4
Enter: 77
Enter: 36
Enter: 0
The sorted order is:  -4 0 12 34 36 77 90 
'''
