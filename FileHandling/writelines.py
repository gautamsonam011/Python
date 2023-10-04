# Method:-writelines()

lis = ["Welcome","to","here","Delhi"]
with open("hi.txt",'w') as f:
    f.writelines("%s\n" %l for l in lis)
    
# Method:- writelines() with 'a+' mode  this can override file on writelines mode

fruits = ["\nOrange\n","Banana\n","Apple\n"]
new_file = open("hi.txt",mode = "a+",encoding="utf-8")
new_file.writelines(fruits)
new_file.close()

# Method:- writelines() with append

f = ["\nHi\n","Fruits\n","Food\n"]
a = open("hi.txt","a+")
a.writelines(f)
a.close()


