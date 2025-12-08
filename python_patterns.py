#print number of stars in same line
# n=int(input("enter n value:"))
# for i in range(n):
#     print('*',end=' ')

#square pattern like 3x3,4x4
# n=int(input("enter n value:"))
# for i in range(n):
#     print(n*'* ',)

#square pattern with same number of rows number
# n=int(input("enter no of rows:"))
# for i in range(n):
#     print((str(n)+' ')*n)

# #square pattern each row with its count
# n=int(input("enter no of rows:"))
# for i in range(n):
#     print((str(i)+' ')*n)

# n=int(input("enter no of rows:"))
# for i in range(n):
#     print((str(i+1)+' ')*n)

# n=int(input("enter n value:"))
# for i in range(n):
#     print('s '*n)

#using chr to print sequential alphabet characters
# n=int(input("enter n:"))
# for i in range(n):
#     print((chr(65+i)+' ')*n)

# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(n):
#         print(str(j+1),end=' ')
#     print()

#square pattern in ascending order
# n=int(input("enter n value:"))
# for i in range(n):
#         print((str(i+1)+' ')*n)

#square pattern in descending order
# k=int(input("enter k value:"))
# for i in range(k):
#         print((str(k-i)+' ')*k)

#print square pattern with alphabets in descending order or reverse
# n=int(input("enter n value:"))
# for i in range(n):
#     print(str(chr(65+n-i)+' ')*n)

# n=int(input("enter n value:"))
# for i in range(n):
#     print(str(chr(64+n-i)+' ')*n)
#     print(str(chr(64+n-i)+' ')*n)
#     print(str(chr(64+n-i)+' ')*n)

# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(n):
#         print(n-j,end=' ')
#     print()

#printing alphabets in reverse order in each row
# n=int(input("enter n value:")) 
# for i in range(n):
#     for j in range(n):
#         print(str(chr(64+n-j)+' '),end=' ') #here printing j as element in reverse or reducing
#     print()

#printing triangle patterns
#1. right angle trianle
# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

#2.right angle triangle pattern with ascending numbers
# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=' ') #
#     print()

# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=' ') #printing (i+1) because same number want to print in each row
#     print()

#same above pattern without nested loop since same element in each row
# n=int(input("enter n value:"))
# for i in range(n):
#     print((str(i+1)+' ')*(i+1))

#right angle triangle with same characters in each row
# n=int(input("enter n value:"))
# for i in range(n):
#     print(str(chr(65+i)+' ')*(i+1)) #pattern is increasing by (i+1) times, so multiplied with same

#right angle triangle with increasing alphabets 
# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end=' ')
#     print()

#right angle triangle with numbers in descending order(4 to 1)
# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=' ')
#     print()

#right angle triangle with characters in descending order(d to a)
# n=int(input("enter n value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(str(chr(64+n-j)),end=' ')
#     print()

#inverted/reversed right angled triangle
# n=int(input("enter n value:"))
# for i in range(n):
#     print('* ' *(n-i)) #using 1 loop because same * is printing element in each row

# #printing right angled triangle opposite each other
# n=int(input("enter n value:"))
# for i in range(n):
#     print('* ' *(n-i)) #using (n-i) in loop because no difference in printing element
# for j in range(n):
#     print('* '*((j+1))) #increasing no of *'s as (j+1) times

#print inverted right angled triangle in ascending order with numbers
# n= int(input("enter n value:"))
# for i in range(n):
#     #print((str(i+1)+' ')*(n-i))
#     print(((str(i+1)+' ')*(n-i)))

#printing inverted right angle triangle with same element in each row
# n=int(input("enter n value:"))
# for i in range(n):
#     print(str(chr(65+i)+' ')*(n-i)) #element--chr(65+i), how many times --(n-i) because reducing as inverted triangle

#inverted right angled triangled in descending order
# n= int(input("enter n value:"))
# for i in range(n):
#     print((str(n-i)+' ')*(n-i))

# n= int(input("enter n value:"))
# for i in range(n):
#     print((str(i+1)+' ')*(n-i))

import virtualenv

def gen():
    for i in range(3):
        yield i
g=gen()
list1=[x for x in g]
list2=[x for x in g]
print(list1)
print(list2)

def make_funcs():
    funcs=[]
    for i in range(3):
        funcs.append(lambda:i)
    return funcs
f1,f2,f3=make_funcs()
print(f1(),f2(),f3())  #all will print 2 because lambda captures by reference not by value