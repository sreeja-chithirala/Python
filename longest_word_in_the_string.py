str=input("Enter a string: ")
c=0
s=0
for i in range(0,len(str)):  #calculating no of vowels and spaces
    if str[i]=='a' or str[i]=='e'or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U':
        c=c+1
    if str[i]==' ':
        s=s+1
print("No of vowels in the given string is ",c)
print("No of spaces in the given string is ",s)

list1=[]
list2=[]
p=""
for i in range(0,len(str)):
    if str[i]!=' ' and str[i]!='.':
        p+=str[i]
    else:
        list1.append(p)   #each word in the string is appended into the list1 at index i
        list2.append(len(p))  #the lenght of that word is appended into the list2 at i only
        del p
        p=""
m=max(list2)   #we find max length in list2
for j in range(0,len(list2)):
    if m==list2[j]:  #now the index where that max is present is known 'j'
        break
print("The longest word in the string is ",list1[j]) #the element at 'j'th index is printed


'''
Enter a string: My name is Sreeja Chithirala.Iam from CSE E.
No of vowels in the given string is  15
No of spaces in the given string is  7
The longest word in the string is  Chithirala
'''
