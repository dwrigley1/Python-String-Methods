'''
The join() method is rather complicated.

As its name suggests, the method performs a join - it expects one argument as a list; 
it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
all the list's elements will be joined into one string but...
...the string from which the method has been invoked is used as a separator, put among the strings;
the newly created string is returned as a result.
'''

'''
Let's analyze it: 

the join() method is invoked from within a string containing a comma (the string can be arbitrarily long, or it can be empty)
the join's argument is a list containing three strings;
the method returns a new string.
'''

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"])) # output -> omicron,pi,rho
print("".join(["omicron", "pi", "rho"])) # output -> omicronpirho
print(" ".join(["omicron", "pi", "rho"])) # output -> omicron pi rho

'''
To join strings in a readable way, use join() with a separator, like a space or a comma, and pass in an iterable of strings:
'''
# Demonstrating joining strings in conjunction with variables
string_one ="Hello"
string_two ="World"
string_three = [string_one, string_two]
print(" ".join(string_three))

