# Method:- read()

f = open("hi.txt",'r')
a = f.read(4)  # read the first 4 data
print("A read",a)
f.read(4)  # read the next 4 data

f.read()   # read in the rest till end of file
c = f.read()   # further reading returns empty string
print(c)

# readline() and readlines()

with open('hi.txt','r') as f:
    a = f.readline()
    print(a)
    b = f.readline()
    print(b)
    
    
with open("hi.txt",'r') as f:
    s = f.readlines()
    print(s)