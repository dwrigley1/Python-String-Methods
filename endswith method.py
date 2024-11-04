'''
The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.
Note: the substring must adhere to the string's last character - it cannot just be located somewhere near the end of the string.
'''

# Demonstrating the endswith() method:
# outputs -> yes
if "epsilon".endswith("on"):
    print("yes") 
else:
    print("no") 

# outputs -> no
if "epsilon".endswith("xyz"):
    print("yes") 
else:
    print("no") 