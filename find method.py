'''
The find() method is similar to index(), which you already know - it looks for a substring and returns the index of the first occurrence of this substring, but:
it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
it works with strings only - don't try to apply it to any other sequence.
'''

# Demonstrating the find() method:
print("Eta".find("ta")) # output -> 1
print("Eta".find("mma")) # output -> -1

t = 'theta'
print(t.find('eta')) # output 2
print(t.find('et')) # output 2
print(t.find('the')) # output 0
print(t.find('ha')) # output -1
print(t.find('etaxyz')) # output -> -1

'''
Breakdown:
index 0 -> t
index 1 -> h
index 2 -> e
index 3 -> t
index 4 -> a

find() method returns the number related to the first index it is found within. 
When using find() to locate "et", the letter "e" is located at index 2, therefore the output will return a 2 unless the letters after it are not within the string.
'''

'''
If you want to perform the find, not from the string's beginning, 
but from any position, you can use a two-parameter variant of the find() method.
The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
Among the two a letters, only the second will be found. 
Look at the example:
'''

print('kappa'.find('a', 2)) # output -> 4

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

'''
You can use the find() method to search for all the substring's occurrences, like here:
'''

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
# The code prints the indices of all occurrences of the article the
# output -> 15 80 198 221 238

'''
There is also a three-parameter mutation of the find() method. 
The third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search).
The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
Look at the example below:
'''
print('kappa'.find('a', 1, 4)) # output -> 1
print('kappa'.find('a', 2, 4)) # output -> -1

'''
(a cannot be found within the given search boundaries in the second print().
'''