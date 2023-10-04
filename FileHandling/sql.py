import sqlite3

con = sqlite3.connect("hello.db")
# print("DB is Connected....")
# Create table--->

cur = con.cursor()

# cur.execute("create table Product(p_id INTEGER PRIMARY KEY AUTOINCREMENT,p_name Text NOT NULL,price REAL,quantity INTEGER)")

# print("Table is created...")

# Insert Data in table --------->

# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('AutoCAD',200,20)");
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Quick Hill',330,12)");
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Keyboard',250,25)");
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Mouse',150,34)");
# print("Data Inserted!!!")
# con.commit()

# Select All ----------> 

# print("p_id \t p_name \t price \t quantity \n")

# c = cur.execute("SELECT * FROM Product")
# for q in c:
#     print(q[0],"\t",q[1],"\t",q[2],"\t",q[3],"\n")
 
# Update Query----------->

cur.execute("UPDATE Product SET quantity = quantity+1");
con.commit()
print("p_id \t p_name \t price \t quantity \n")
c = cur.execute("SELECT * FROM Product")
for q in c:
    print(q[0],"\t",q[1],"\t",q[2],"\t",q[3],"\n")   
con.close()