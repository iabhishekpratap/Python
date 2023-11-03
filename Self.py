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









































































































