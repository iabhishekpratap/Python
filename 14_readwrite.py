# with open ("user.txt","w") as file:
#     file.write("this is the first file creating an write ") 


# with open ("user.txt","a") as file:
#     file.write (" second line\n")
#     file.write("third line")


# with open ("user.txt","r") as file:
#     content=file.read()

# print(content)

with open ("user.txt","r") as file:
    content=file.readlines()

for line in content:
    print("welcome",line.rstrip())