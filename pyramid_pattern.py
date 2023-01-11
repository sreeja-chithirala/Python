n = int(input("Enter the number of rows: "))    
for i in range(1, n+1):      #Loop to print pattern above the middle line
    for j in range(1, i + 1):  #this loop is for printing the stars
        print("* ",end='')       
    print() #to go to next line
    
for i in range(1,n+2):   #loop to print middle line stars
    print("* ",end='')
print()
        
for i in range(n + 2, 1, -1):  #Loop to print pattern below the middle line  
    for j in range(1, i - 1):     #this loop is for printing the stars
        print("* ",end='')  
    print()  
    
'''
Enter the number of rows: 5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
