n=int(input("Enter the no of rows to get the pattern: "))
for i in range(1,n+1,1) :        #starting 'i'th line
    for j in range(1,n+1,1) :      #In 'i'th line for one value of 'j' we will print 0 or 1
        if i%2 == 0 :            #if the line no is even 
            if j%2 == 0 :     
                print("1 ",end='')  #if it is an even position we will print 1
            else :
                print("0 ",end='')  #else we will print 0
        else :                  #else if the line no is odd  
            if j%2 == 0 :
                print("0 ",end='')  #if it is an even position we will print 0
            else :
                print("1 ",end='')  #else we will print 1
    print()          #go to the next line
    
 '''
 Enter the no of rows to get the pattern: 7
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 
1 0 1 0 1 0 1 
'''
