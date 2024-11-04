'''
The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
'''

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # output -> www.pythoninstitute.org
print("This is it!".replace("is", "are")) # output -> Thare are it!
print("Apple juice".replace("juice", "")) # output -> Apple

'''
If the second argument is an empty string, replacing means actually removing the first argument's string.
The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
'''

print("This is it!".replace("is", "are", 1)) # output -> Thare is it!
print("This is it!".replace("is", "are", 2)) # output -> Thare are it!