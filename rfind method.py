'''
The one-, two-, and three-parameter versions of the rfind() method do nearly the same things as their counterparts (the ones devoid of the r prefix), 
but start their searches from the end of the string, not the beginning (hence the prefix r, for right).

Remember: 
The find() method looks for a substring and returns the index of the first occurrence of this substring
'''

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta")) # output -> 8
print("tau tau tau".rfind("ta", 9)) # output -> -1
print("tau tau tau".rfind("ta", 3, 9)) # output -> 4