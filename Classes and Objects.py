'''
OOPS - Object Oriented Programming System

OBJECT?
REAL TIME ENTITY
    person
    bottle
    hair

    
Object - Real Time Entity
    Characterstic and Behaviour
        Appearance And Functionality 
    
Student 
    Sname, email               course choose

Admission Cards => class
Class => ia a blue print for the object
    template for the object

    
#
----------------------------
characterstic (attribute)
method(functionality)


sname:___________________
semail:__________________  
course:__________________

----------------------------

'''

# class AdmissionForm:
#     sname = "Vijay"             # attribute   <= variable
#     course = "B.Tech"


# #Student object // object creation
# student = AdmissionForm()     # object=class()
# print(student.course)


# #Student object // object creation
# student = AdmissionForm()     # object=class()
# print(student.course)
# student.course="BCA"        #Change for student
# print("Updated:",student.course)


# #Student object // object creation
# student2 = AdmissionForm()     # object=class()
# print("student2:",student2.course)   #default value



# class AdmissionForm:
#     name = "Vijay"
#     course = "B.Tech"           # attribute   <= variable

#     def info(self):      # method
#         print("My Name is:",self.name)
#         print("My Course is:",self.course)

# std=AdmissionForm()
# std.name="Ajay"     #
# std.info()




# class AdmissionForm:
#     name = "Samyak"          #class variable directly exits to the class
#     course = "B.Tech"           # attribute   <= variable

# print("before",AdmissionForm.name)   #class variable access by class name
# AdmissionForm.name="Regex"    #class variable change by class name
# print("after",AdmissionForm.name)    #class variable access by class name


# aman_student=AdmissionForm()
# print(aman_student.name)    #class variable access by object name





class AdmissionForm:
    #Constructor -  function use to initialize the memory address for object
    def __init__(self):   #self is current object
        print("Constructor Called")


x=AdmissionForm()   #class() => calling constructor
print("Return from const::",x)