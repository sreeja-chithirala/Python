#recursive function to find the number of digits
def count(num) :
    if num/10 == 0:
        return 0
    else :
        return (1 + count(num//10))  

#main
num=int(input("Enter the number to know the number of digits in it: "))
print("The number of digits in the given number is ",count(num))

'''
Enter the number to know the number of digits in it: 234554
The number of digits in the given number is  6
'''
