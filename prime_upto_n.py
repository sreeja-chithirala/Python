num=int(input("Enter the 'num' upto which the prime no's need to be displayed: "))
for i in range(1 , num+1 , 1) :  #for loop executes from 1 to num+1
    p=0                          #every time we will consider a variable p and initialixe it to 0
    if i == 1 :  #we will increment p if 'i' is not a prime number       
        p=p+1    #here 1 is not a prime no hence p is incremented
    else :
        for j in range(2 , (i//2)+1 , 1) :   #for other i's we will divide them with j which varies from 1 to i/2 +1
            if i%j == 0 :                  #if any 'j' divides 'i' completely then 'i' cannot be a prime no 
                p=p+1                       #and hence will increment p
                break                        #break from the loop as it is not our required
    if p == 0 :           #after executing the above if-else if 'p' is still equal to 0 then it implies there is no number 
        print(i," ",end='')   #that can divide 'i' and hence it is a prime num and thus we print it
        
'''
Enter the 'num' upto which the prime no's need to be displayed: 129
2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97  101  103  107  109  113  127
'''
