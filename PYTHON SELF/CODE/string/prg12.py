# upper and lower case = str.upper or str.lower
text = "Hello"
print(text.upper())
print(text.lower())

# str.split used to split string as list with default space 
text = "apple,mangoes,banana"
print(text.split(","))

# to check string is numeric , alphabetic or alphanumeric 
text = "1234"
print(text.isdigit()) # to check string is numeric 

text = "abcd"
print(text.isalpha()) #to check string is numeric

text = "abc1234" # or 1234acboc same output
print(text.isalnum()) #to check string is alphanumeric


