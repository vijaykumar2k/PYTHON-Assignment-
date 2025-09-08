# class BankAccount:
#   __charge = 50
#   def __init__(self,username,balance):
#     self.username = username
#     self.balance = balance

#   def withdrawa(self, amount):
#     new_amount = amount + self.__charge
#     if new_amount <= self.__balance:
#       self.__balance -= new_amount

#   def display(self):
#     print(f"The Balance is { self.__balance}")

# obj1 =  BankAccount("Vijay", 5000)
# print(f"Before Withdrawal the balance: ")
# obj1.display()

# obj1.withdraw(500)
# print(f"After Withdrawal the balance: ")
# obj1.display()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#   @abstractmethod
#   def start_Vehicle(self):
#     pass
  

# class Bike(Vehicle):
#   def start_Vehicle(self):
#     print("The Bike is starting with key.")
#   def  vehicle_wheels(self):
#     print("Wheel no. is 2")

# class Car(Vehicle):
#     def start_Vehicle(self):
#         print("The Car starts with key.")
#     def  vehicle_wheels(self):
#         print("Wheel no. is 4")

# car = Car()
# car.start_Vehicle()
# bike = Bike()
# bike.start_Vehicle()



# from abc import ABC, abstractmethod

# # Here we are basically making abstract class
# class shape(ABC):
#   @abstractmethod
#   def area(self):
#     pass

# class Rectangle(shape):
#   def area(self, length, breadth):
#     return length * breadth
  

# rect = Rectangle()
# area = rect.area(24, 10)
# print(area)



from abc import ABC, abstractmethod

class PaymentSystem(ABC):
  @abstractmethod
  def payment_initialize(self, amount):
    pass
  
  @abstractmethod
  def payment_process(self, amount):
    pass
  
  @abstractmethod
  def payment_status(self):
    pass
  

class UPI(PaymentSystem):
    def payment_initialize(self, amount):
        print(f"UPI Payment of {amount} is initialized.")
    
    def payment_process(self, amount):
        print(f"UPI Payment of {amount} is being processed.")
    
    def payment_status(self):
        print("UPI Payment is successful.")

upi = UPI()
upi.payment_initialize(100000)
upi.payment_process(100000)
upi.payment_status()



class CreditCard(PaymentSystem):
    def payment_initialize(self, amount):
        print(f"CreditCard Payment of {amount} is initialized.")
    
    def payment_process(self, amount):
        print(f"CreditCard Payment of {amount} is being processed.")
    
    def payment_status(self):
        print("CreditCard Payment is successful.")



CreditCard = CreditCard()
CreditCard.payment_initialize(50000)
CreditCard.payment_process(50000)
CreditCard.payment_status()


class PayPal(PaymentSystem):
    def payment_initialize(self, amount):
        print(f"Paypal Payment of {amount} is initialized.")
    
    def payment_process(self, amount):
        print(f"Paypal Payment of {amount} is being processed.")
    
    def payment_status(self):
        print("Paypal Payment is successful.")

paypal = PayPal()
paypal.payment_initialize(75000)
paypal.payment_process(75000)
paypal.payment_status()