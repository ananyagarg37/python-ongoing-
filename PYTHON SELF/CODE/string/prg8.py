# write a programm to fill in a letter template given below with name and date .

letter  = """
       dear <|name|>
       you are selected 
       <|date|>
           """
print(letter.replace("<|name|>" , "huhu").replace("<|date|>", "24 septermber 2045"))
# this is called chaining . isme pehle first string ko replace kiya uske bad usi mai 2nd string ko replaced kar diya