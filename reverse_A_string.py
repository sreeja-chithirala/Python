str1=input("Enter a string: ")
str2=""
for i in range(len(str1)-1,-1,-1):  #in the reverese order all the characters in the str1 are copied to str2
    str2+=str1[i]
print("After reversing,the string is ",str2)
del str1  #then we delete str1.

'''
Enter a string: chithirala sreeja
After reversing,the string is  ajeers alarihtihc
'''
