# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
# multiplication=num1 * num2
# addition= num1+num2
# if num1<0 or num2<0:
#     pass
# #    print("please enter positive number!")
# elif multiplication>=1000:
#     print(f"the addition of 2 numbers is {addition}")
# else:
#     print(f"product of numbers is {multiplication}")

#2.Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number
# previous=0
# for i in range(11):
#     sum=previous+i
#     print(f"current number is {i} , previous number is {previous}. their sum is = {sum}")
#     previous=i # if need cummulative sum  'sum+=i'

#3.Write a Python code to accept a string from the user and display characters present at an even index number.
# my_string=input("enter your string:")
# even_str=my_string[::2]
# print(even_str)

#anothe way
# str1=input("enter your text:")
# even_place=[]
# for i in str1[::2]:
#     even_place.append(i)
#     print(even_place)

#another way
# word=input("enter text:")
# even=list(word)
# for i in even[::2]:
#     print(i)

#4.Write a Python code to remove characters from a string from 0 to n and return a new string
# text=input("enter your text:")
# n=int(input("enter number to slice upto:"))
# if n>len(text):
#     print(f"please enter n value less than {len(text)}")
# else:
#     print(text[n:])

#5. Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# if numbers_x[0]==numbers_x[-1]:
#     print(True)
# else:
#     print(False)

#using functions
# def first_last_same(num_list):
#     first=num_list[0]
#     last=num_list[-1]
#     if first==last:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print(first_last_same(numbers_x))
# numbers_y = [75, 65, 35, 75, 30]
# print(first_last_same(numbers_y))

#6.Write a Python code to display numbers from a list divisible by 5
# my_list=[10, 20, 33, 46, 55]
# for i in my_list:
#     if i%5==0:
#         print(i)

#7.Write a Python code to find how often the substring “Emma” appears in the given string
# str_x = "Emma is good developer. Emma is a writer"
# if 'Emma' in str_x:
#     print(f"emma repeated {str_x.count('Emma')} times")

# l=[1,1,2,3]
# print(l.count(1))

# for number in range(6):
#     for i in range(number):
#         print(number,end=" ") # 0 wont print here.cause outer loop 0 times run. inner loop wont print anything
#     print("\n")

# for num in range(6):
#     for j in range(1,num+1):
#         print(j,end=' ')
#     print()

# rows=5
# b=0
# for i in range(rows,0,-1):#step=-1 because i want to print it in number of times as decrement
#     b+=1 #im increasing it by 1 for each turn of loop
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# sr='james bond'
# print(sr[2::-1])
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)

# var = "James" * 2  * 3
# print(var)

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

nums=[100,200,300,400]
for i in range(len(nums)-1,-1,-2):
    print(nums[i])

s={12,13}
s1={14,15}
print(s<s1)
