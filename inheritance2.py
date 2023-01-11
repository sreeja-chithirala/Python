class car:  #parent car class
    def __init__(self):
        self.model=input("Enter model: ")
        self.speed=int(input("Enter speed: "))
        self.price=int(input("Enter price: ")) 
    
class firing_car(car):   #derived class firing_car
    def __init__(self):
        super().__init__()
        self.bullets=int(input("Enter no of bullets: "))
    def fire_method(self):
        print("The details of the car are: ")
        print("Model: ",self.model)
        print("Speed: ",self.speed)
        print("Price: ",self.price)
        print("No of bullets: ",self.bullets)

obj1=firing_car()  #declaring objects
obj2=firing_car()
print()
print("The car details are: ")   #printing their details
print()
obj1.fire_method()
obj2.fire_method()

'''
Enter model: Maruti
Enter speed: 165
Enter price: 315000
Enter no of bullets: 1
Enter model: Hyundai
Enter speed: 210
Enter price: 500000
Enter no of bullets: 2

The car details are: 

The details of the car are: 
Model:  Maruti
Speed:  165
Price:  315000
No of bullets:  1
The details of the car are: 
Model:  Hyundai
Speed:  210
Price:  500000
No of bullets:  2
'''
