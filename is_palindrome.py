#function to check whether a string is palindrome or not
def is_palindrome(st):
    opp=""
    st2=""
    for i in range(0,len(st),1):    #first the spaces in the st are removed and copied into another string st2
        if st[i]!=' ' :
            st2+=st[i]
    
    for j in range((len(st2)-1),-1,-1):   #the opposite of the st2 is found and stored in the string opp
        opp+=st2[j]
    
    if st2==opp:            #if both st2 and opp are same strings then the string st is a palindrome
        print(st," is a palindrome.")
    else :
        print(st," is not a palindrome.")
        

#main
st=input("Enter a string: ")
is_palindrome(st)

'''
Enter a string: aroma mora
aroma mora  is a palindrome.
'''
