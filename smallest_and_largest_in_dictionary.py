n=int(input("How many elements you want to enter into the dictionary: "))
dict={}
list=[]
for i in range(1,n+1):        #taking the dictionary from the user
    key=int(input("Enter key: "))
    value=int(input("Enter value: "))
    dict[key]=value
    list.append(value)       #only the values are appended to the list
print("The dictionary is ",dict)
list.sort()                  #the list is then sorted
print("The smallest value of the dictionary is ",list[0])    #smallest and largest from the list are printed
print("The largest value of the dictionary is ",list[len(list)-1])

'''
How many elements you want to enter into the dictionary: 5
Enter key: 2
Enter value: 50
Enter key: 4
Enter value: 100
Enter key: 3
Enter value: 70
Enter key: 5
Enter value: 10
Enter key: 6
Enter value: 120
The dictionary is  {2: 50, 4: 100, 3: 70, 5: 10, 6: 120}
The smallest value of the dictionary is  10
The largest value of the dictionary is  120
'''
