class EMP:     #employee class
    def __init__(self):
        self.id=input("Enter id: ")
        self.name=input("Enter name: ")
        self.sal=int(input("Enter salary: "))
        
def PaySlip(obj):   #payslip function to display employee details
    print("EMP id: ",obj.id)
    print("EMP name: ",obj.name)
    print("EMP basic salary: ",obj.sal)
    HRA=0.18*obj.sal
    DA=0.1*obj.sal
    gross=obj.sal+HRA+DA
    net=gross-0.1*gross
    print("EMP HRA: ",HRA)
    print("EMP DA: ",DA)
    print("EMP GROSS SAL: ",gross)
    print("EMP NET SAL: ",net)
    
obj1=EMP()    #declaring objects of employee class
obj2=EMP()
print()
print("EMPLOYEE DETAILS: ")
print()
PaySlip(obj1)   #calling payslip function
print()
PaySlip(obj2)


'''
Enter id: 1870
Enter name: Stefen
Enter salary: 200000
Enter id: 1360
Enter name: Isac
Enter salary: 190000

EMPLOYEE DETAILS: 

EMP id:  1870
EMP name:  Stefen
EMP basic salary:  200000
EMP HRA:  36000.0
EMP DA:  20000.0
EMP GROSS SAL:  256000.0
EMP NET SAL:  230400.0

EMP id:  1360
EMP name:  Isac
EMP basic salary:  190000
EMP HRA:  34200.0
EMP DA:  19000.0
EMP GROSS SAL:  243200.0
EMP NET SAL:  218880.0
'''
