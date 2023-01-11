list=[1,4,6,3,4,7,4,3,4,7,8,3,7,7,9,7,10]   #the list
new_list=[]
for i in range(0,len(list)):
    if list[i] in new_list:     #if a number is present in the new_list we check the next number
        continue
    else:                       #else add that into the new list
        new_list.append(list[i])
print(new_list)
del list

'''
[1, 4, 6, 3, 7, 8, 9, 10]
'''
