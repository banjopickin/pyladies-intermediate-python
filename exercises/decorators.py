import time

# Note 1: your code goes everywhere there's an ellipsis (...)

# Note 2: to run this file, use the "normal" way of running Python scripts from
# the command line. For example:
# $ python decorator_solutions.py


# Exercise 1
# Step 1: write a function called "print_message" 
# that prints the phrase "Python is awesome!"

def print_message():
    '''
    step 1 print phrase
    :return: string
    '''
    print "Python is awesome"

#
# Step 2: Write a decorator called "spam" that prints
# the phrase "Ministry of Silly Walks" before the wrapped 
# function is called, prints "Python is awesome!" when 
# the function you wrote in Step 1 is 
# called, and "Pining for the fjords" after this.

def spam(my_func):
    '''
    decorator function
    :param my_func: inner function
    :return:
    '''
    def inner_func(*args, **kwargs):
        print "Ministry of Silly Walks"
        result = my_func(*args,**kwargs)
        print "Pining for the fjords"
        return result
    return inner_func

#
# Step 3: apply your decorator to print_message()

@spam
def print_message():
    '''
    step 1 print phrase
    :return: string
    '''
    print "Python is awesome"


#
# Output will look like the following 3 lines:
# Ministry of Silly Walks
# Python is awesome!
# Pining for the fjords
# ================================

print "Exercise 1 output:"

# ...

print "--------------------------"  # separate exercise output


# Exercise 2
# 
# Write a decorator that returns the product of two numbers.
# Step 1: write a function that returns the product of two numbers.
# Step 2: write a decorator that prints a message before and after
def bf_af(my_func):
    def inner_func(*args,**kwargs):
        print "before"
        result = my_func(*args,**kwargs)
        print "after"
        return result
    return inner_func


@bf_af
def product(n1,n2):
    return n1*n2


# your function is executed.
# ================================
print "Exercise 2 output:"

# ...

print "--------------------------"  # separate exercise output

# Exercise 3
# 
# Write a decorator that outputs the time a function takes to execute.
# Step 1: Write a function that does anything you like. Suggestion: append
# some numbers to a list.
# Step 2: Write a decorator that times how long it takes the function from
# step 1 to run. Hint: time.time(); the time module has already been 
# imported.
# ================================
print "Exercise 3 output:"

# ...

print "--------------------------"


# Exercise 4
# Use a decorator to simulate rate-limiting. That is, have the decorator
# wait before invoking the wrapped function. Your wrapped function can do 
# whatever you want; if you're looking for inspiration try iterating over
# a sequence of numbers.
#
# Step 1: write a function that accepts a number and returns double the number.
# Step 2: write a decorator that accepts arguments and waits one second before
# calling the function from step 1. 
# Hint: time.sleep() will be useful.
# ================================
print "Exercise 4 output:"

# ...

print "--------------------------"
