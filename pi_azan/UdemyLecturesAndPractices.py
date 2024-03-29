#!/usr/bin/env python

# This is Windows Specific. It is a good start, but the work runs on non-Windows. So it is imperative to know about that too.
# We're not going to delve into that now until you have access to a Linux virtual machine to learn in it.

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

# When you use the index operation [N] where n is an integer matching one of the index number as outlined above,
# you get the corresponding letter in that index (position) back.
# That's why this prints S because it is the letter at index 0 of the start_string

start_string = 'START'
print( 'START STRING SLICING [firstletter]', start_string[0] )

# Here you're starting backward, this isn't very common in other languages, but python has it.
stop_string = 'STOP'
print( 'STOP STRING SLICING\n[THIRD LETTER REV. INDEXING]', stop_string[-2] )

# Here you're taking a "Slice" which you can think of as a sandwich slice.
# This one says take a slice from the beginning of the string until the end but leave the last two characters out.
# That's why this print omits the E and P of STEP.

step_string = 'START STOP STEP'
print( 'STEP STRING JUMP [::2]', step_string[::2] )

# I doubt that you'll need to use this fancy slicing in the next two lines real application code.
# If your algorithm requires this much "slicing and dicing" then you need to rethink it.
# It will be difficult for you (or others) to know what you're trying to do when you come back later to read this code.
# Optimize your development for maintainability and readability.

print( 'Start, Stop, Slice', step_string[2:7:2] )
print( 'reverse slicing =', step_string[::-1] )

# String concatenation
# No concatenation is done here by the way, review that lesson and come back here again.
title = 'Repository'
alt_title = title[2:]

print( 'De' + alt_title )

# String are immutable
# Can't use indexing to change individual elements of a string


# built in string methods
# object on python usually have built in methods
# where the methods are function inside the object

A = "Jump IN"

# The "title" method converts the latin strings first character to an upper case,
# the "A" string variable is already like that, to see the "title" function work you need
# to make sure your "A" string is all lower case.

print( A.title() )
print( A.lower() )

# String Interpellation

# There are two type of methods
#               >>> .format()
#               >>> f-strings   (formatted string literals)


# A string with' {}' format.('insert interp. 1','insert interp. 2', 'etc...')
print( "\t\t\t .format string_interpellation".title() )
print( 'You can have a before string then add {}'.format( 'an after string' ) )
# using number of interp position
print( 'Or use multiple {0} {1} {2}'.format( 'multiple', 'string', 'and keywords' ) )
# Or assigning variables
print( 'DYK: The {Rc} was once named {t}'.format( Rc='RubiksCube', t='techRC' ) )

# Float formatting      "{value:width.precisionf}"
Range = 100 / 77
precision = 100 / 77
print( "Float formatting considers a tradeoff between {r:3.3f} and {p:3.5f}".format( r=Range, p=precision ) )

# f-string method

# name = input('What is your name:')
# intro = 'Hello'
# name_input = name
# w = 'Welcome'

# print(f'{intro} {name}')
# print(f'{name}, what is your age?')
# print(f'{intro} {name_input} and {w} to your age of', input())


# Lists in Python


print("List in Python".title())

mylist = ['one', 'two', 'three']
print( mylist )
another_list = ['four','five']
print((mylist + another_list))
mylist[0] = 'ONO'
print(mylist)                                                        #mutate a string in list
print(mylist, another_list.append('six'))