import pickle

# pickling

list = ['python','php',"js",'java']
with open('hi.txt','wb') as h:
    pickle.dump(list,h)
    
# Unpickling


with open("hey.txt",'rb') as h:
    a = pickle.load(h)
print(a)