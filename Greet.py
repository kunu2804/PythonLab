# Q. Write a program to greet all the person names stored in a list L1 and which starts with S. (hint: use startswith("S") method)   L1 = [“Simarjeet”, “Sohan”, “Sachin”, “Rahul”]

# By - Kunal Baraniya 
 

L1 = ["Simarjeet", "Sohan", "Sachin", "Rahul"]

for i in L1:
    if i.startswith('S'):
        print("Hello ",i)


# Output : Hello  Simarjeet
#          Hello  Sohan
#          Hello  Sachin