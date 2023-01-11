basic_sal=float(input("Enter basic salary: ")) #taking basic salary from user
if basic_sal <= 10000 :
    HRA = 0.2*basic_sal
    DA = 0.8*basic_sal
    gross = basic_sal + HRA + DA  #gross salary is sum of basic salary,HRA and DA
    print("The gross salary of this person is ",gross)
elif basic_sal <= 20000 :
    HRA = 0.25*basic_sal
    DA = 0.9*basic_sal
    gross = basic_sal + HRA + DA
    print("The gross salary of this person is ",gross)
else :
    HRA = 0.3*basic_sal
    DA = 0.95*basic_sal
    gross = basic_sal + HRA + DA
    print("The gross salary of this person is ",gross)
'''
Enter basic salary: 18000
The gross salary of this person is  38700.0
'''
