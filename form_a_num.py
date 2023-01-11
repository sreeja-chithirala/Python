list=[]  #declaring the list
num=0
n=int(input("How many digits you want to enter: "))
print("Enter ",n," digits into the list: ")
for i in range(0,n):      
    digit=int(input("Enter: "))    #taking n digits into the list
    list.append(digit)    
print(list)
for i in range(0,len(list)):         #now,for every digit in the list
    d=list[i]
    num=(num*10)+d            #we add it to num*10
print(num)

'''
How many digits you want to enter: 6
Enter  6  digits into the list: 
Enter: 4
Enter: 2
Enter: 6
Enter: 1
Enter: 9
Enter: 3
[4, 2, 6, 1, 9, 3]
426193
'''
