""" Bracket notation """

# course = "Python for beginners"

# print(course[-1])

""" formatted strings """

# first = "john"
# last = "snow"
# message = f'{first} {last} is a coder'
# print(message)

""" String methods """
#len - to get the length of a string
#upper - transforms to uppercase ... It doesn't affect the original variable, 
# hence doesn't modify the original variable
#find -  Finds an element in a sting and returns the index
#replace - Finds a letter/word in a string & Replaces the word with the value requested  
#in - You want to check the existence/sequence of characters in a string: 
# use in { produces a boolean value}

course = "Python for beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.replace('Python', 'Absolute python'))