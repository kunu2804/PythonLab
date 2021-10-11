# Q. Replace double spaces with single spaces in previous program

# By - Kunal Baraniya

string = input("Enter String: ")
while '  ' in string:
    string = string.replace('  ', ' ')
    print("changed string = " + string)

# Output: Enter String:  Kunal  Baraniya
#         changed string =  Kunal Baraniya