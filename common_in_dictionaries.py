d1 = {'a': 10, 'b': 20, 'c':30, 'd':40, 'e':50, 'f':60}    #we have two dictionaries
d2 = {'a': 20, 'b': 30, 'd':40, 'f':10}
list1=['a','b','c','d','e','f']       #the keys are taken in to the lists
list2=['a','b','d','f']
d3={}                       #new dictionary
for i in range(0,len(list1)):    
    if list1[i] in d2:     #if we find the same keys in both the list we add its values 
        d3[list1[i]]= d1[list1[i]]+d2[list1[i]]     #and add them in to the new dictionary
    else:
        d3[list1[i]]= d1[list1[i]]
print(d3)      #after both lists are completed the dictionary is printed

'''
{'a': 30, 'b': 50, 'c': 30, 'd': 80, 'e': 50, 'f': 70}
'''
