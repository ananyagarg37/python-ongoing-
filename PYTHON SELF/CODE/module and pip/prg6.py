# to list directory path
#first import os module - in built module
import os
#define directory which list you wanna show
directory_path="/"
# use os module to list the contents
contents=os.listdir(directory_path)
# to print list 
print(contents)