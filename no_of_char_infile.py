f=open("python_2file.txt","r")
data=f.read()            #reads the content of the file and stores that in the form of string data
print("The data in the file is: ",data)
c=0
for i in range(0,len(data)):
    if data[i]==' ':
        i=i+1
    else :
        i=i+1
        c=c+1    #for every character the c variable gets incremented except for the space
    
print("The no of characters in the above txt file are ",c)

'''
The data in the file is:  Hi!.My name is Sreeja Chithirala.My roll no is AP20110010321.Iam from CSE section 'E'.
The no of characters in the above txt file are  74
'''
