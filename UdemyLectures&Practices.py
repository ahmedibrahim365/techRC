# Lesson 1
# How to use CMD line
# To know where you are in the directory type       >>> cd
# You can also type to list whats in the directory  >>> dir
# To jump into a file you can type                  >>> cd Desktop or cd etc...
# To go back to the directory type                  >>> cd ..
# To clear all of its type                          >>> cls

# numpy is numerical computing

# Introduction to strings:

# Indexing happens when you want to grab a single character from a string

# Such as: h e l l o
# Index    0 1 2 3 4
# rev.     0 -4 -3 -2 -1

# Slicing allows you to grab a subsection of multiple characters, a 'slice' of the string

# Structure of slicing              [ start : stop : step ]
#           >>> start is the numerical index for the slice START
#           >>> stop  is the index you will go up to (but not include)
#           >>> step  is the size of the 'jump' you take

start_string = 'START'
print('START STRING SLICING [firstletter]', start_string[0])


stop_string = 'STOP'
print('STOP STRING SLICING\n[THIRD LETTER REV. INDEXING]', stop_string[-2])

step_string = 'START STOP STEP'
print('STEP STRING JUMP [::2]', step_string[::2])

print('Start, Stop, Slice', step_string[2:7:2])
print('reverse slicing =', step_string[::-1])

# String concatenation
title = 'concatenation'
alt_title = title[3:]
print(alt_title)

# String are immutable
# Can't use indexing to change individual elements of a string


# built in string methods
# object on python usually have built in methods
# where the methods are function inside the object

A = "Jump IN"

print(A.title())
