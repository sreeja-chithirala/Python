m1=int(input("1st subject marks: "))   #taking the marks as input from the user
m2=int(input("2nd subject marks: "))
m3=int(input("3rd subject marks: "))
m4=int(input("4th subject marks: "))
m5=int(input("5th subject marks: "))
per=((m1+m2+m3+m4+m5)/500)*100    #calculating the percentage and giving the grade accordingly
if per>=90 :
    print("percentage=",per,"% , Grade=A")
elif per>=80 :
    print("percentage=",per,"% , Grade=B")
elif per>=70 :
    print("percentage=",per,"% , Grade=C")
elif per>=60 :
    print("percentage=",per,"% , Grade=D")
elif per>=40 :
    print("percentage=",per,"% , Grade=E")
else :
    print("percentage=",per,"% , Grade=F")
    
'''
1st subject marks: 81
2nd subject marks: 76
3rd subject marks: 69
4th subject marks: 54
5th subject marks: 90
percentage= 74.0 % , Grade=C
'''
