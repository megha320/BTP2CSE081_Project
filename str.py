str = input("Enter a String : ")
print(str)

#operations on string

# 1--> indexing and slicing
str[0]
str[0:11:2]
# 2--> concatenation 
str1 = "Python"
str2 = "Programming"
strr = str1 + str2
print(strr)
# 3--> replication
print(str*3)
# # 4--> membership operator 
print("a" in "Megha")
print("s" not in "Megha")
print("s" not in "Manshi")
print("a" in "Manshi")


# in-built functions 
len(str)

str.isalnum() # checking that is there any alphabetic or digit present in the string
str.isalpha() # checking that is there any alphabet present in the string
str.isdigit() # checking that is there any digit present in the string
str.isspace() # checking that is there only whitespace in the string 
str.islower() # checking that is there only small alphabets present in the string
str.isupper() # checking that is there only capital alphabets present in the string
str.istitle() # checking that is there only First letter of the string is in capital

str.capitalize() # return the string with its first letter capital.
# ex - megha harbola --> Megha harbola
str.lower() # return the all characters of the string in small letter
str.upper() # return the all characters of the string in Capital letter
str.title() #return the string with its first letter capital after a space 
# ex - megha harbola --> Megha Harbola
str.split()
# ex - megha harbola --> ['megha', 'harbola']
str.swapcase() # swap capital letter to small letters and small letters to capital letters
str.lstrip() # remove all whitespace from left side
str.rstrip() # remove all whitespace from right side

str.partition()
list(str)