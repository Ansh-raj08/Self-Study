# DATA TYPE CHECK
# innt = 5.5
# print(type(innt))

# DATA TYPE CONVERSION
# num = 5 
# convnum = float(num)
# print(type(convnum))
# print(convnum)
# stri = "123"
# constr = int(stri)
# print(type(constr))

# gemini

# a = 5
# total_sum = 0

# for i in range(1, a+1):
#     total_sum = total_sum + i

# print(total_sum)

# Reverse the digits

# n = 12345
# r = 0

# while n > 0:
#     last_digit = n % 10
#     r = r * 10 + last_digit
#     n = n // 10
# print(r)

# Even no. counter
# sam = [1,2,3,4,5,6,7,8,9,10]

# for num in sam:
#     if num % 2 == 0:
#         print(num)

# To print 1 to 100 using while loop
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# reverse countdown problem
# n = 100
# while n >= 0:
#     print(n)
#     n -= 1

# Factorial calculator [Ex. 5! = 5x4x3x2x1]
# N = int(input("Enter Number: "))
# fact = 1
# while N >= 1:
#     fact = fact * N
#     N -= 1
# print(fact)

# FizzBuzz Logic: Loop from 1 to 20.
# If the number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number.
N = 1
while N <= 20:
    if (N % 3 == 0) and (N % 5 == 0):
        print(f"{N} is FizzBuzz")
    elif N % 5 == 0:
        print(f"{N} is Buzz")
    elif N % 3 == 0:
        print(f"{N} Fizz")
    else:
        print("Nothing")
    N += 1