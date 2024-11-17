class Employee:
    #constructor
    '''constructor is a special method used to
    initialize the attributes of a class 
    when an object is created.'''

    '''The constructor ensures that certain actions 
    (like initializing data or setting default values) 
    happen automatically whenever a new object is created.'''

#     def __init__(self): #this functional automatically called
#         print("const called")

# #object emp1
# emp1 = Employee()
#########################################################
#     def __init__(self,name,email,dept,salary): #this functional automatically called
#         self.name=name
#         self.email=email
#         self.dept=dept 
#         self.salary=salary
#         #self.email reperesent self(खुद का) mail of employe 
#         #=email represent that we provide

# #object emp1
# emp1 = Employee("raju","raju@gmail.com","sales", 4000)
# emp2 = Employee("shaym","shyam@gmail.com","hr", 40000)

# print(emp2.email)
##############################################################
    def __init__(self,name,email,dept,salary): #this functional automatically called
        self.name=name
        self.email=email
        self.dept=dept 
        self.salary=salary

    def empinfo(self):
        print("name is ",self.name)
        print("email is ",self.email)
        print("department is ",self.dept)
        print("salary is ",self.salary)

    def deptchange(self,newdept):
        self.dept=newdept
        print("department change to newdept",newdept)


# #object emp1, emp2
# emp1 = Employee("raju","raju@gmail.com","sales", 4000)
# emp2 = Employee("shaym","shyam@gmail.com","hr", 40000)

# print(emp2.email)
# emp1.empinfo()
# emp2.empinfo()

# emp1.deptchange("devops")

######################################3

# class Employee:
#     pass

# #object emp1
# emp1 = Employee()
# print(emp1)

