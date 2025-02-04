# find greatest of four number enter by user .
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a>b and a>c and a>d) :
    print("a greatest")
elif ( b >a and b > c and b>d ) :
    print("b greatest")
elif (c>a and c>b and c>d):
    print("c greatest ")
else:
    print("d greatest")
