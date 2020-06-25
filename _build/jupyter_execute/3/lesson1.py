# Lesson 1: Introduction to Python


[View this lesson on DataCamp](https://learn.datacamp.com/courses/intro-to-python-for-data-science )

## Chapter 1
This chapter introduces the basics of Python - simple math and variable types

### Basic Operations

| Operator |  Operation                                                   |
|----------|--------------------------------------------------------------|
| \#      |  add comment                                                 |
| \+      |  addition                                                    |
| \-      |  subtraction                                                 |
| \*      |  multiplication                                              |
| \/      |  division                                                    |
| **       |  exponentiation                                              |
| %        |  modulo; returns remainder of division (e.g., `18 % 7` equals `4`) |
| =        |  variable assignment                                         |
| ==       |  equal to                                                    |
| !=       |  not equal to                                                |



### Variable Types

|                                          |                                                                      |
|------------------------------------------|----------------------------------------------------------------------|
| integer                                  |  number without fractional component (no decimal point)                                      |
| float                                    |  number with both integer and fractional part separated by a decimal |
| string  | text; enclose in `' '` or `" "`    |
| boolean                                  |  logical values; can only be `True` or `False`                       |
|list | Can contain many different types. Create with `[]`. Separate items with commas. |



### Functions
|           |                                       |
|-----------|---------------------------------------|
| `print()` |   outputs what's enclosed in `()`     |
| `type()`  |  gives the type of a defined variable |
| `int()`   |  converts a value into an integer     |
| `float()` |  converts a value into a float        |
| `str()`   |  converts a value into a string       |
| `bool()`  |  converts a value into a boolean      |
| `list()`  |  converts a value or values into a list |

## Chapter 2
This chapter covers everything to do with lists - creating lists, subsetting, and manipulation.

Lists are ordered sets of items. 

### Working with Lists
Create a list:

odd = [1, 3, 5, 7, 9]

First index (position) in list is 0, not 1:

odd[1]

odd[0]

Negative indexing works from the end of the list. 

odd[-1]

#### Slicing
Specify a range of indices inside square brackets: [inclusive:exclusive]

odd[0:5]

odd[1:3]

odd[:]

odd[:3]

odd[3:]

#### List Manipulation
Replacing list elements: subset list and assign a new value using =


odd[0] = 2
odd[0:5]

Extend a list, use + operator to add elements


odd + [11]

odd  = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

all_numbers = odd + even
all_numbers

Sort a list:

all_numbers.sort()
all_numbers

Delete list items:

del(all_numbers[9])  # remember 0-indexing!
all_numbers

Copying a list

my_numbers = all_numbers.copy()

my_numbers

You can also use the `list` function to make a list from another list:

some_numbers = list(all_numbers)

some_numbers

Be careful not to do this. This "points" the new list, `my_numbers_nono`, at the original list, `all_numbers`

my_numbers_nono = all_numbers
my_numbers_nono

So when you nodify `all_numbers`, you also change `my_numbers_nono`

del(all_numbers[8])
my_numbers_nono

## Chpater 3

 This chapter introduces a variety of functions and methods, as well as Python packages

my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

### Functions

Maximum-valued element in list

max(my_list)

min(my_list)

Rounding

pi = 3.14159265359
round(pi, 2)

Length of list

len(my_list)

Get help using a function:

?len

going_up = sorted(my_list)
going_up

going_down = sorted(going_up, reverse=True)
going_down

# Finish from here down

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



