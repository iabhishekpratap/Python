(35.)#To get rnos, names and marks of the students and store these
#details in a file called "Marks.dat"
'''
fout=open("marks.dat","w")
n=int(input("How many students : "))
for i in range(n):
 rno=input("Enter Rno: ")
 name=input("Enter Name : ")
 mks=input("Enter Marks : ")
 fout.write(str(rno))2
 fout.write("\n")
 fout.write(name)
 fout.write("\n")
 fout.write(str(mks))
 fout.write("\n")
fout.close()
fin=open("marks.dat","r")
data=fin.readline()
print("File contents are : \n")
while data:
 print(data,end="")
 data=fin.readline()
fin.close()
'''
#(34.)No. of lines in a file
'''f=open("c:\poem\world.txt")
n1=0
for line in f:
 n1+=1
print(n1)
'''
#(33.) A PYTHON PROGRAM TO WRITE NUMERIC DATA IN A TEXT FILE
'''
f=open("nfile.txt","w")
num = int(input ("\nEnter the a Number "))
f.write(str(num)) # CONVERT NUMERIC DATA INTO
STRING
f.close()
#rREAD DATA FROM FILE
f=open("nfile.txt","r")
readdata = f.read()
print("The Entered Value is ",readdata)
f.close()
'''
#(32.) A PYTHON PROGRAM TO APPEND DATA IN FILE
'''
fapp=open("c:\\poem\\file.txt","a") # Open file in append mode
newtext = input ("\nEnter the text to append in the file ")
fapp.write(newtext)
fapp.close()
fin=open("c:\\poem\\file.txt","r")
new_data = fin.read()
print("Contents of the file are : ")
print(new_data)
fin.close()
'''
#(31.) A PYTHON PROGRAM TO COPY THE CONTENTS FROM ONE FILE TO OTHER
'''
fin=open("c:\poem\dragon.txt","r")
data_in=fin.read()
fout= open("c:\poem\dest.txt" ,"w")
fout.write(data_in)
fin.close()
fout.close()
fout= open("c:\poem\dest.txt" ,"r")
print(fout)
data_out=fout.read()
print(data_out)
fout.close()
'''
#(30.) A PYTHON PROGRAM TO FIND THE FREQUENCY OF A WORD IN A TEXT FILE
'''
count =0
f=open("c:\poem\dragon.txt","r")
data=f.read()
wordsList = data.split() # THIS FUNCTION IS USED TO BREAK THE LINE
INTO LIST OF WORDS
key = input ("\nEnter the word to find its frequnecy in the File : ")
for word in wordsList:
 if word == key:
 count =count +1
print("\n The frequency of word " , key , " is " ,count)
f.close()
'''

#(29.) A PYTHON PROGRAM TO COUNT ALL THE LINE HAVING 'a' AS LAST
#CHARACTER

'''
count =0
f=open("c:\poem\dragon.txt","r")
data=f.readlines()
print(data)
for line in data:
 print(line)
 if line[-1] == '': #In Binary File last character of the line is
at -2 position count=count+1
 count+=1
print("Number of lines having 'a' as last character is/are : " ,count)
f.close()
'''
#(28.) A PYTHON PROGRAM TO COUNT ALL THE LINE HAVING 'A' AS FIRST
#CHARACTER

'''
count =0
f=open("c:\poem\dragon.txt","r")
data=f.readlines()
print(data)
for line in data:
 if line[0] == 'A':
 count=count+1
print("Number of lines having 'A' as first character is/are : "
,count)
f.close()
'''
#(27.) A PYTHON PROGRAM TO SEARCH A WORD IN A TEXT FILE

'''
f=open("c:\poem\dragon.txt","r")
key = input ("\nEnter the word to be Searched in the File : ")
data=f.read()
wordsList = data.split() # THIS FUNCTION IS USED TO BREAK THE LINE
INTO LIST OF WORDS
print("wordlist : ", wordsList)
for word in wordsList:
 if word == key:
 print("\n Word Found ")
 break # Terminate the Loop
else:
 print("\n Word Not Found ")
f.close()
'''

#(26.) A PYTHON PROGRAM TO COUNT THE NUMBER OF DIGITS IN A TEXT FILE
'''
count =0
f=open("c:\poem\dragon.txt","r")
data=f.read()
for c in data:
 if c >= '0' and c<='9': # Check each character for 0-9
 count=count +1
print("The number of Digits in this file are : ",count)
f.close()
'''
#(25.) A python program to count the number of vowels in a text file
'''count =0
f=open('c:\poem\dragon.txt',"r")
data=f.read()
for c in data:
 if c== 'a' or c=='e' or c=='i' or c=='o'or c=='u': #
Check each character for a vowel
 count=count +1
print("The number of Vowels in this file are : ",count)
f.close()
'''
#(24.) A python program to find the number of characters in a text
#file
'''f=open('c:\poem\dragon.txt',"r")
characters=f.read() # Read entire file
count=len(characters)
print("The number of Characters in this file are : ",count)
f.close()
'''
#(23.) A python program to find the number of words in a text file
'''f=open('c:\poem\dragon.txt',"r")
linesList=f.readlines() # This method will creates a List of all lines
count=0
for line in linesList: # Read each line
 wordsList=line.split() # THIS FUNCTION IS USED TO
BREAK THE LINE INTO LIST OF WORDS
 #print(wordsList) # No Need to Print
 count = count+ len(wordsList)
print("The number of words in this file are : ",count)
f.close()
'''
#(22.)A python program to create and read a file
'''f=open("newfile.txt","w")
f.write("MY First Python text File !!!!\n\ndo all these programs ")
f.close()
# OPEN FILE TO READ
f=open("newfile.txt","r")
d=f.read()
print(d)
f.close()
'''
#(21.)Read the contents of the file
'''fin=open("stu_details.dat","r")
data=" "
while data:
 data=fin.readline()
 print(data,end="")
fin.close()
'''
#(20.)Write student's roll.no,name and marks in a file
'''fout=open("stu_details.dat","w")
count=int(input("Enter no. of students "))
for i in range(count):
 rno=input("Enter roll no : ")
 nm=input("Enter name : ")
 mk=float(input("Enter marks : "))
 fout.write(rno +"\t" +nm +"\t" +str(mk) +"\n")
fout.close()
'''
#(19.)Write student's names in a file using List
'''fout=open("stu_names_lst.txt","w")
stu_list=[ ]
for i in range(5):
 name=input("Enter name of student : ")
 stu_list.append(name+"\n")
print(stu_list)
fout.writelines(stu_list)
fout.close()
'''
#(18.)Write student's names in a file using string
'''fout=open("stu_names.txt","w")
for i in range(5):
 name=input("Enter name of student : ")
 fout.write(name)
 fout.write("\n")
fout.close()
'''
#(17.) A python program to find the number of lines in a text file
'''f=open('hello.txt',"r")
linesList=f.readlines()
count=0
print(linesList)
for line in linesList: # Read each line
 count = count+ 1
print("The number of lines in this file are : ",count)
f.close()
'''
#(16.)Display File Size
'''fin=open('c:\poem\dragon.txt',"r")
str=fin.read()
print(str)
size=len(str)
print("size of the given file is : ",size," bytes. ")
fin.close()
'''
#(15.)Reading the complete file in a list using readlines() method
'''fin=open(r'c:\poem\dragon.txt',"r")
s=fin.readlines()
print(s)
fin.close()
'''
#(14.) Display Contents of a file using for loop
'''fin=open('c:\poem\dragon.txt',"r")
print(fin)
for line in fin:
 print(line, end='')
fin.close()
'''
#(13.)Reading n bytes and then reading some more bytes from the last
#position
'''fin=open('c:\poem\dragon.txt',"r")
str=fin.read(10)
print(str)
str=fin.read(5)
print(str)
fin.close()
'''
#(12.)Opening and reading file in single command
'''file=open('c:\poem\dragon.txt',"r").read(20)
print(file)
'''
#(11.)Display Contents of a File Using readline( ) Function
'''myf=open('c:\poem\dragon.txt',"r")
str1=" "
while str1:
 str1=myf.readline()
 print(str1,end="")
myf.close()
'''
#(10.)Display Contents of a File Using read( ) Function
'''myf=open('c:\poem\how.txt',"r")
print(myf)
str=myf.read()
print(str)
'''
#(9.)Display Contents of a File With Limited No. of Bytes
'''
myfile=open('c:\poem\dragon.txt',"r")
str=myfile.read(8)
print(open('c:\poem\dragon.txt',"r").read(20))
print(str)
print(open('c:\poem\dragon.txt',"r").readline())
'''
#(8.)Appending data in a file
'''f=open("E:\\avi\\abhishek.txt","a")
f.write("file does not exists")
f.write("this line is appended at the end of existing file")
f.write("\nnext line")
print("data appended")
f.close()
'''
#(7.)Program to write data to a file using writelines method() and
#"with" command
'''with open("student.txt","w") as f :
 lst=
["vivek\n","christafar\n","ansh","saanidhya","manu\n","devansh\n","shi
vangi","Himanshi","abhishek"]
 f.writelines(lst)
 print("is the file closed -> ",f.closed)
print("is the file closed -> ",f.closed)
print("data written")
f.close()
print("is the file closed -> ",f.closed)
'''
#(6.)Program to write data to a file using writelines method()
'''f=open("student.txt","w")
name=
["vivek\n","christafar\n","ansh\n","saanidhya","manu\n","devansh\n","s
hivangi","Himanshi","abhishek"]
f.writelines(name)
print("data written")
f.close()
'''
#(5.)Program to write data to a file
'''f=open("my_file.txt","w")
f.write("This is my first file writing program ")
f.write("Write more programs")
f.write("end of file")
print("Written data to file")
f.close()
'''
#(4.)Reading of specific bytes
'''f=open(r"D:\ttable\kids.txt")
data=f.readline(30)
print(data)
f.close()
'''
#(3.)A basic file program
f=open("e:\world.txt")
data=f.read()
print(data)
f.close()

#(2.)Simple file commands
"""
f=open("e:\world.txt")
print("File name : ", f.name)
print("File mode : ", f.mode)
print("Is file readable : ", f.readable())
print("Is file closed : ", f.closed)
f.close()
print("Is file closed : ", f.closed)
f.close()
"""
#(1.)opening a file
"""f=open("e:\world.txt")
print(f)
f.close()"""



