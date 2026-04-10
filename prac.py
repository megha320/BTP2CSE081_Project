# Design a program to store a patient's name and age in a dictionary—print patients whose age is more than 60.
# my_dic = {}
# n = int(input("Enter no. of data which you want to enter: "))

# for i in range(n):
# 	name = input("Enter patient's name: ")
# 	age = int(input("Enter her/his age: "))
# 	my_dic[name] = age
# print(my_dic)

# for name, age in my_dic.items():
#     if age > 60:
#         print(name, age)
# check = lambda x: "Even "if x %2 == 0 else "Odd"
# num = int(input("Enter a number: "))
# print(check(num))



# check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# num = int(input("Enter a number: "))
# print("The number is", check_even_odd(num))



# Write a program to print values in a dictionary
# dict = {"Name" : "Megha", "Age" : 18, "Gender" : 'F', }
# print(dict.keys())
# print(dict.values())



# Show how reverse indexing works on a tuple
# tup1 = (1,2,3,4,5)
# print(tup1[ : : -1])


# Write a program to print all the elements of a list in reverse order using a looping statement.
# lst = [1, 2, 3, 4 ,5]
# lenn = len(lst)
# for i in range(lenn -1, -1, -1):
# 	print(lst[i], end = ' ')

# Write into file
f = open("demo.txt", "w")
f.write("Hello Megha!\n")
f.write("This is file handling in Python.")
f.close()

# Read from file
f = open("demo.txt", "r")
content = f.read()
print("File content:")
print(content)
f.close()
