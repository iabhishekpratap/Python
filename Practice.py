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























































































