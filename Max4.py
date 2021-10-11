# Q. Write a program to find the greatest of 4 numbers entered by the user (without using logical operators).

# By -  Kunal Baraniya

maxn = []
print("Enter 4 number: ")
x=1
for i in range(4):
    maxn.append(int(input("number " + str(x) + " =")))
    x=x+1
print("Maximun number between 4 digit:", max(maxn))

# Output: Enter 4 number: 
#         number 1 =12
#         number 2 =34
#         number 3 =67
#         number 4 =10
#         Maximun number between 4 digit: 67