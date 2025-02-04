# tuple methods
a = (3 , 6 , "rohan" , False  , 3456)
print(a)

# count tuple
q = a.count(3)
print(q)

# index tuple
b = a.index("rohan")
print(b)

# maximum and minimum
c = (1,2,3,4,5,6,7,8)
print(max(c))  
print(min(c))

# sum of tuple element
print(sum((1, 2, 3)))  

# converting into tuple
d = [1,2,3,4,5,6]
e = tuple(d)
print(e)
print(type(e))

# tuple membership 
my_tuple = (10, 20, 30)
print(20 in my_tuple)   
print(40 not in my_tuple)  

# concatination and repetition
# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  

# Repetition
print(t1 * 3)  

# unpacking tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  




