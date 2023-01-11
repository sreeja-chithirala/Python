class student:     #student class
    def __init__(self):
        self.id=input("Enter id: ")
        self.name=input("Enter name: ")
        self.mid1=int(input("Enter mid1 marks: "))
        self.mid2=int(input("Enter mid2 marks: "))
        self.quiz=int(input("Enter quiz marks: "))
    def result(self):
        print("Roll no: ",self.id)
        print("Name: ",self.name)
        print("Mid1 marks: ",self.mid1)
        print("Mid2 marks: ",self.mid2)
        print("Quiz marks: ",self.quiz)
        total=self.mid1+self.mid2+self.quiz
        print("Total: ",total)
        if total>=80:
            print("Result: A grade")
        elif total<80 and total>=60:
            print("Result: B grade")
        elif total>=50 and total<60:
            print("Result: C grade")
        else:
            print("Result: D grade")
    
obj1=student()   #declaring objects
print()
obj2=student()
print()
obj3=student()
print()
print("STUDENT RESULTS")
print()
print("STUDENT 1")
obj1.result()   #printing student details
print()
print("STUDENT 2")
obj2.result()
print()
print("STUDENT 3")
obj3.result()
print()


'''
Enter id: 123
Enter name: bhoomika
Enter mid1 marks: 24
Enter mid2 marks: 20
Enter quiz marks: 40

Enter id: 124
Enter name: mahita
Enter mid1 marks: 24
Enter mid2 marks: 23
Enter quiz marks: 25

Enter id: 122
Enter name: hema
Enter mid1 marks: 20
Enter mid2 marks: 20
Enter quiz marks: 30

STUDENT RESULTS

STUDENT 1
Roll no:  123
Name:  bhoomika
Mid1 marks:  24
Mid2 marks:  20
Quiz marks:  40
Total:  84
Result: A grade

STUDENT 2
Roll no:  124
Name:  mahita
Mid1 marks:  24
Mid2 marks:  23
Quiz marks:  25
Total:  72
Result: B grade

STUDENT 3
Roll no:  122
Name:  hema
Mid1 marks:  20
Mid2 marks:  20
Quiz marks:  30
Total:  70
Result: B grade
'''
