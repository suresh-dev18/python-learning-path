# from PIL import Image
# original_image= "Prabhas.jpg"
# Image.open(original_image)

# img=Image.open(original_image)
# mirror_image=img.transpose(Image.FLIP_LEFT_RIGHT)
# mirrored_image='prabhas_new.jpg'
# mirror_image.save(mirrored_image)
# Image.open(mirrored_image)


# from PIL import Image

# original_image = r"C:\Users\komir\Downloads\Prabhas.jpg"

# # Open original image
# img = Image.open(original_image)

# # Create mirrored image
# mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)

# # Save mirrored image
# mirrored.save("prabhas_new.jpg")

# # Display mirrored image
# mirrored.show()

# import os
# print(os.getcwd())
# n=int(input("enter the number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"factorial of number {n} is {fact}")
4

# Factorial using loop

# n = int(input("Enter a number: "))
# fact = 1

# for i in range(1, n + 1):
#     fact *= i   # multiply fact by i each time

# print(f"Factorial of {n} is: {fact}")

# Factorial using recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print(f"Factorial of {n} is: {factorial(n)}")


# import math
# print(math.factorial(int(input("Enter a number: "))))

# l=[10,20,30,40,50]
# #print(l[-4:-1])
# print(l[-1:-4:-1])

# l1=[i for i in range(1,11) if i%2==0]
# print(l1)

# tup=tuple([10,20,30,40,50])
# print(tup)
# print(tup.count(20))
# print(tup.index(50))

# a=[[],[]]*2
# print(a)
# a[0].append(7)
# print(a)

def prime(n):
    if n==0 and n==1:
        print("not prime")
    elif n>1:
        flag=1
        for i in range(2,n):
            if n%i==0:
                flag=0
                break
        if flag==0:
            pass
        else:
            print("prime number",n)

# for number in range(20,51):
#     if prime(number):
#         print("prime numbers:",number)
#     else:
#         pass
# prime(23)
# prime(18)

def fact(n):
    if n<2:
        return 1
    else:
        return n * fact(n-1)
#print(fact(6))

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#print(fib(9))

def sumis(n):
    sum=0
    for i in range(1,n+1):
        sum+=i*i
        return sum
print(sumis(9))