# dic method 
marks ={
    "harry" : 89 ,
    "sambal" : 55,
    "mike" : 33 ,
}

# item method
print(marks.items()) #these item of dictionary given in proper list and in tuple form

# key method
print(marks.keys())

# update method 
marks.update({"harry":99 , "renuka" : 88}) #change happen in original dictionary too coz dic are mutable amd it also add new key 

print(marks)

# get method 
print(marks.get("harry")) 
# its show none if key no present in dictionary
print(marks.get("shubhiu"))


 