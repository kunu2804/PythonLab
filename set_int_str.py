# Q. Can we have a set with 18 (int) and “18” str as values in it?

# By - Kunal Baraniya

sint = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
sstr1 = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'}

# Union operation performed
print("Merged sets = ",sstr1.union(sint))

# Output : Merged sets =  {1, 2, 3, 4, 5, 6, 'H', 7, 8, 9, 10, 11, 12, 13, 'N', 14, 15, 16, 17, 'G', 'B', 'Q', 18, 'F', 'D', 'M', 'C', 'J', 'O', 'L', 'P', 'R', 'K', 'I', 'E', 'A'}

