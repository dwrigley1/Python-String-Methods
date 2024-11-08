'''
The split() method does what it says - it splits the string and builds a list of all detected substrings.

The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.

If the string is empty, the resulting list is empty too.
'''

# Demonstrating the split() method:
print("phi       chi\npsi".split()) # output -> ['phi', 'chi', 'psi']

'''
Note: the reverse operation can be performed by the join() method.
'''

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
print(s3[1])