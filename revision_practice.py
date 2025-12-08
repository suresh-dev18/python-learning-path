# #6 ways to reverse a List
# #using list method [reversed]
# mylist=[1,2,3,4,5]
# reversed_list=list(reversed(mylist))
# print(reversed_list)

# #using list comprehension with reversed()
# my_list=[10,20,30,40]
# reversed_list=[temp for temp in reversed(my_list)]
# print(reversed_list)

# #using reversed() method in-place
# grades=['a','b','c','d']
# grades.reverse()
# print(grades)

# #reversing a list using index slicing
# games=['volleyball','cricket','handball','hockey']

#variables basics
# name='suresh'
# print(name)
# print(id(name))

# #we cant assign same value to multiple variables using commas
# # a,b,c='i'
# # print(a)
# # print(b)

# #we can assign same value to multiple varables at a time using assignment =
# a=b=c=1
# print(a,b,c)

# c=1,2,3
# print(c)
# print(type(c))

#data types in python
'''
int
float
boolean
complex
'''
# num=-20
# #print(type(num))
# num1=1+3j
# print(type(num),(type(num1)))
# print(num is not num1)

# print(1==1)
# print(False==0)

#type conversion
# a=5
# print(str(a))

# #explicit data type conversion
# b=2.3
# c=int(b)
# print(c)

#control statements
#conditioinal statements [if,else,elif,nested if else]

# age=18
# if age>18:
#     print("you can vote")
# elif age==18:
#     print("you can vote")
# else:
#     print("you are minor, please wait")
#trying loops with different types of data
# persons={"suresh":25,"vikranth":23,'loku':26,'leela':31}
# for i in persons:
#     if persons.values()==25:
#         print("eligible to marry")
#     else:
#         print("focus on life")

#using functions to find prime numbers
# nums=range(1,1000) #taking a variable to take the numbers range 
# def is_prime(num):#creating a function is_prime
# #    print(num)
#     for x in range(2,num):
#         if(num%x)==0:
#             return False
#     return True
# primes=list(filter(is_prime,nums)) #calling function to get prime numbers in variable nums
# print(primes)

#using for & while 
# classes=range(1,11) 
# for i in classes:# for using because ,we know the number of statements to execute
#     if i<10:
#         print(f"{i} grade students go to ground")
#     else:
#         print(f"{i} grade students stay in class")

# classes=0
# while classes<10:#using while because ,i want execute it until some value to reach
#     print(f"{classes} grade students go to ground")
#     classes+=1

# x=int(5)
# print(x)
# print('Hello')
# print("Hello")
#to know current python version by importing sys module
# import sys
# print(sys.version)

# #oops override method example
# class memorydevice:
#     def printphysicalsize(self):
#         print("medium")
# class sdcard(memorydevice):
#     def printphysicalsize(self):
#         print("small")
# SDcard=sdcard()
# SDcard.printphysicalsize()

#basic class method using decorator
# class myclass:
#     class_variable=0
#     def __init__(self,instance_variable):
#         self.instance_variable=instance_variable
#     @classmethod
#     def increment_class_variable(cls):
#         cls.class_variable+=1
#         return cls.class_variable
# myclass.increment_class_variable()


#python patterns
# rows=5
# for i in range(1,rows+1):
#     print(' ' *(rows-i)+'*'*(2*i-1)) #upper part
# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+'*'*(2*i-1))  #lower part

#QR Code generating
# import qrcode
# qr=qrcode.make("my qrcode")
# qr.save("my_qrcode.png")
# print("QR code generated")
#code snippet
# def sum(a, b=[]):
#     total = 0
#     b.append(a)  # Add 'a' to the list 'b'
#     for num in b:  # Loop through the list 'b'
#         total += num  # Add each element in 'b' to 'total'
#     return total  # Return output after all iterations (Exits the loop)
# print(sum(4))
# print(sum(6))
# print(sum(2,))
# #finding LCM using functions
# #Since the LCM (Least Common Multiple) of two numbers is always greater than or equal to the larger of the two numbers, 
# #this is a logical starting point for checking.
# def find_lcm(a, b):
#     greater = max(a, b)  # Find the greater of the two numbers (to start checking for LCM)
#     while True:  # Infinite loop to keep checking until we find the LCM
#         if greater % a == 0 and greater % b == 0:  # Check if 'greater' is divisible by both a and b
#             return greater  # If divisible, 'greater' is the LCM, return it
#         greater += 1  # If not divisible, increment 'greater' and check again

# print(find_lcm(4, 6))  # Call the function with 4 and 6
# print(find_lcm(3,7))

# #list slicing
# list_x=[1,2,3,4,5]
# idx=slice(None,None,-1)
# result=list_x[idx]
# print(result)

#python doesn't support insert because it is immutable
# tuple=(5,10,20)
# tuple.insert(2,15)
# print(tuple)

#we can modify Tuple by using indexing
# my_tuple = (1, 2, 3)

# # Insert 5 at index 1 (between 1 and 2)
# new_tuple = my_tuple[:1] + (5,) + my_tuple[1:]

# print(new_tuple)  # Output: (1, 5, 2, 3)

# numbers=(1,2,3,4)
# if 5  in numbers:
#     print("number is there")
# print("number is not in")

#sample login program using nested if-else
# username=input("enter userrname:")
# if username=="suresh":
#     password=input("enter password:")
#     if password=="suresh@23":
#         print("login success")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")

#using short hand if
# number=int(input("enter your number:"))
# result="even" if number%2==0 else "odd"
# print(result)

# #short hand if-else
# number=int(input("enter your number:"))
# print(f"{number} is even") if number%2==0 else print(f"{number} is odd")

# rows=5
# for i in range(1,rows+1):
#     print('* ' * i) #i want space after every *, so im printing * followed by space
# #another process
# # Number of rows for the pattern
# rows = 5

# # Outer loop for each row
# for i in range(1, rows + 1):
#     # Inner loop for printing '*' in each row. if we are not using inner loop it will print single * in each line
#     for j in range(i):
#         print("*", end=" ")
#     # Move to the next line after each row
#     print()
    

#python program to calculate the power using recursion
# def power(base,exp):
#     if exp==0:#Vase class
#         return 1
#     return base * power(base,exp-1)
# #If exp is not 0, the function returns the result of multiplying base by the result of the function called with exp - 1.
# base=int(input("enter base value:"))
# exp=int(input("enter exponent:"))
# print(power(base,exp-1))
# print(power(base,exp))

#python patterns

# rows=5
# for i in range(1,rows+1):
#     print('*'*(2*i-1)) #leading spaces print upto * , trailing spaces wont print here

# #another method for same pattern that prints spaces at trailing end
# rows = 5
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1) + ' ' * (rows - i))

# print("==============================")
# #reverse pyramid pattern
# rows=5
# for i in range(rows,0,-1):
# #    print(i)
#     print(' '*(rows-i)+'*' *(2*i-1))

#full program
# rows=7
# for i in range(1,rows+1):
#     print(' '*(2*rows-i)+'*'*(2*i-1))# ' '*(2*rows-i)  - spaces reduces as i increases, to form central allignment
# for i in range(rows-1,0,-1):
#     print(' '*(2*rows-i)+'*'*(2*i-1))# '*'*(2*i-1) - controls width of each row

# rows=5
# for i in range(1,rows+1):
#     print(' '*(rows-i)+'*'*(2*i))
# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+'*'*(2*i)) 

# #pattern of X with stars *
# rows=5
# for i in range(1,rows+1):
#     print('*'*i+' '*(2*(rows-i))+'*'*i)
# for i in range(rows-1,0,-1):
#     print('*'*i+' '*(2*(rows-i))+'*'*i)

#rectangular box pattern
# rows=5
# for i in range(rows):#range is only rows , because no increment or decrement in pattern output
#     if i==0 or i==rows-1:#If it is the first or last row, print a solid row of stars (* * * * *).
#         print('*'*rows)
#     else:
#         print('*'+' '*(rows-2)+'*')#If it's not the first or last row, print a row with a star at the beginning and end, and spaces in between

# rows=5
# for i in range(rows):
#     print('*'*rows)

# import decimal
# integer=20
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

# from decimal import Decimal
# result=Decimal(0.9)+Decimal(0.6)
# print(int(result))
# #Financial calculations
# from decimal import Decimal,ROUND_HALF_UP

# import decimal
# string='1234'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string))) #Decimal (the class from the decimal module):

# name='suresh naidu'
# print(name[::-1])
# Name="".join(reversed(name))
# print(Name)
# print(id(Name))

#counting vowels in string
# vowel=['a','e','i','o','u','A','E','I','O','U']
# name='suresh naidu RAGIPATI'
# count=0
# for i in name:
#     if i in vowel:
#         count+=1
# print(count)
# #counting consonants in string
# vowel=['a','e','i','o','u']
# name='eiuhwihbfjdndfcslldloixea'
# char=0
# for i in name:
#     if i not in vowel:
#         char+=1
# print(char)

#counting the number of occurences of a character in a string
# name='ragipati suresh kumar naidu'
# char=0
# for rep in name:
#     if 'a' in rep:
#         char+=1
# print(char) 

# #finding maximum number in a list
# number_list=[13,24,56,74,78,90,234,567,976,1233,12,54,11]
# maximum=number_list[0]
# for num in number_list:
# a=0b1111
# print(a)
# b=0b10101110001
# print(b)
# c=0x10
# print(c)

#practice list
# l=['a',(1,2,3),5.6]
# print(type(l[1]))
# print(id(l))
# l[2]=True
# print(l)
# print(id(l))
# l1=l[1:]
# print(l1)
# print(len(l))
# # l[5]=100 #you cant assign a value beyond index range. we can go with append to acheive this
# # print(l)
# l.append(100)
# print(l)
# l.remove(l[2])
# print(l)
# print(len(l))

#Tuple practice # need less memory to store because static compared to list
# t=()
# print(type(t))
# l1=list(t)
# print(l1)
# l1.append(1)
# l1.append(2)
# print(l1)
# t=tuple(l1)
# print(t)
# tuple1=(10,)
# print(type(tuple1))

#set practice
# s={} #empty curly brace will considered as empty dict
# s1=set()
# print(type(s1))
# s1.add(3)
# print(s1)
# s2={'name',1,1,4,100}
# print(len(s2))
# print(s2)
# s2.add("suresh")
# print(s2)

#frozen set
# s={1,2,3,4,5}
# print(type(s))
# #print(s[-1]) #indexing & slicing is not possible
# s1=frozenset(s)
# print(s1)
# print(type(s1))
# print(len(s1))

#dictionary
# d={}
# print(type(d))
# d[1]='suresh'
# d[2]='btech'
# d[3]='job'
# d[10]=40
# print(d)
# print(len(d))
# d[3]="abcd" #key=3 is already existed . so ,its value will get replace.
# print(d)

# num=int(input("enter a number:"))
# result=sum(int(digit) for digit in str(num)) #first converting num(input) into string to iterate through it and then sumu up by again converting int(digit)
# print(result)

# input_numbers=input("enter numbers seperated by space:")
# user_list=input_numbers.split()
# print("user list is:",user_list)
# for i in range(len(user_list)):
#     user_list[i]=int(user_list[i])

# print('user given list is:',user_list)
# print('sum is:',sum(user_list))

#python code in line continuation
# addition=1+4\
# +6+7+8\
# +87
# print(addition)
#python code in multiline with braces
# a=(20+30+22+
# 31+8+90
# +32)
# print(a)

#multiple statements in single line
# length=5;breadth=5
# area=length*breadth;print(area)

# num1=int(input("enter the num1:"))
# num2=int(input("enter the num2:"))
# if num1>num2:
#     print(num1 ,"is greater than" , num2)
# elif num1<num2:
#     print(num2, 'is greater than ',num2)
# else:
#     print("both numbers are equal",num1,'=',num2)

# num=int(input("enter your number:"))
# if num>99:
#     if num%2==0:
#         print("number is even and greater than 99")
#     else:
#         print(num," the number is odd")
# elif num<99:
#     print(num, " number is lower than 99")
# else:
#     print("number is equal")

# def name(args):
#     pass
# x=20
# print(x)
# del x
# print(x)
#addition
# def addition(arg1,arg2):
#     return arg1+arg2
# print(addition(80,60))
# import datetime
# now=print(datetime.datetime.now()
# from datetime import datetime
# now=datetime.now()
# print(now)
# print(dir(datetime))

# from datetime import date
# curr=date(1998,4,23)
# print('my birth date is: ',curr)
# today=date.today()
# print('today:',today)
# print('year:',today.year)
# print("month:",today.month)
# print("day:",today.day)

# from matplotlib import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,20,30,40]
# plt.plot(x,y)
# plt.show()

# from datetime import datetime,date
# date1=datetime.now()
# print('today is:',date1)

# # from datetime import date
# date1=date(2003,12,30)
# print(date1)
# today=datetime.today()
# print(today)

# from datetime import datetime,time
# now=datetime.now()
# print(now)
# print(now.time())
# t1=time()
# print('time is:',t1)
# t2=time(hour=12,minute=45,second=6)
# print('current time is:',t2)
# t3=time(2,10,30)
# print('login time is:',t3)
# t4=datetime.now()
# print(t4)

# names=['suresh','manohar','babu']
# for item in names:
#     print(item, end=' ')

# def greet(name,region):
#     message=get_message(region)
#     return message +" "+ name
# def get_message(region):
#     if region=='usa':
#         return "hello"
#     else:
#         return "namaste"
# print(greet('suresh','usa'))
# print(greet('virat','india'))


# def greeting(name,location):
#     if location=='india':
#         return 'namaste'+" "+ name
#     else:
#         return 'hello'+' '+ name
# print(greeting('suresh','usa'))
# print(greeting('hesvi','india'))

# def bonus(salary):
#     return (salary*11/100)
# print(bonus(1000))

# import keyword
# print(keyword.kwlist)
# help("keywords")
# import keyword
# print(keyword.iskeyword('else'))
# print(keyword.iskeyword('range'))
# print(keyword.iskeyword('from'))

# x=23
# y=34
# z=x>y
# print(z)
# s=x<y
# print(s)

# x_salary=1000
# y_salary=3000
# if x_salary>=100 and y_salary<4000:
#     print(x_salary+500)
# else:
#     print(x_salary,y_salary)

# x = 10
# y = 20

# # and to combine to conditions
# # both need to be true to execute if block
# if x > 5 and y < 25:
#     print(x + 5)

# # or condition
# # at least 1 need to be true to execute if block
# if x > 5 or y < 100:
#     print(x + 5)

# # not condition
# # condition must be false
# if not x:
#     print(x + 5)

# my_data=['sUResh','jaya','vikranth','murali','mahesh','loku','krishna']
# # mylist=my_data.lower()
# check_name=input("enter your name:").lower()
# if check_name in my_data:
#     print("congratulations!, your name in list.")
# else:
#     print("sorry!.please try next time")

# for i in range(5):
#     print(i,end='\n')
# n=0
# while n<5:
#     print(n,)
#     n=n+1

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(self.name,self.age)
# s=student('suresh',26)
# s.show()

# with open("suresh.txt",mode='r',encoding='utf-8') as fp:
#     print(fp.read())

# mine=open("suresh.txt",mode='a')
# print(mine)
# import datetime  # importing entire module called datetime
# curr=datetime.datetime.now()  # fetching current time using now() method in datetime class from datetime module
# # stop=datetime.datetime.date(year=2025,month=3,day=6)
# # print(stop)
# print(f"current date and time is: {curr}")

#importing only required class from module
# from datetime import datetime
# today=datetime.now()
# print(f"today is: {today}")

# #return keyword
# def multiplication(num1,num2):
#     print(f"multiplication of given numbers {num1,num2} is:")
#     return  num1*num2   # return keyword is end of the function.you cant write program after return
# # print(f"mul of {num1,num2} is", multiplication(20,15))
# print(f"mul  is", multiplication(20,15))

# import asyncio
# async def suresh():
#     print("hello")
#     await asyncio.sleep(5)
#     print("how are you")
# print(suresh)
# asyncio.run(suresh())

# assign=input("enter project name:")
# import asyncio
# async def office(name,project=assign):
#     global assign
#     print(f"hi {name}")
#     await asyncio.sleep(3)
#     print("your project:",project)

# asyncio.run(office('suresh',assign))

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))
# print((aTuple[2:3]))
# print(type(0xFF))

# for i in range(1,10,3):
#     print(i)
#     if i==4:
#         break

# import pandas as pd
# df = pd.DataFrame({'A': [1, 2, None, 4]})
# df.fillna(df['A'].mean(), inplace=True)  # Fill missing values with mean
# import pandas
# mydata={'cars':['bmw','volvo','benz'],'passings':[1,5,2]}
# myvar=pandas.DataFrame(mydata)
# print(myvar)

# import pandas as pd
# print(pd.__version__)
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y, marker='o', linestyle='-', color='b')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Plot Example")
# plt.show()

# a=5+4.3j
# print(a)
# name='suresh'
# print(name)
# fullname=name+'naidu'
# print(fullname)
# print(fullname[2:6])

# my_list = ['Jessa', 10, 20, 'Kelly', 50, 10.5]
# print(my_list[0])
# print(my_list[3:])
# my_list[0]='suresh'
# my_list.append('murali')
# print(my_list)
# print(my_list[-1])
# my_list = ['Jessa', 10, 20, 'Kelly', 50, 10.5]
# name=my_list.append('mahesh')
# print(name)
# print(my_list)
# print(type(my_list))
# print(type(my_list).__name__)

# a,b,c=1,2,3  # multiple values to multiple variables
# print(a,b,c)
# x=y=z=10  # single value to multiple variables
# print(x,y,z)

#local variables
# def test1():
#     price=100
#     print("the price is ",price)
# def test2():
#     print("current price is:",price)

# test1()
# test2()

#global variables
# name='suresh'
# section='10b'
# price=12
# def stud1():
#     print("student name is:",name)
# def stud2():
#     print("student's section is:",section)
# stud1()
# stud2()
# x,y,x=10,20,30
# import sys
# print(sys.getrefcount(x))  # will give count for how many  variables assigned to same value

# a,b=10,30
# c=35
# d=11
# tuple1=a,b,c,d
# print(tuple1)

# tuple2=(3,6,9)
# x,y,z=tuple2
# print(x,y,z)

# names=['suresh','murali','mahesh']
# k,l,m=names  # list unpacking
# print(k,l,m)

# a=10
# b=10
# c=10
# import sys
# print(sys.getrefcount(a))

# x=10.5
# y=5
# print(x//y)

# a=5
# print(a)
# a+=2
# print(a)
# a-=3
# print(a)
# a*=4
# print(a)
# a/=5
# print(a)
# a//=5
# print(a)

# x=5
# y=10
# if x>0 and y>x:
#     print(f"multiplication is {x*y}")
# else:
#     print("do nothing")

# print(200 and 20)
# print(300 or 30)
# print(30 or 300)

# a=10
# # b=50
# if a>0 or b>0:
#     print(a+b)
# else:
#     print("do not need")

# print(not 1)
# print(not 0)
# list1=[1,20,23,18,45,7]
# number=100
# if number in list1:
#     print("number found")
# else:
#     print("number not found")

# list2=['suresh','murali','mahesh','hesvi']
# #search='hesvi'
# search=input("enter the name:")
# #while True:

# if search not in list2:
#     list2.append(search)
#     print(f"name added : {search}")
# else:
#     print("name found",search)
# print(list2)

# a,b,c=7,4,3
# print(~a,~b,~c)

# # name='suresh naidu'
# # print(name[3])
# # print(name[1]=='a')
# # salary=float(40000)
# # print(f"my salary {salary}")

# number=1.2223e3
# print(number)
# num1=45.8902516723727263e10
# print(num1)

# names=['murali','mahesh','suresh',]
# print(names[1])
# print(names[2:])
# names[2]='lohitha'
# names.append('varalakshmi')
# print(names)

# tuple1=(10,20,30,'suresh')
# print(tuple1)
# print(type(tuple1))
# tuple2=tuple(('2.abc',4,5.,3.))
# print(tuple2)
# print(type(tuple2))

# mydict={'suresh':3,
#         'murali':2,'mahesh':1}
# print(mydict)
# mydict['suresh']=4
# print(mydict)
# print(mydict['mahesh'])
# print(mydict.keys())
# print(mydict.values())
# mydict['murali']=1996
# print(mydict)

# names=set()
# print(type(names))
# names.add('suresh')
# names.add('murali')
# names.add('murali')
# print(names)
# names.remove('murali')
# print(names)
# names.add('mahesh')
# names.add('hesvi')
# print(names)
# names.clear()
# print(names)
# names.add('hesvi')
# print(names)
# names.copy()
# print(names)

# myset=set({1,2,3,4,5,5,6,6})
# print(myset)
# print(type(myset))
# myfroz=frozenset(myset)
# print(type(myfroz))
# list1=[1,3,2,4,4,5,6]
# list2=list([1,2,3,4,5,6,7,8])
# print(list1,',',list2)

# if(True):
#     print("0")
#     if(True):
#         print("1")
# else:
#     print("2")
# condition=True
# if condition:
#     print("0")   # Executes
#     if not condition:  
#         print("1")  # Executes
# else:
#     print("2")  
# a=[23,50,564,980]
# print(type(a))
# b=bytes(a)
# print(b)
# print(type(b))
# c=[20,40,55]
# d=bytearray(c)
# print(c)
# c[0]=100
# print(c)
# print(d)
# print(type(d))
# for i in d:
#     print(i,end=' ')

# numbers=range(20)
# while numbers<20:
#     for i in numbers:
#         print(i)
#         numbers+=1

# age=25.10
# print(type(age))
# ages=int(age)
# print(type(ages))
# myflag=True
# print(type(myflag))
# mine=int(myflag)
# print(mine)

# name='suresh'
# names=float(name)
# print(names)
# x=10
# y=20
# comp=complex(y,x)
# print(comp)
# comp1=complex(y)
# print(comp1)
# z='suresh'
# a=complex(z)
# print(a)
# names=[10,20]
# mine=(1,2,3)
# name=complex(names[0],names[1])
# print(name)
# name1=complex(names[1],mine[2])
# print(name1)
# a=1.3
# b=4.2
# c=complex(a,b)
# print(c)

# def function1():
#     x=50
#     print(x)
# function1()
# print(x)
# str1 = 'Ault\\'Kelly''
# 'str1 = 'Ault\'Kelly'
# str1 = """Ault'Kelly"""
# x=75
# def myfunction():
#     x=x+1
#     print(x)
# myfunction()
# print(x)
# str1 = 'Ault\'Kelly'
# print(str1)
# print(2%6)
# print(2 ** 3 ** 2)
# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

# name=input("enter name:")
# salary=input("enter the salary")
# company=input("enter the company")
# print("employee details are")
# print("employee_name salary company")
# print(name,salary,company)
# name,age,marks=input("enter name,age,marks seperated by space").split()
# print("student details:",name,age,marks)

about=[]
while True:
    line=input()
    if line:
        about.append(line)
    else:
        break
print(about)
