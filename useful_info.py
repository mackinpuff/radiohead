'''useful python info '''

# Why python? It has efficient high-level data structures and a simple but effective
# approach to object-oriented programming. 

# One of the main advantages of python is that it is quick to use and implement. 
# There is no need for extensive compiling, testing and re-compiling. It is agile. 

# "You could write a Unix shell script or Windows batch files for some of the tasks
# to move around files and change text data, but these are not well-suited for GUI
# applications or games. C/C++/Java take a lof ot development time to even get a 
# first-draft program. 

# Moreover, python offers more error checking than C, and (being a very-high-level 
# language) has high-level data types built in such as flexible arrays and 
# dictionaries. 

# Python allows you to split your program into modules that can be reused in other
# Python programs, and comes with a large collection of standard modules that can 
# be used as the basis of programs. 

# Moreover, it is extensible. It can be linked into applications written in C. 



# GETTING STARTED IN PYTHON
# Add the python path to whereever you are in the command line
# set path = %path%;c:\Python27

# Indices: the start is always included and the end excluded to make sure that
# s[:i] + s[i:] equals s (e.g. 'Python'[:2]+'Python'[2:] = 'Python')

# Multiple assignment possible 
# A trailing comma avoids newline after output. 
def fib(n):
	'''Create a Fibonacci sequence up to n''' 
	
	'''Functions should be followed by a one-line description, then an empty line. Further documentation can follow after the empty line.'''
	
	a,b = 0,1
	while b<n:
		print b,
		a,b = b, a+b


# Control flow:
# 'for' in python is different from other languages. Rather than always iterating 
# over an arithmetic progression of numbers, or giving the user the ability
# to define both the iteration step and halting condition, Python's 'for' statement
# iterates over the items of any sequence in the other that they appear in the sequence.

# The 'break' statement breaks out of the smallest enclosing for or while loop. 
# Loop statements may have an 'else' clause, which is executed when the loop terminates
# through exhaustion of the list or when the condition becomes false, but not
# when the loop is terminated by a 'break' statement'. 

# Prime number searcher
for n in range(2, 100):
	for x in range(2,n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break
	else:
		print n ,'is a prime number'

# a 'try' statement's 'else' clause runs when no exception occurs, and a loop's 
# 'else' clause runs when no 'break' occurs. The 'continue' statement continues
# with the next iteration of the loop. 

# Pertaining to functions, a function introduces a new symbol table used for the 
# local variables of the function. All variable assignments in a function store the 
# value in the local symbol table. Variable references first look in the local
# symbol table, then in the local symbol tables of enclosing functions then in the
# global symbol table. 
# The name of a function can be assigned to another name which can then also be used
# as a function. 

# The 'return' statement returns with a value from a function. 'return' without
# an expression returns 'None'. Failing off the end of a function also returns 'None'

# NOTE: the default values of a function are evaluated *at the point of function
# definition in the defining scope. e.g.
i = 5
def f(argument=i):
	print argument
	
i = 6
f() # prints '5'.

# NOTE 2: The default vlaue is evaluated only once. A mutable object such as a list 
# therefore can accumulate the arguments passed to it on subsequent calls.

# Calling arguments can be done in multiple ways, as long as the calling is done 
# in a consistent manner and non-multiply. 


# KEYWORDS
# keywords: when a final formal parameter in the form of ** is present, it receives
# a dictionary containing all keyword arguments except from those corresponding to
# a formal parameter. 


# METHODS
# A method is a function that 'belongs' to an object and is named obj.methodname


# LAMBDA expressions
# Small anonymous functions can be created with the lambda keyword. This function
# returns the sum of its two arguments: lambda a,b: a+b. Lambda functions can be used 
# wherever function objects are required. They are syntactically restricted to a single
# expression. Semantically, they are just syntactic sugar for a normal function
# definition. Like nested function definitions, lambda functions can reference variables from the containing scope. E.g.

def make_incrementor(n):
	return lambda x: x+n
	
f = make_incrementor(42)
f(0)
>> 42
f(1)
43

# Another interesting example (setup): 
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# lambda form 
pairs.sort(key=lambda pair: pair[1])
pairs

# def form
def sort_key(pair):
    return pair[1]

pairs.sort(key=sort_key)


# Now, there are some notes on CODING STYLE:
# Use 4-space indentation, no tabs.
# Wrap lines so that they do not exceed 79 characters (that's as long as this)
# Use blank lines to separate functions and classes, and larger
# blocks of code inside functions. 
# Use spaces around operators and after commas, but not directly inside
# bracketing constructs: a = f(1, 2) + g(3, 4)

# IMPORTS
# Imports should be grouped in order:
# 1. Standard library imports
# 2. Related third party imports
# 3. local application/library specific imports
# And put a blank line between each group. 

# Absolute imports are recommended, usually more readable. e.g.
# import mypkg.sibling
# from mypkg import sibling
# from mypkg.sibling import example
# Explicit relative imports are an acceptable substitute:
# from . import sibling 
# wildcard imports should be avoided. 





# ITERABLES
# Everything you can use "for...in..." on is an iterable.
# These iterables are handy because you can read them as much as you wish, but:
# You store all the values in memory and this is not always what you want when you 
# have a lot of values. 

mylist = range(1,4)
for i in mylist:
	print(i)
	
# GENERATORS 
# Generators are iterators, but you can only iterate over them once. That's because
# they do not store all the values in memory, they generate the values on the fly.

mygenerator = (x*x for x in range(3))
for i in mygenerator:
	print(i)
	
# You cannot perform for i in mygenerator a second time since generators can only be used once. 

# YIELD
# Yield is a keyword that is used like return, except the function will return a 
# generator. 

def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i
		
mygenerator = createGenerator()
for i in mygenerator:
	print(i)
	
# To master yield, you must understand that when you call the function, the code 
# you have written in the function body DOES NOT RUN. The function only returns 
# the generator object. THEN, your code will be run each time the for uses the generator.

# The first time the 'for' calls the generator object created from the function,
# it will run the code in the function from the beginning until it hits yield. 
# Then it'll return the first value of the loop. Each other call will run the loop
# written in the function one more time, and return the next value, untill
# there is no more value to return. 

# This can be useful for various things like controlling access to a resource. 







# itertools
# http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python