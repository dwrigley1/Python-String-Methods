'''
The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the leading and trailing whitespaces.
'''

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]") # output -> [aleph]

'''
Reviewing rstrip() and lstrip() methods
'''
print("[" + "   aleph   ".rstrip() + "]") # output -> [   aleph]
print("[" + "   aleph   ".lstrip() + "]") # output -> [aleph   ]