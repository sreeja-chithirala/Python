#function to find the factors of a number
def factors(num):
    k=num     #we copy the num in k variable because it may be modified afterwards
    if num==1 :
        print("1 is not a prime no.")
        return      #if num is 1 we print and return
        
    list=[]
    for i in range(2,num+1,1):  
        if num % i == 0:     #we print the numbers that divide the given number completely and also add them to the list
            print(i,end=' ')
            list+='i' 
    print()
    
    if len(list)>1: #if the list contains more than 1 then it is  not considered as the prime no
        print("The number ",k," is not a prime number")
    else:
        print("The number ",k," is a prime number")
    
# main
num=int(input("Enter the number to find its factors: "))
print("The factors of the number ",num," are:1",end=' ')
factors(num)

'''
Enter the number to find its factors: 34
The factors of the number  34  are:1 2 17 34 
The number  34  is not a prime number
'''
