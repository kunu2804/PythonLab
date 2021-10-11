# Q. Write a program to find out whether a given name is present in a list or not.

# By -  Kunal Baraniya

Names = ["Mayur","Hardik","khushboo","Kunal","Simran","Nik"]
X = input("Enter Name to search: ")

if(X in Names):
    print("Name is Present...")
    exit
else:
    print("Name is not Present...")

# Output :    Enter Name to search:  Rahul
#             Name is not Present...

#             Enter Name to search: Kunal
#             Name is Present...