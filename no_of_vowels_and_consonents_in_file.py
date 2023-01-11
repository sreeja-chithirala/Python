f=open("python_2file.txt","r")
data=f.read()      #reads the content of the file and stores that in the form of string data
print(data)
v=0
c=0
for i in range(0,len(data)):  #in the string if we encounter the vowels V gets incremented and for consonents c gets incremented
    if data[i]=='a' or data[i]=='e' or data[i]=='i' or data[i]=='o' or data[i]=='u' or data[i]=='A' or data[i]=='E' or data[i]=='I' or data[i]=='O' or data[i]=='U' :
        v=v+1
        i=i+1
    elif (data[i]>='a' and data[i]<='z')  or  (data[i]>='A'  and data[i]<='Z') :
        c=c+1
        i=i+1
    else :
        i=i+1
        
print("no of vowels: ",v)
print("no of consonents: ",c)
print("other characters: ",(len(data)-v-c))   #other characters are simply length -vowels-consonents


'''
Hi!.My name is Sreeja Chithirala.My roll no is AP20110010321.Iam from CSE section 'E'.
no of vowels:  23
no of consonents:  33
other characters:  30
'''
