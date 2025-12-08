# number1=20
# number2=30
# print(f"the result is {number1*number2}")
# num1=20
# num2=30
# print(f"the addition is {num1+num2}")

#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.
# number1=int(input("enter the number1:"))
# number2=int(input("enter the number2:"))
# addition=number1+number2
# multiplication=number1*number2
# if multiplication<1000:
#     print(f"the multiplication of 2 numbers is :{multiplication}")
# else:
#     print(f"addition of given numbers is:{addition}")

#using functions
# def muliple_or_sum(number1,number2):
#     product=number1*number2
#     if product<=1000:
#         return product
#     else:
#         return number1+number2
# result=muliple_or_sum(20,30)
# print("the output is",result)
# result=muliple_or_sum(50,50)
# print(f"the result is:{result}")

#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number

# for i in range(1,11):
    # if i==0:
    #     continue
    # print(f"current number is {i}, previous number is {i-1}. the addition is {i+(i-1)}")

# previous_num=0
# for i in range(11):
#     sum=previous_num+i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", sum)
#     previous_num=i

# rect=(4,5)
# len,width=rect
# area=len*width
# print(area)

# odd_input = input("Enter odd numbers separated by spaces: ")
# # Create a tuple from the user input
# odd_numbers = tuple(int(num) for num in odd_input.split())

# even_input = input("Enter even numbers separated by spaces: ")
# # Create a tuple from the user input
# even_numbers = tuple(int(num) for num in even_input.split())

# # Concatenate the two tuples
# combined_tuple = odd_numbers + even_numbers
# sorted_tuple=sorted(combined_tuple)
# print(f"Combined tuple: {combined_tuple}")
# print(f"sorted tuple is {sorted_tuple}")

#Write a Python code to accept a string from the user and display characters present at an even index number.
# alphabets=input("enter the string:")
# range1=len(alphabets)
# for i in range(0,range1,2):
        
#Write a Python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. 
# However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100"

# numbers = [25, 30, 20, 40, 15, 25]
# sum=0
# for i in numbers:
#     sum+=i
#     if sum>100:
#         print(f"sum is {sum}, exceeded 100")
#         break
#     else:
#         print(f"the sum is {sum} ")

# def my_function(country = "Norway"):
#   print("I am from" ,country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# fruits = ["apple", "banana", "cherry"]
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

#positional arguments
# def my_func(x,**y):
#     print(x)
#     print(y)
# my_func([1,2,3],name='suresh',role='job')

# def my_function(*, x,y):
#     z=x+y
#     return z
# sum=my_function(x=5,y=7)
# print(sum)

# def my_function(a,b ,/,*, c,d):
#     print(a+b+c+d)
# my_function(1,2,c=9,d=7)

# def my_function(n):
#     if n==0:
#         return 0
#     return my_function(n-1)+n
# n=int(input("enter the number:"))
# res=my_function(n)
# print(res)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
# #    print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# res=tri_recursion(6)
# print(res)

#fibonacci series
# def fibonacci_series(n):
#   a,b=0,1
#   series=[]
#   for i in range(n):
#     series.append(a)
#     a,b=b,a+b
#   return series
# num_terms=int(input("enter the no of terms:"))
# if num_terms<=0:
#   print("pls enter positive integer")
# else:
#   print("fibonacci series")
#   print(fibonacci_series(num_terms))
# print('hello world')
# x=7,8,9
# print(x)
# print(x==7,8,9)

# x=y=1,2,3
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# print(id(x) is not id(y))

# x=1234567890
# y=1234567890
# print(id(x))
# print(id(y))
# print(id(x) is id(y))

# animal = "dog"

# match animal:
#     case "cat":
#         print("It's a cat")
#     case "dog":
#         print("It's a dog")
#     case _:
#         print("Unknown animal")

# for i in range(1,8):
#     if i%3==0 or i%4==0:
#         continue
#     print(i,end=' ')

# count=1
# while count<=3:
#     print(count*2)
#     count+=1


# import random
# target_num,guess_num=random.randint(1,10),None
# while target_num!=guess_num:
#     guess_num=int(input('guess a number between 1 and 10 until u get it right:'))
# print('well guessed!')

#second version
# import random

# target_num = random.randint(1, 10)
# guess_num = 0

# while guess_num != target_num:
#     guess_num = int(input("Guess a number between 1 and 10: "))
#     if guess_num < target_num:
#         print("Too low, try again!")
#     elif guess_num > target_num:
#         print("Too high, try again!")

# print("Well guessed!")

# def append_item(item,container=[]):
#     container.append(item)
#     return container
# print(append_item(1),append_item(2))

# for i in range(3):
#     print(i)
#     continue

# d= {1:10,2:20,3:30}
# for k,v in d.items():
#     print(k+v,end=' ')

# from collections import defaultdict
# d=defaultdict(int)
# for x in [1,2,2,3,3,3]:
#     d[x]+=1
# print(d[2]+d[3])

#functions
#lambda ,qfilter,
#lambda syntax- -> lambda args:expression
#filter syntax--> filter(function,iterable)
# list1= [1,2,3,4,5,6,7,8,9,10]
# my_output= filter(lambda i:i%2==0,list1)
# print(list(my_output))
# print(tuple(my_output))

# x={}
# y=[1,2]
# z=[3,4]
# print(x.fromkeys(y,z))

# map function
#map syntax: map(function,iterable)
# def  sqr(i):
#     return i**2
# result=map(sqr,[1,2,3,4])
# print(result)

# from functools import reduce
# list2=[10,10.5,30,5.9,66,4.32]
# def add(a,b):
#     return a+b
# results=reduce(add,list2)
# print(results)

# #from functools import reduce
# sequence=1,3,5,7,8,33,44,64,89,10.10,20.3
# def mul(a,b):
#     return a*b
# mymulti=reduce(mul,sequence)
# print(mymulti)

def get_numbers():
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    return numbers

print(get_numbers())

def get_numbers():
    for i in range(1, 6):
        yield i

for num in get_numbers():
    print(num)
