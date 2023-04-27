#   Re-uasability
#   clean, reliable and light weight
#   Recurrsive functions.

"""
def add():
    a = input()
    b = input()
    c = a + b
    print(c)

add()
"""


"""
def add():
    try:
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    print(a+b)

add()
"""



"""
check  out the link:

https://github.com/meh-sudhanshu/RGM

"""
"""
def addNumber(a,b):
    return a+b


sum = addNumber(10,30)


def returnMultipleValues():
    return 10,20,30

output = returnMultipleValues()
print(output)
"""




#   fibonacii series 0,1,1,2,3,5,8,13,21,34,55,89,144,....

"""
def fibonacii(n):
    if n <= 1:
        return n                                               #    Wrong Answer
    else:
        return (fibonacii(n-1) + fibonacii(n-2))

n=int(input(" Enter the number:"))
print(fibonacii(n))

"""

#  Factorial of a number by sir


"""

def printFibonacciSequence(n):
    if n<=0:
        print("Invalid input")
        return -1
    if n==1:
        print(0)
        return -1
    if n==2:
        print(0," ",1)
        return -1
    a=0
    b=1
    print(a," ",b)
    count=3
    while count<=n:
        next = a+b
        print(next,end = " ")
        a=b
        b=next
        count=count+1

printFibonacciSequence(10)

"""

            #   LCM of two numbers

"""
def lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def hcf(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+1):
        if a%i == 0 and b%i == 0:
            hcf = i
    return hcf


a=int(input(" Enter the first number:"))
b=int(input(" Enter the second number:"))

lcm = lcm(a,b)

print(lcm)

hcff=int(hcf(a,b))

print(hcff)


"""




         #   Trace the code below

"""
def do(n):
    if(n<=5):
        return
    do(n-1)
    print(n)
    do(n-1)
    print(n)
do(8)

"""

#                            towers of Hanoi code

                #source, helper, designation.
