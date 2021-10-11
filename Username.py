# Q. Write a program to check whether a username consists of less than 10 characters or not.

# By -  Kunal Baraniya

usrnme = input("Enter your Username: ")
C = len(usrnme)
if(C<10):
    print("Username consists of less than 10 characters")
else:
    print("Username consists of equal or more than 10 characters")

# Output :    Enter your Username: mayurbohra9
#             Username consists of equal or more than 10 characters

            # Enter your Username: mayurboh
            # Username consists of less than 10 characters