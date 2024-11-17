# import calc

# result=calc.add(10,20)
# print(result)

# x=calc.evenodd(3235352)
# print(x)


import emp

#object emp1, emp2
emp1 = emp.Employee("raju","raju@gmail.com","sales", 4000)
emp2 = emp.Employee("shaym","shyam@gmail.com","hr", 40000)

print(emp2.email)
emp1.empinfo()
emp2.empinfo()

emp1.deptchange("devops")