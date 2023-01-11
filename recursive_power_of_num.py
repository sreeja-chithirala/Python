#recursive function to display the power of a number 
def power(base,P):
    if P == 0:
        return 1
    elif P == 1:
        return base   
    else:
        return (base*power(base, P-1)) #recursive step
    
#main
base=int(input("Enter the base: "))
P=int(input("Enter the power: "))
print(power(base, P))

'''
Enter the base: 4
Enter the power: 5
1024
'''
