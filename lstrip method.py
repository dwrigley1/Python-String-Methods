'''
The parameterless version of the lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.

Note: The brackets are not a part of the result - they only show the result's boundaries.
'''

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]") #output -> [tau ]

'''
The one-parameter version of the lstrip() method does the same as its parameterless version, 
but removes all characters enlisted in its argument (a string), not just whitespaces
'''

print("www.cisco.com".lstrip("w.")) # output -> cisco.com
print("pythoninstitute.org".lstrip(".o")) # output -> pythoninstitute.org

'''
Leading characters, leading whitespaces.
'''