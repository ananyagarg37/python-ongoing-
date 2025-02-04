# a spam comment is define as text containing following keyboard , "make a lot of money " , "buy now ", "subscribe this " , "click this ".write a programm to detect these  spam.
p1 = "make a lot of money" 
p2 = "buy now"  # first i write p2 = "buy now " here i gave space at last that why its not detecting in prgramm
p3 = "subscribe this"
p4 = "click this "

message = input("entre your comment :")

if((p1 in message) or (p2 in message) or( p3 in message) or( p4 in message )):
    print("this is spam")
else :
    print("this is not spam")