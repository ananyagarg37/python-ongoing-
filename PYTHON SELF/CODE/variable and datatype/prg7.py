#  type function and type casting 
a = 30
t = type(a) #class int
print(t)

a = 30.7
t = type(a) #class float
print(t)

a = "khikhi"
t = type(a) #class string(str)
print(t)

a = "30.7" #any value in double "" consider as string 
t = type(a) #class str
print(t)

a = "30.7"
# fun to change this str into float 
b = float(a)
t = type(b)
print(t)

