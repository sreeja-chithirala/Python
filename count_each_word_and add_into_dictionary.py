str=input("Enter a string: ")
list=[]
p=""
for i in range(0,len(str)):
    if str[i]!=' ' and str[i]!='.':
        p+=str[i]    #after taking the string p stores each word and if we encounter a ' ' or '.'
    else:
        list.append(p)   #that word is appended into the list
        del p            #we delete that p and declare a new one for the next one
        p=""
print("list is ",list)
dict={}
for word in list:  #now for every word in the list
    if word not in dict:   #if it is not in the dictionary we include that
        dict[word]=len(word)   #in it with the word as key and length of it as value
print("The dictionary is ",dict)  #print the dictioanary

'''
Enter a string: My name is Sreeja Chithirala.My rollno is AP20110010321.Iam from CSE E section.
list is  ['My', 'name', 'is', 'Sreeja', 'Chithirala', 'My', 'rollno', 'is', 'AP20110010321', 'Iam', 'from', 'CSE', 'E', 'section']
The dictionary is  {'My': 2, 'name': 4, 'is': 2, 'Sreeja': 6, 'Chithirala': 10, 'rollno': 6, 'AP20110010321': 13, 'Iam': 3, 'from': 4, 'CSE': 3, 'E': 1, 'section': 7}
'''
