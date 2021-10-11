# Q. Can you change the values inside a list which is contained in set S?  S = {8,7,12,”Simarjeet”,[1,2]}

# By -  Kunal Baraniya

S = [8,7,12,"Simarjeet",[1,2]]
S[4]="Kunal Baraniya"
S[0]=9
print("Changed list = ",S)

# Output : Changed list =  [9, 7, 12, 'Simarjeet', ' Kunal Baraniya']