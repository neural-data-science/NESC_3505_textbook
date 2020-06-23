# Lesson 1: Introduction to Python

[View this lesson on DataCamp](https://learn.datacamp.com/courses/intro-to-python-for-data-science )

## Chapter 1
This chapter introduces the basics of python - simple math and variable types
Basic Operations
\# - add comment
\+ - addition
 \- subtraction
 \* - multiplication
\/ - division
** - exponentiation
% - modulo, returns remainder of division (ie. 18 % 7 equals 4)
= - variable assignment
== - equal to
!= - not equal to
Variable Types
Integer - number without fractional part
Float - number with both integer and fractional part, separated by a point
String - text, use ' ' or " " to generate
Boolean - logical values, can only be True or False
Functions
print()  - outputs what's enclosed in ()
type() - gives the type of a defined variable
str() - converts a value into a string
int() - converts a value into an integer
float() - converts a value into a flaot
bool() - converts a value into a boolean

## Chapter 2
This chapter covers everything to do with lists - creating lists, subsetting, and manipulation
Variable Types
List - can contain many different types, made with []
List subsetting
0 indexing - first element in a list has index 0
Negative indexing - starts at the end of the list (-1 gives last element)
Slicing
[inclusive:exclusive]
Not including a starting index takes everything from the beginning of the list to the value you specify (ie [:3] takes from beginning to 4th element)
Not including an end index takes everything form the value you specified to the end of the list
List Manipulation
Replacing list elements - subset list and assign a new value using =
Extend a list - use + operator to add elements
Delete list items - use del(list[index])
Copying a list - use list('list name')

## Chapter 3
 This chapter introduces a variety of functions and methods, as well as python packages
### Functions
max() - gives maximum element of a list
round(number, ndigits) - calling with only 1 input results in rounding nearest integer
len() - gives the length of a list or a string
help() - provides information about a function
? - use before a function, same purpose as help()
Sorted(iterable, reverse=False)
Sorts items in a list in ascending order
Specifying reverse=True will give items in descending order

### Methods
.index() - gives index of the input
.capitalize() - returns string with the first letter capitalized
.upper() - capitalizes all letters in a string
.count()
counts how many of the input are in a string
counts the number of times an element appears in a list
.append() - adds an element to the list it is called on
.remove() - removes the first element of a list that matches the input
.reverse() - reverses the order of the elements in the list its called on

### Packages
Import _ as _ - import a package
From _ import _ - use if you only need a specific function from a package

## Chapter 4
This chapter introduces the numpy package, focussing on the numpy array
### Numpy arrays
np.array() - create numpy array from a list
Contain values of only 1 type (for booleans, True=1, False=0)
Does operations element wise
Can subset numpy arrays using [] or boolean arrays
#### 2D arrays
Can create from a regular python list of lists
Subset using [rows, columns]
.shape - gives shape (rows, cols) of 2D numpy array
### Functions (statistics)
np.mean()
np.median()
np.corrcoef() - correlation coefficient
np.std() - standard deviation
