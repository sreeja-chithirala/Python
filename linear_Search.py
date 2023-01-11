#linear search 
n=int(input("Enter no of elements: "))
num=[]
for l in range(0,n):
    ele=int(input("Enter: "))
    num.append(ele)
search=int(input("Enter the element to be searched: "))
for i in range(0,n):   #we will check the element search with all the elements in the list
    if(num[i]==search):  #if any element matches we print found
        print("Element ",search," found")
        break
if(i==n-1): #after executing the loop if i and lenght of list are same we print not found
    print("Element ",search," not found")
    
'''
Enter no of elements: 6
Enter: 12
Enter: 34
Enter: 8
Enter: 10
Enter: 55
Enter: 72
Enter the element to be searched: 9
Element  9  not found
'''
