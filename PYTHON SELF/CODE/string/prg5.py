# string functions
name = "ananya"
print(len(name)) # to calculate length of string

print(name.endswith("ya"))
# it use to see whether fun end with given condition or not

print(name.startswith("an"))
#use to see whether fun start with given condition...

print(name.startswith("An"))
#alphabet matters . small a is diff from big A

print(name.capitalize())
#can say make first letter capital..like if its ananya are it only make A in ananya capital only not are 

s = "hello world "
index = s.find("world")
print(index)
# yeh dekhega world konse index par hai space also count iska output 6 hai kuki world 6th index se start hai

replaced_string = s.replaced("world" , "python")
print(replaced_string)
# replaced old word with new word . it take all occurances...