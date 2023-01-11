#tower of hanoi recursive function
def TOH(n,source,temp,dest):
    if n>0 :
        TOH(n-1,source,dest,temp)
        print("Move disk ",n,"from ",source,"->",dest)
        TOH(n-1,temp,source,dest)

#main
n=int(input("Enter the no of disks: "))
print("The sequence is:")
source="S"
temp="T"
dest="D"
TOH(n,source,temp,dest)

'''
Enter the no of disks: 3
The sequence is:
Move disk  1 from  S -> D
Move disk  2 from  S -> T
Move disk  1 from  D -> T
Move disk  3 from  S -> D
Move disk  1 from  T -> S
Move disk  2 from  T -> D
Move disk  1 from  S -> D
'''
