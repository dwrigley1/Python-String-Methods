'''
The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.

The centering is actually done by adding some spaces before and after the string.

Don't expect this method to demonstrate any sophisticated skills. It's rather simple.

The example in the editor uses brackets to clearly show you where the centered string actually begins and terminates.
'''

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']') # outputs -> [   alpha   ]
print('[' + 'alpha'.center(10, '*') + ']') # outputs -> [**alpha***]