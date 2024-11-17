tillnum=int (input("enter your specified no : "))

list=[]

for num in range(1, tillnum+1):

    result = "" #empty because we dont know the final addition in list
    
    if num % 3 ==0 and num % 5 ==0:
        result=result+"FizzBuzz"
    elif num %3 ==0:
        result=result+"Fizz"           
    elif num % 5 ==0:
        result=result+"Buzz"
    else:
        result=num
        
    list.append(result) #result will be add in the list accordiing to the condition

print(list)





    