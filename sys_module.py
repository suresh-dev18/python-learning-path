# from sys import argv
# print("total arguments are",len(argv))


# #name=input("enter the name:")
# #print("your name is:",name)

# name=input("name is:")
# village=input("village is:")
# country=input("country name:")
# country_rank=int(input("country rank :"))
# print("your details are:",name ,village,country,country_rank,sep="%")

#output formatting

# name=input("enter the name:")
# salary=input("enter salary")
# company=input("enter company name")
# print('\n')
# print('{0},{1},{2}'.format(name,salary,company))

#taking string in output
# name=input("enter name:")
# marks=int(input("enter marks"))
# print('\n')
# print('student: name:{firstname}, marks:{achiv}'.format(firstname=name,achiv=marks))

# text=input("enter your text:")
# print('\n')
# print(text)
# print('{:>30}'.format(text))
# print('{:^30}'.format(text))
# print('{:<30}'.format(text))

# print(text.ljust(50,'#'))
# print(text.rjust(50,'#'))
# print(text.center(50,'#'))

# password=input("enter your password:")
# if password=='Suresh@1998':
#     print("password is correct! login success")
# else:
#     print("incorrect password, please try again!!")

# def emp_check(choice):
#     if choice==1:
#         print("developer")
#     elif choice==2:
#         print("tester")
#     elif choice==3:
#         print("scrum")
#     else:
#         print("no entry")
# emp_check(4)
# emp_check(1)

# #nested if else statements
# num1=int(input("enter the first number:"))
# num2=int(input("enter second number:"))
# if num1>=num2:
#     if num1==num2:
#         print("both numbers are equal!!")
# #    else:
# #       print("number1 is greater than num2")
# else:
#     print("num1",num1, "is smaller than num2 ",num2)

# number=10
# mynumber=int(input("enter the number:"))
# if mynumber>10:
#     print("exponent is: ",mynumber**2)
# else:
#     print("number is less than 10")

# def emp(dept):
#     if dept=='it':
#         print("supporter")
#     elif dept=='python':
#         print("data scientist")
#     elif dept=='java':
#         print("java developer")
#     else:
#         print("bench mutyam")

# emp("ciber security")

# father="narayana"
# son=input("enter son's name:").lower()
# # if son=="suresh" or son=="mahesh" or son=="murali":
# #     if son !="suresh" or son !="mahesh" or son !="murali":
# #         print("he is not ",father ,"son")
# #     print("he had relation")
# # else:
# #     print("he is not relative")

# if son=="suresh" or son=="mahesh" or son=="murali": print("he is ",father,"'s son")
# else: print("other relation")

#for loop , using f'strings in input
# name=input("enter your name:")
# sentence=f"my name is, {name}"
# for item in sentence:
#     print(item,)

#using nested for loop
# names=['suresh','mahesh']
# for i in names:
#     for j in i:
#         print(j,)
#     print(i ,'\n')

#sum of first 10 numbers
# sum=0
# number=0
# while number<=10:
#     sum+=number
# #    print(sum)
#     number+=1
# print(sum)

#using break to exit from loop if condition false
# for number in range(10):
# #    print(number)
#     if number>=7:
#         print("stop processing")
#         break
#     print(number)

# #using continue statement in python
# for num in range(3,8):
#     if num==5:
#         continue
#     else:
#         print(num)
# print(type(num))
# print(type(num).__name__)

# while 1<2:
#     break

# for i in range(10):
#     print(i)

#print sum of even numbers from 2 to 20
# sum=0
# for item in range(21):
#     if item%2==0:
#         sum+=item
# print(sum)
# #another way
# sum=0
# for i in range(0,22,2):
#     sum+=i
# print(sum)

# #finding sqares of a numbers in a sequence
# numbers=[32,9,38,84,21]
# for i in numbers:
#     print("squares of numbers :",i**2)

# #find average of numbers in list
# numbers=[20,67,53,153,167]
# sum=0
# for i in numbers:
#     sum+=i
# total_numbers=len(numbers)
# average=sum//total_numbers
# print(sum)
# print(f"average of numbers in list is = {average}")

# for i in range(11):
#     if i%2==0:
#         print("number is even:",i)
#     else:
#         print("number is odd:",i)

# #Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
# for i in range(9,51):
#     if i%2==0:
#         print(i)

# list1=[1,3,5,6,8,4,2]
# list1.sort()
# for i in list1:
#     print(i)
#     if i>=6:
#         break

# name="sureshuiegrfebfksnxscjfhfdjvbns"
# count=0
# for i in name:
#     if i !='s':
#         continue
#     else:
#         count+=1
# print(count)

# nums=(1,2,3,4,5,6)
# for i in nums:
#     print(i)
#     if i>=3:
#         pass

# for i in range(5):
#         print(i)
# else:
#     print("loop completed")

#print first 2 numbers of loop
# count=0
# for i in range(1,6):
#       count+=1
#       if count>2:  # first 2 iterations will false . so else block will be executed
#         break  
#       else:
#         print(i)
# else:
#      print("done")  # else block wont executes when if statement true, break will exits the loop.

# #reverse for loop using reversed()
# list1=[10,20,30,40,'suresh']
# for i in reversed(list1):
#     print(i)

#reverse for loop using range()
# print("printing numbers in reverse order")
# num=5
# for num in range(num,-1,-1):
#     print(num)

# #reversing a sequence using loop
# numbers=[1,2,3,4,5,6,7]
# for i in numbers[::-1]:
#     print(i)

# names=['a','b','c','d']
# for i in names[::-1]:
#     print(i)
# print(type(names).__name__)

#nested for loops
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print('')

# rows=6
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print("suresh",end=' ')
#     print(' ')

#using a while loop in for loop
# for i in range(1,10):
#     print("multiplication table of ",i)
#     count=1
#     while count<11:
#         print(f"{i}*{count}={i*count}")
#         count+=1
#     print('\n')

# num=[1,3,5,7,9,11]
# even=[i+1 for i in num if i%2==1]
# print(even)

# name="my name is suresh .i live in bangalore"
# for word in name.split():
#     print(word)

# numbers = [1, 2, 3, 6, 7]
# size=len(numbers)
# for i in range(size):
#     print(numbers[i])

# mine='suresh'
# number='23'
# for i in number:
#     print(i)

# #one line for loop
# [print(i) for i in numbers]

# set={}
# print(type(set))

#for loop using dict
# dict1={'a':'apple','b':'ball','c':'cat'}

# #iterate only keys and print
# for ke in dict1:
#     print(ke)
# for values in dict1:
#     print(values)

# #iterate keys and print keys along with values using key-value as dict1[keys]=value
# for keys in dict1:
#     print(keys,'->',dict1[keys])

# #iterate only values
# for i in dict1.values():
#     print(i)

# for i in range(5):
#     for j in range(5):
#         print(1 if (i + j) % 2 == 0 else 0, end=" ")
#     print()

# dict={"Id":1, "Name":"John", "Location":"Chennai", "Age":22}
# for key in dict:
#     print(key, "is", dict[key])

#find second largest number in list
# def sec_large(list1):
#     if len(list1)<2:
#         return "sequence must contains atleast 2 unique numbers"
#     unique_nums=list(set(list1))
#     unique_nums.sort(reverse=True)
#     return unique_nums[1] if len(unique_nums)>1 else "no second highest number"
# print(sec_large([10,20,40,23,65,12]))
# print(sec_large([1000]))

# def sec_large(list1):
#     if len(list1)<2:
#         return "sequence must contains atleast 2 unique numbers"
#     unique_nums=list(set(list1))
#     unique_nums.sort(reverse=True)
#     return unique_nums[1]
# print(sec_large([10,20,40,23,65,12]))
# from collections import Counter   # using counter from collections because .counter() will go through sequence multiple times & increase time complexity
# def word_count(sentence):
#     words=sentence.lower().split()
#     total_words=Counter(words)
#     return total_words
# sentence='my name is my name.and this is me.me is mine'
# #sentence.replace('.','')
# print(word_count(sentence))

# from collections import Counter

# def word_count(sentence):
#     words = sentence.lower().split()  # Convert to lowercase and split into words
#     word_freq = Counter(words)  # Count occurrences of each word
#     return word_freq

# Example usage:
# sentence = "This is a test. This test is only a test."
# sentence = sentence.replace(".", "")  # Remove punctuation
# print(word_count(sentence))

# def reverse_string(s):
#     chars=list(s)
#     n=len(chars)
#     for i in range(n//2):
#         chars[i],chars[n-i-1]=chars[n-i-1],chars[i]
#     return "".join(chars)
# s="suresh here"
# print(reverse_string(s))

#how many times a number divisible by 3 before it turns less than 10
# count=0  #to find count, initiated a variable
# number=int(input("enter your number"))
# while number>10:
#     number=number/3
#     count+=1
# print(count)

# number=int(input("enter the number:"))
# while number<100 or number>500:
#     print("enter your numbers between 100 to 500")
#     number=int(input("enter your number"))
# else:
#     print("number is correct",number)

#using if-else in while loop
#printing even and odd numbers from 0 to user given number
# number=int(input("enter your number"))
# while number>0:
#     if number%2==0:
#         print("even number:",number)
#     else:
#         print("odd number",number)
#     number-=1

# name='suresh18rayapati'
# size=len(name)
# i=0
# while i<size:
#     if name[i].isdecimal():
#         i+=1  # use i+=1 inside loop to increase i in loop. otherwise i value wont increase causes infinite loop
#         continue
#     print(name[i])
    # i+=1


# name='suresh18rayapati'
# size=len(name)
# i=-1
# while i<size-1:
#     i=i+1
#     if not name[i].isalpha():
#         continue
#     print(name[i])

# rows=6
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(' ',end="")
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

#
# n=4
# while n<0:
#     print(n)
#     n-=1
#     pass

# i=1
# while i<5:
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
#     i+=1

# i=1
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("execution done")


# i=1
# while i<5:
#     print(i)
#     if i==3:
#         break
#     i+=1
# else:
#     print("done loop")  # else block wont execute. because break statement will skip exits the loop

#reverse while loop
# i=10
# while i>1:
#     print(i)
#     i-=1
# names=['suresh','murali','mahesh']
# for i in names:
#     print(i)
# size=len(names)
# i=0
# while i<size:
#     print(names[i])
#     i+=1


# name = "Jessa"
# i = 0
# res = len(name)-1
# while i <= res:
#     print(name[i])
#     i = i + 1

# #excercises
# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)

# for num in range(-2,-5,-1):
#     print(num, end=", ")

# for l in 'Jhon':
#    if l == 'o':
#       pass
#    print(l, end=", ")

# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(x)

# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break
# x = 0
# while (x < 100):
#   x+=2
#   print(x)
# print(x)

#while loop excercises
# i=0
# while i<11:
#    print(i)
#    i+=1

# rows=6
# for i in range(1,rows):
#    for j in range(1,i+1):
#       print(j,end=' ')
#    print()

# number=int(input("enter number:"))
# sum=0
# for i in range(number+1):
#    sum+=i
# print('sum is',sum)
# number=int(input("enter number:"))
# print("multiplication of number:",number)
# for i in range(1,11):
#         print(f"{number}X{i}={i*number}")
#         i+=1
# print()

# numbers = [750,12, 75, 150, 180, 145, 525, 50]
# numbers.sort()
# divisibles=[]
# for i in numbers:
#         if i>500:
#                 break
#         elif i>150:
#                 continue
#         elif i%5==0:
#                 divisibles.append(i)
# print(divisibles)


# number=78965
# numbers=str(number)
# print(type(number))
# count=0
# for i in numbers:
#         count+=1
# print(count)

# number=100000
# count=0
# while number!=0:
#         number=number//10
#         count+=1
# print(count)

# 
# rows=6
# k=5
# for i in range(0,rows+1):
#         for j in range(k-i,0,-1):
#                 print(j,end=' ')
#         print()

# rows=5
# for i in range(1,rows+1):
#         print(' ' * (rows-i)+ '*' * (2* i-1))

# #diamond pattern
# rows=6
# for i in range(1,rows+1):
#         print(" " * (rows-i) + '*' * (2*i-1)) 
# for i in range(rows-1,0,-1):
#         print(" " * (rows-i) + '*' *(2*i-1))

# rows=8
# columns=8
# for i in range(rows):
#         for j in range(columns):
#                 if(i+j)%2==0:
#                         print('X',end=' ')
#                 else:
#                  print('O',end=' ')
#         print()

# reversing a list items
# list1 = [10, 20, 30, 40, 50]
# size=len(list1)
# for i in range(size-1,0,-1):  # size-1 is because index starts from 0
#     print(list1[i])

# list2=reversed(list1)  # list is mutable
# for i in list2:
#     print(i)

# i=-10
# while i<0:
#     print(i)
#     i+=1

# for i in range(-10,0,1):
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print("done")

# start=25
# end=50
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i==0):
#                 break
#         else:
#             print(num)

# name='suresh'
# print(hash(name))
# print(id(name))

# a=[10]
# b=[20]
# print(f"{a=},{b=}")
# dico=dict(zip(a,b))
# print(dico)

#finding duplicates in List

# list1=[2,4,2,5,89,5,77,25,77]
# uniques=[]
# duplicates=[]
# #size=len(duplicates)
# for i in list1:
#     if i not in uniques:
#         uniques.append(i)
#     else:
#         duplicates.append(i)
# size=len(duplicates)
# print(duplicates,'count is',size)
# print(uniques)
# print(size)
# number=76542
# reverse_number=0
# while number>0:
#     remainder=number%10
#     reverse_number=(reverse_number*10)+remainder
#     number=number//10
# print(reverse_number)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# odd_list=[]
# size=len(my_list)-1
# for i in range(0,size+1):
#     if i%2==1:
#         odd_list.append(my_list[i])
# print(odd_list)
# for j in my_list[1::2]:
#     print(j,end=' ')

# for i in range(1, 11):
#     print('Multiplication table of', i)
#     for j in range(1, 11):
#         # condition to break inner loop
#         if i > 5 and j > 5:
#             break
#         print(i * j, end=' ')
#     print('')

# for i in range(4):
#     for j in range(4):
#         if j == i:
#             break
#         print(i, j)

# first = [2, 3, 4]
# second = [20, 30, 40]
# final = []
# for i in first:
#     for j in second:
#         final.append(i+j)
# print(final)

# first=[2,3,4]
# second=[20,30,40]
# final=[i+j for i in first for j in second]
# print(final)

# combined=[[x,y] for x in [10,20,30] for y in [100,200,300] if x!=y]
# print(combined)

# i=1
# while i<=5:
#     j=1
#     while j<=10:
#         print(j,end=' ')
#         j+=1
#     i+=1
#     print('\n')

# print('Show Perfect number fom 1 to 100')
# n = 2
# # outer while loop
# while n <= 100:
#     x_sum = 0
#     # inner for loop
#     for i in range(1, n):
#         if n % i == 0:
#             x_sum += i
#     if x_sum == n:
#         print('Perfect number:', n)
#     n += 1

#optimizing way to find perfect number
# print('Show Perfect numbers from 1 to 100')

# for n in range(2, 101, 2):  # Only check even numbers
#     x_sum = sum(i for i in range(1, n) if n % i == 0)  # Find sum of divisors
#     if x_sum == n:
#         print('Perfect number:', n)

# f=open("C:\Users\komir\OneDrive\Desktop\file_handling\hello",mode='r')
# information=f.read()
# f.close()

# def add(num1,num2):
#     return num1+num2
# print(add(10,40))

# result=lambda number1,number2,number3:number1+number2*number3
# print(result(2,5,3))

# list1=[10,20,30]
# list2=[1,2,3]
# list3=lambda list1,list2:list1 * list2  # lambda will give results based on condition
# print(list[list3])

# list4=[1,2,3,4,5,6,7,8,9,11,12]
# result=filter(lambda num:num**2,[1,2,3,4,5,6,7,8,9,11,12])
# print(list(result))

# results=map(lambda i:i**2,list4)
# print(list(results))  # in filter ,iterable data will transform and prints results

# #taking multiple lines as input from user
# data=[]
# print("tell me about yourself")
# while True:
#     my_data=input()
#     if my_data:
#         data.append(my_data)
#     else:
#         break
# print("my biography is")
# print('\n'.join(data))
name=eval(input("enter your name:"))
print(name)
print(type(name))