#INPUT KEY VALUE PAIR IN DICTIONARY
n=int(input("how many students  :  "))
stu={ }
for a in range(n):
      key=input("Name of the student : ")
      value=int(input("No. of wins  : "))
      stu[key]=value
print("The dictionary now is : ")
print(stu)
