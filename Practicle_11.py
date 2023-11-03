
#Program to input names of 'n' employees and their salary details
#(basic salary,HRA,conveyance allowance.Calculate total salary of each employee and display
'''

d1=dict()
i=1
n=int(input("Enter no. of employees :"))
while i<=n:
    name=input("Enter Name : ")
    basic=int(input("Enter Basic : "))
    hra=int(input("Enter HRA : "))
    ca=int(input("Enter Conveyance Allowance : "))
    d1[name]=[basic,hra,ca]
    i=i+1
lst=d1.keys()
print("Name\t\tNet Salary")
for i in lst:
    tot_sal=0
    x=d1[i]
    for y in x:
        tot_sal=tot_sal+y
    print(i, "\t\t",tot_sal)
'''    
#21.Program to count the frequency of list-elements using a dictionary

'''
import json
msg="Dictionaries are a way of storing elements just like you would\
    in a Python list. But, rather than accessing elements using\
    its index, you assign a fixed key to it."
words=msg.split()
dct={}
for x in words:
    var=x
    if var not in dct:
        count=words.count(var)
        dct[var]=count
print(json.dumps(dct,indent=1))
'''
#20.Program to display unique and duplicate items of a given list
'''
lst1=[4,7,9,2,5,12,15,24,32,4,15,4,4,2,15,4,11]
lst2=[]
lst3=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
    else:
        if lst3.count(i)==0:
            lst3.append(i)
print("Unique elements -> ",lst2)
print("Repeated elements -> ",lst3)
'''
#19.To count frequency of an element in a list of numbers
'''
lst=[4,7,9,2,5,12,15,24,32,4,15,4,4,2,15,4,11]
length=len(lst)
print("List elements are : ", lst)
ele=int(input("Enter the element to be searched for : "))
count=0
for i in range(length):
    if ele==lst[i]:
        count+=1
if count==0:
    print(ele, " not found in the given list ")
else:
    print(ele," found ",count," no. of times.")
'''
#18.To remove vowel in a string
'''
st1=input("Enter a string : ")
st2=""
l=len(st1)
for i in range(l):
    if st1[i] not in 'aeiouAEIOU':
        st2 += st1[i]
print("Original string -> ", st1)
print("New string -> ", st2)
'''
#17.To Count no. of time 'the' appears in a line

st1=input("Enter a line : ")
st2="the"
x=st1.split()
ctr=0
for i in x:
    if i==st2:
        ctr+=1
print("No. of times ",st2," appearing : ",ctr)

#16.To capitalize every alternate letter
'''
st=input("Enter a string : ")
length=len(st)
print("Original string -> ", st)
st2=""
for x in range(length):
    if x%2==0:
        st2 += st[x]
    else:
        st2 += st[x].upper()
print("New string is : ",st2)
'''
#15.To find sum of digits of a number
'''
num=int(input("Enter a number "))
sum1=0
while num>0:
    sum1=sum1+(num%10)
    num //= 10
print("Sum of digits : ",sum1)
'''
#14. To display a pattern
'''
i=1
num=65
while i<=5:
    j=1
    while j<=i:
        print(chr(num),  end=' ')
        j+=1
        num += 1
    print()
    i += 1
'''
#13.To check whether a number Palindrome or Not
'''orig=int(input("Enter a number : "))
num=orig
rev=0
while num>0:
    r=num%10
    rev = rev *10 + r
    num = num//10
if orig == rev :
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
#12.To display first n prime numbers
'''
n=int(input("Enter a number : " ))
ctr=1
while ctr<=n:
    i=2
    flag=0
    while i<ctr:
        if ctr%i==0:
            break
        i += 1
    else:
        print(ctr, " is a prime number ")
    ctr += 1
'''       
#11. to check whether a character vowel or consonant
'''
st=input("Enter a single character : ")
if st in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
'''
#10.Use of break & else command
'''
for val in "good morning":
    if val== 'r':
        continue
    print(val)
else:
    print("Over")
'''
#9.Use of break & else command
'''
for val in "good morning":
    if val== 'r':
        break
    print(val)
else:
    print("Bye")

'''
#8.Display of Pattern
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
'''
#7.Sum of first n numbers
'''
num=int(input("Enter limit : "))
sum1=0
for i in range(num+1):
    sum1 += i
print("Sum of first ",num, " numbers is ",sum1)
 '''      
#6.To calculate and display the factorial of an inputted number
'''
num=int(input("Enter a number : "))
fact=1
for i in range(2,num+1):
    fact=fact*i
print("Factorial of given number is : ",fact)
'''   
#5.Program to accept salary and calculate tax amount
'''
sal=int(input("Enter salary of a person : "))
if sal<=50000:
    tax=0.05*sal
elif sal<=60000:
    tax=0.07*sal
elif sal<=70000:
    tax=0.08*sal
else:
    txt=0.10*sal
print("Salary : ",sal," Tax : ",tax)
'''
#4.To calculate largest of three inputted numbers
'''
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
big=a
if b>big:
    big=b
if c>big:
    big=c
print("The largest of three inputted numbers is : ",big)
'''
#3.To calculate simple interest
'''
prin=float(input("Enter principle amount : "))
rate=float(input("Enter rate : "))
time=float(input("Enter Time : "))
sim_int=(prin*rate*time)/100
print("Simple Interest is : ",sim_int)
'''
#2.To find amount for given cost-qty-discount
'''
cost=float(input("Enter cost : "))
qty=int(input("Enter Quantity : "))
dis=int(input("Enter discount in % : "))
amount=(cost*qty)-(cost*qty)*dis*(0.01)
print("Amount : ",amount)
'''
#1.To find average and grade for given marks
'''
print("Enter Details of Student :  ")
sub1=int(input("Enter Marks in English : "))
sub2=int(input("Enter Marks in Accountancy : "))
sub3=int(input("Enter Marks in Economics : "))
sub4=int(input("Enter Marks in B.Studies : "))
sub5=int(input("Enter Marks in IP : "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if avg>90:
    gr="A+"
elif avg>=75:
    gr="A"
elif avg>60:
    gr="B+"
elif avg>45:
    gr="B"
elif avg>=33:
    gr="C"
else:
    gr="Fail"
print("Average Marks : ",avg,"\nGrade : ",gr)
'''
