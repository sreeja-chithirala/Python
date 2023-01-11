
def bin_search(num,s,e,search):  #recursive binary search function
    if(s<=e):
        m=(s+e)//2
        if(int(num[m])<search):   #to search in the right part
            return bin_search(num,m+1,e,search)
        elif(int(num[m])>search): #to search in the left part
            return bin_search(num,s,m-1,search)
        else:                     #if found return 1
            return 1
    else:                         #else return 0
        return 0

#main    
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
search=int(input("Enter the element to be searched: "))
t=bin_search(num,0,n-1,search)
if(t):
    print("Element ",search," is found")
else:
    print("Element ",search," is not found")
    

'''
Enter no of elements: 7
Enter: 4
Enter: 14
Enter: 26
Enter: 38
Enter: 47
Enter: 68
Enter: 90
Enter the element to be searched: 68
Element  68  is found
'''
