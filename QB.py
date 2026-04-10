# 1 - WAP to swap two numbers without using a third variable. 
# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# a, b = b, a
# print("Number1: ",a)
# print("Number1: ",b)

# 2 - WAP to check whether a given number is even or odd. 
# n = int(input("Enter a number: "))
# if(n%2==0):
#     print(n, "is an Even number")
# else:
#     print(n, "is an Odd number")

# 3 - WAP to find the sum of two numbers entered by the user.
# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# sum = n1 + n2
# print("Sum of", n1, "and", n2, "is:", sum) 

# 4 - WAP to calculate the area of a circle given its radius. 
# r = float(input("Enter Radius:"))
# aoc = 3.14*((r)**2)
# print("Area of Circle:", aoc)

# 5 - WAP to find the largest of three numbers entered by the user.
# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# n3 = int(input("Enter number3: "))
# if(n1>n2):
#     if(n1>n3):
#         print(n1, "is largest")
#     else:
#         print(n3, "is largest")
# elif(n2>n1):
#     if(n2>n3):
#         print(n2, "is largest")
#     else:
#         print(n3, "is largest")


# 6 - WAP  to check if a given year is a leap year. 
# y = int(input("Enter a year:"))
# if(y%4 == 0):
#     if(y%100 == 0):
#         if(y%400 == 0):
#             print(y,"is a leap year.")
#         else:
#             print(y,"is a not a leap year.")
#     else:
#         print(y,"is a leap year.")
# else:
#     print(y, "is not a leap year.")



# 7 - WAP  to count the number of vowels in a given string.
# str = input("Enter a string: ")
# count = 0
# for i in str:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             count = count+1
# print("Number of vowels are:", count)

# # 8 - WAP to reverse a string entered by the user.
# str = input("Enter a string: ")
# rev = str[ : :-1]
# print("REVERSE OF", str, "IS:", rev)
# # USING FOR LOOP
# str = input("Enter a string: ")
# rev = " "
# for i in str:
#     rev = i + rev
# print(rev)

# 9 - WAP to find the square and cube of a number. 
# n = int(input("enter a number:"))
# sq = n**2
# cube = n**3
# print("Square of", n, "is:", sq)
# print("Cube of", n, "is:", cube)

# 10 - WAF to calculate the factorial of a given number using recursion.
# USING FUNCTION
# def fact(n):
#     fact = 1
#     for i in range(1, n+1): # we take range 1 to n+1 because, python always take 1 less 
#         fact = fact * i
#     print(fact)
# fact(6)
# # USING RECURSION
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return(n*fact(n-1))
# print(fact(6))

# 11 - WAP  to generate the Fibonacci series up to n terms. 
# n = int(input("Enter number:"))
# if(n<=0):
#     print("Please, enter positive number.")
# elif(n==1):
#     print("Fibbonacci sequence:")
#     print(0)
# else:
#     print("Fibbonacci sequence:")
#     a, b = 0, 1
#     for _ in range(n): # we use this when we use to repeat a block of a specific
#         print(a)
#         a, b = b , a+b

# 12 - WAP to check if a given number is a prime number. 
# n = int(input("Enter number:"))
# if(n<=0):
#     print(n, "is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5)+1):
#         if(n%i == 0):
#             is_prime = False
#     if is_prime:
#         print(n, "is a prime number.")
#     else:
#         print(n, "is not a prime number.")

# 18 - WAP to sort a list of numbers in ascending order. 
# lst = input("Enter elements:").split()
# sort = sorted(lst)
# print(sort)

# # 15 - WAF to check if a given string is a palindrome. 
# str = input("Enter string:")

# if str == str[::-1]:
#     print("yes")
# else:
#     print("no")

# # 16 - WAP to count the occurrences of each character in a string.
# str = input("Enter string:")
# freq = {}
# for i in str:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1
# print(freq)

