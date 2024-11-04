'''
The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), 
and returns True or False according to the result.
'''

# Demonstrating the isalnum() method:
print('lambda30'.isalnum()) # True
print('lambda'.isalnum()) # True
print('30'.isalnum()) # True
print('@'.isalnum()) # False
print('lambda_30'.isalnum()) # False
print(''.isalnum()) # False

'''
The more intriguing examples are here
'''
t = 'Six lambdas'
print(t.isalnum()) # False

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum()) # False

t = '20E1'
print(t.isalnum()) # True