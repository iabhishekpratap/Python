"""
"""run=int(input("Enter A Number : "))
if run>=100:
    print("batman scored century")
elif run >=50:
    print("batman scored a fifty")
else:print("batman nither score a century or fifty")
"""

"""
import os
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="apsingh", database="apple")
mycursor = mydb.cursor()


def AccInsert():
        L = []
        Accno = int(input("Enter the Account number : "))
        L.append(Accno)
        name = input("Enter the Customer Name: ")
        L.append(name)
        age = int(input("Enter Age of Customer : "))
        L.append(age)
        occup = input("Enter the Customer Occupation : ")
        L.append(occup)
        Address = input("Enter the Address of the Customer : ")
        L.append(Address)
        Mob = int(input("Enter the Mobile number : "))
        L.append(Mob)
        Aadharno = int(input("Enter the Aadhar number : "))
        L.append(Aadharno)
        Amt = float(input("Enter the Money Deposited : "))
        L.append(Amt)
        AccType = input("Enter the Account Type (Saving/RD/PPF/Current) : ")
        L.append(AccType)
        cust = (L)

        sql = "Insert into ACCOUNT(Accno ,Name,Age,occu,Address,Mob,Aadharno,amt,AccType) values(%s,%s,%s, %s,%s,%s, %s,%s,%s)"
        mycursor.execute(sql, cust)
        mydb.commit()


# --------------------------------------------------------
def AccView():
        print("Select the search criteria : ")
        print("1. Acc no")
        print("2. Name")
        print("3. Mobile")
        print("4. Aadhar")
        print("5. View All")
        ch = int(input("Enter the choice : "))
        if ch == 1:
                s = int(input("Enter ACC no : "))
                rl = (s,)
                sql = "select * from account where Accno=%s"
                mycursor.execute(sql, rl)
        elif ch == 2:
                s = input("Enter Name : ")
                rl = (s,)
                sql = "select * from account where Name=%s"
                mycursor.execute(sql, rl)
        elif ch == 3:
                s = int(input("Enter Mobile No : "))
                rl = (s,)
                sql = "select * from account where Mob=%s"
                mycursor.execute(sql, rl)
        elif ch == 4:
                s = input("Enter Adhar : ")
                rl = (s,)
                sql = "select * from account where Aadharno=%s"
                mycursor.execute(sql, rl)
        elif ch == 5:
                sql = "select * from account"
                mycursor.execute(sql)
        res = mycursor.fetchall()
        print("The Customer details are as follows : ")
        # print("(Accno ,Name,Age,occu,Address,Mob,Aadharno,amt,AccType)")
        # for x in res:
        k = pd.DataFrame(res, columns=['AcNo', 'Name', 'Age', 'Occn', 'Add', 'Mob', 'Aadh', 'Amt', 'AccTy'])
        print(k)


# --------------------------------------------------
def AccDeposit():
        L = []
        Accno = int(input("Enter the Account number : "))
        L.append(Accno)
        Amtdeposit = eval(input("Enter the Amount to be deposited : "))
        L.append(Amtdeposit)
        month = input("Enter month of Salary : ")
        L.append(month)
        cust = (L)
        sql = "Insert into amt(Accno,Amtdeposite,Month) values(%s,%s,%s)"
        mycursor.execute(sql, cust)
        mydb.commit()


# ---------------------------------------------------------------------
def closeAcc():
        Accno = int(input("Enter the Account number of the Customer to be closed : "))
        rl = (Accno,)
        sql = "Delete from amt where Accno=%s"
        mycursor.execute(sql, rl)
        sql = "Delete from Account where Accno=%s"
        mydb.commit()


# -------------------------------------------------
def accView():
        #        print("Please enter the details to view the Money details :")
        #      Accno=int(input("Enter the Account number of the Customer whose amount is to be viewed : "))
        #        sql="Select Account.Accno, Account.Name,Account.Age,Account.occu,Account.Address,Account.Mob,Account.Aadharno,Account.Amt,Account.AccType, sum(amt.Amtdeposite), amt.month from Account INNER JOIN amt ON Account.Accno=amt.Accno and amt.Accno = %s"
        sql = "Select Account.Accno,Name,Age,occu,Address,Mob,Aadharno,AccType , sum(amt.amtdeposite)+amt from Account,amt where (account.accno=amt.accno) group by amt.accno"

        #    rl=(Accno,)
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print("AccountNo\tName\tAge\tOccupation\tAddress\tMobile No.")
        for x in res:
                print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t", x[4], "\t", x[5], "\t", x[6], "\t", x[7], "\t",
                      x[8], "\t")
                # ---------------------------------------------------


def runAgain():
        runAgn = input("\nwant To Run Again Y/n: ")
        while (runAgn.lower() == 'y'):
                if (platform.system() == "Windows"):
                        print(os.system('cls'))
                else:
                        print(os.system('clear'))
                MenuSet()
                runAgn = input("\nwant To Run Again Y/n: ")


# -------------------------------------------------

def MenuSet():
        print("Enter 1 : To Add Customer")
        print("Enter 2 : To View Customer ")
        print("Enter 3 : To Deposit Money ")
        print("Enter 4 : To Close Account")
        print("Enter 5 : To View All Customer Details")
        try:  # Using Exceptions For Validation
                userInput = int(input("Please Select An Above Option: "))  # Will Take Input From User
        except ValueError:
                exit("\nHy! That's Not A Number")  # Error Message
        else:
                print("\n")  # Print New Line
        if (userInput == 1):
                AccInsert()
        elif (userInput == 2):
                AccView()
        elif (userInput == 3):
                AccDeposit()
        elif (userInput == 4):
                closeAcc()
        elif (userInput == 5):
                accView()
        else:
                print("Enter correct choice. . . ")


MenuSet()
runAgain()
"""
#Write a program to remove all the lines that contain the character `a' in a file
#and write it to another file.

"""apple= open("f:\\old.txt",'r')
lines = apple.readlines()
ball=open("f:\\new.txt",'w')
for x in lines:
    if 'a' not in x:
        ball.write(x)
print("File written Successfully..")
apple.close()
ball.close()"""
l=eval(input("Enter the elements of list "))
ele=int(input("Enter the element to be searched "))
low=0
high=len(l)
while low<=high:
        mid=int((low+high)/2)
        if ele==l[mid]:
                print("Element found at ", mid, " location ")
                break
        elif ele<=l[mid]:
                high=mid-1
        else:
                low=mid+1
else:
        print("Element not found")



import numpy
numpy.arange(5)
"""



'''
x=(8<9)
type(x)
print(type(x))
'''
'''
x,y,z=1,2,3
x-y
print(x-y)
'''
'''
x=input("Enter a Number : ")
x=eval(x)
y=input("Enter another Number : ")
y=eval(y)
z=x*y
print("This Is Your Answer : ",z)'''


'''
x=input("Enter Total Marks")
x=eval(x)
y=input("Enter Obtain Marks")
y=eval(y)
z=(y/x)*100
print(z,"%")
'''
# User Defined Function
'''
def x():
    print("I am a Boy")
    print("apple")
print(x())
'''
'''
x=input("Enter Your Name :")
print("Hello",x)
'''
'''
x=input("Enter °F ")
x=eval(x)
z=(x*9/5+32)
print(z,"°C")
'''

'''
x=input("Enter Original Price : ")
x=eval(x)
y=input("Enter Selling Price : ")
y=eval(y)
z=(y-x)
print("+ Profit / - Loss : ",z)
'''
'''
from collections import namedtuple
x=namedtuple("Fruitsname","apple , grapes ,pomagranet,watermelon")
y=x("green","black","red","sweet")
print(y)
'''
'''
from collections import namedtuple
a=namedtuple("cources","apple,ball,cat")
b=a._make(["green","bat","meaw"])
print(b)
'''

'''
from collections import deque
a=['apple','ball','cat','dog']
d=deque(a)
print(d)

d.append("python")
print(d)

d.append("apple")
print(d)

d.appendleft("cat")
print(d)

d.pop()
print(d)
'''
'''
from collections import ChainMap
a={1:"abhishek",2:"bro"}
b={3:"ram",4:"bhai"}
c=ChainMap(a,b)
print(c)
'''
'''
from collections import Counter
a=[1,2,1,3,3,4,4,5,6,7,5,6]
b=Counter(a)
print(b)

print(list(b.elements()))

print(b.most_common())

sub={3:1,4:2}
print(b.subtract(sub))
print(b.most_common())

'''
'''
from collections import OrderedDict
a=OrderedDict()
a[1]="ram"
a[2]="AAm"
a[3]="Syam"

a[1]="Ashiqui"
print(a)
'''
'''
from collections import defaultdict

a=defaultdict(str)
a[1]="abhishek"
a[2]="bhai"
print(a)
'''
'''
import math
x=8-6+((6*2)/7)-(math.sqrt(64))
print(x)
'''
"""
# area of triangle
a=int(input("Enter Base In CM :"))
b=int(input("Enter Height In CM :"))
c=(1/2)*(a*b)
print(c)
"""

"""
# Print Pattern With Star
def x(n):
    for i in range (0,n):
        for j in range (0,i+1):
            print("*",end="")
        print("\n")
n=int(input("Enter A No : "))
x(n)
"""

'''
a=input("Enter Type Of Currency : ")
if a == "dollar":
    b=int(input("Enter Value : "))
    print("In Indian Currency : ",b*76)
else :
    d=int(input("Enter Value : "))
    print("In Dollar :",d/76)
'''
'''
print("AREA OF CIRCLE")
a=int(input("Enter Radius : "))
import math
b=math.pi*a**2
print("Area : ",b)
'''
'''
print("AREA OF EQALATERAL TRIANG]
a=int(input("Enter A Side : "))
import math
b=math.sqrt(3)
c=(b/4)*a**2
print(c)
'''

"""
import array as arr
a=arr.array("i",[1,2,3,4,5,6])
print(a)
x=a[2]
print(x)

"""
"""
import array as arr
a=arr.array("i",[1,2,3])
b=arr.array("i",[4,5,6])
c=a+b
print(c)
c=arr.array('i', [1, 2, 3, 4, 5, 6])
print(c[0:2])
"""
"""
import array as arr
a=arr.array("i",[1,2,3,4,5,6])
print(a)

for x in a:
    print(x)

print("Length Of Array :",len(a))
b=0
while b<len(a):
    print(a[b])
    b=b+1
"""
"""
import array as arr
a=arr.array("i",[1,2,3,4,5])
for x in a :
    print(x)
print("Another Programme :")
for x in a[0:2] :
    print(x)

"""

# Creating Dictionary

dict1={"ram":"001","shyam":"002","mohan":"003","sohan":"004"}

"""print(dict1)
print(type(dict1))"""

# cerating dictionary by using dict function
"""
x=dict(ram="001",shyam="002")
print(x)
"""

# Nested Dictionary
"""
x={"ram":{"id":"001","Designation":"boss","salary":"9182741"},"shyam":{"id":"002","designation":"secratery","salary":"93694q86"}}
print(x)
import array as arr
a=arr.array("i",[1,2,34,5])
print(a)

"""

"""
dict1={"ram":"001","shyam":"002","mohan":"003","sohan":"004"}
y=dict1["ram"]
print(y)
print(dict1.keys())
print(dict1.values())
print(dict1.get("ram"))
for x in dict1:
    print(x)
for x in dict1.values():
    print(x)
for (x,y) in dict1.items():
    print(x,y)
"""
"""
# Updating Dictionary
var = ('\n'
       'd={"Ram":"001","Shyam":"002","Mohan":"003"}\n'
       'd["Ram"]="004"\n'
       'd["Sohan"]="005"\n'
       'print(d)\n')



#Deleting Entries
"""
"""
d={"Ram":"001","Shyam":"002","Mohan":"003"}
print(d.pop("Ram"))
print(d)
"""

# Convert Dictionary Into DataFrame
"""x={"Ram":{"Id":"123","Salary":"1234","designation":"boss"},"Shyam":{"Id":"002","Salary":"5678","designation":"Pa"}}
import pandas as ap
y=ap.DataFrame(x)
print(y)"""

"""
import random
x=random.random()
y=random.randint(0,4)
print(int(x),":",y+int(x))
"""
"""x=[0.5*x for x in range(0,4)]
print(x)
"""
"""
x=23
y=21
x.random.random()
y=random.randit(23.21)
print()

"""

s="welcome2kv"
n = len(s)
m=""
for i in range(0, n):
    if (s[i] >= 'a' and s[i] <= 'm'):
      m = m +s[i].upper()
    elif (s[i] >= 'n' and s[i] <= 'z'):
        m = m +s[i-1]
    elif (s[i].isupper()):
        m = m + s[i].lower()
    else:
         m = m +'#'
print(m)





























































































































































































