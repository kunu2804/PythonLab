# Write a program to fill in a letter template given below with name and date: 
# letter = ''' Dear <|Name|>  You are selected  <|Date|> '''

# By -  Kunal Baraniya

Name = input("Enter your Name: ")
Date = input("Enter Date: ")
print("''' Dear " + Name + "\n You are selected" + "\n" + Date + "'''") 


# Output: Enter your Name: Mayur Bohra
#         Enter Date: 28-09-2021
#         ''' Dear Mayur Bohra
#             You are selected
#             28-09-2021'''