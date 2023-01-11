list=[]              #declaring the list
num=int(input("Enter a number: "))  #taking the num from user
while num!=0:        #until num!=0 we will take each digit of it by using % 
    d=num%10
    list.append(d)   #the append it into the list
    num=num//10      #then removing the digit from the number by dividing num with 10
list.reverse()       #to get the correct order we reverse the list
print("The list is ",list)     #print the list

'''
Enter a number: 3457281
The list is  [3, 4, 5, 7, 2, 8, 1]
'''
