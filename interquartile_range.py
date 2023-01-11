cse=[67 , 88 , 82 , 89 , 90 , 73 , 83 , 84 , 73 , 85 , 77 , 85 , 78 , 79 , 96 , 84 , 98 , 87 , 72 , 80 , 81 , 84 , 84 , 73 
         , 99 , 85 , 86 , 74 , 86 , 90 , 73 , 91 , 77 , 93 , 79 , 95 , 54 , 62 , 70 , 84]

for i in range(1,len(cse)) :  #first we will sort the list using insertion sort method
    p=cse[i]                  #we will start from the 2nd element whose index value is 1
    j=i-1
    while j>=0 and cse[j]>=cse[j+1] :   #for an element at ith or (j+1)th index we will interchange it with elements 
        cse[j+1] = cse[j]               #towards its left(or sorted elements) repeatedly until it reaches a position 
        j = j-1                         #where the element towards its left is less than this value.
        cse[j+1] = p
print("The new list after sorting is ",cse)  #print the sorted list

k=len(cse)//2
if len(cse)%2 == 0 :                      #if the lenght of the list is even then there will be two middle elements
    median = (cse[k - 1] + cse[k])/2          #thus median will be the average of these two elements
else :
    median = cse[(len(cse)//2)]           #if the length is odd then there will be only one middle element
print("Median of the following data is ",median)   


if k%2 == 0 :                      #the first quartile is the median of the first half of the elements.
    l1=k//2
    firstQ = (cse[l1-1]+cse[l1])/2
else :
    firstQ = cse[k//2]
print("The 1st quartile of the list is ",firstQ)


if k%2 == 0 :                            #the third quartile is the median of second half of the elements
    l2 = k + k//2
    thirdQ = (cse[l2-1]+cse[l2])/2
else :
    thirdQ = cse[k + k//2]
print("The 3rd quartile of the list is ",thirdQ)


min=cse[0]        #min is the first element of the sorted list
max=cse[len(cse)-1]       #max is the last element of the sorted list
print("The max element in the list is ",max," and the min element in the list is ",min)
IQR = thirdQ-firstQ
print("The interquartile range for the list is ",IQR)

'''
The new list after sorting is  [54, 62, 67, 70, 72, 73, 73, 73, 73, 74, 77, 77, 78, 79, 79, 80, 81, 82, 83, 84, 84, 84, 84, 84, 85, 85, 85, 86, 86, 87, 88, 89, 90, 90, 91, 93, 95, 96, 98, 99]
Median of the following data is  84.0
The 1st quartile of the list is  75.5
The 3rd quartile of the list is  87.5
The max element in the list is  99  and the min element in the list is  54
The interquartile range for the list is  12.0
'''
