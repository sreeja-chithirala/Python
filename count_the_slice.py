string=input("Enter the string: ")  #takes the string
sl=input("Enter the slice to be found: ")#takes the slice to be searched
c=0
for i in range(0,len(string)-len(sl)+1): #we will check every slice with length as 'sl' in the string and compare it with sl 
    if string[i:i+len(sl)]==sl: #if they are same we increment the 'c' variable.
        c=c+1
print("The count of ",sl," is ",c)

'''
Enter the string: azcbobobegghakl
Enter the slice to be found: bob
The count of  bob  is  2
'''
