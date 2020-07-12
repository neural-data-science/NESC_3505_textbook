# Lesson 1: Introduction to Python

These notes are based on the sequence that concepts are introduced in the DataCamp lesson of the same name. They are most useful as a reference, after you've completed the DataCamp lesson. They are not intended to replace that lesson.

[View this lesson on DataCamp](https://learn.datacamp.com/courses/intro-to-python-for-data-science )

## Chapter 1
This chapter introduces the basics of Python - simple math and variable types

### Basic Operations

| Operator |  Operation                                                   |
|----------|--------------------------------------------------------------|
| `#`      |  add comment                                                 |
| `+`      |  addition                                                    |
| `-`      |  subtraction                                                 |
| `*`      |  multiplication                                              |
| `/`      |  division                                                    |
| `**`       |  exponentiation                                              |
| `%`        |  modulo; returns remainder of division (e.g., `18 % 7` equals `4`) |
| `=`        |  variable assignment                                         |
| `==`       |  equal to                                                    |
| `!=`       |  not equal to                                                |



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

So when you modify `all_numbers`, you also change `my_numbers_nono`

del(all_numbers[8])
my_numbers_nono

## Chapter 3

 This chapter introduces a variety of functions and methods, as well as Python packages

my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

### Functions

#### Max/min values in list

max(my_list)

min(my_list)

#### Rounding

pi = 3.14159265359
round(pi, 2)

#### Length of list

len(my_list)

#### Help

?round

#### Sorting

going_up = sorted(my_list)
going_up

going_down = sorted(going_up, reverse=True)
going_down

### Methods

Methods are functions that are applied to a variable by adding a dot then the method name (and parentheses) to the end of the variable name.

| Method | What it does |
|--------|--------------|
|`.index()` | for a list, gives index of the input value |
|`.capitalize()` | returns string with the first letter capitalized |
|`.upper()` | capitalizes all letters in a string |
|`.count()` | for `string`: counts how many of the input are in a string |
|`.count()` | for `list`: counts the number of times an element appears in a list |
|`.append()` | adds an element to the list it is called on |
|`.remove()` | removes the first element of a list that matches the input |
|`.reverse()` | reverses the order of the elements in the list its called on |
|`.round()` | rounds a float to the number of decimal places specified in the parentheses |

going_down.index(10)

going_down.append(0)
going_down

### Packages

Import a package (sometimes called a library), including all its functions

import matplotlib

Import a package and give it a shorthand name:

import numpy as np

## Chapter 4

This chapter introduces the `numpy` package (by convention, imported as `np`), focusing on the numpy array data type.

### NumPy arrays

NumPy arrays are similar to lists: ordered sets of values. However, they behave differently, and can have multiple dimensons (see below), so NumPy arrays are often a better choice for structured data.

You can **create** an np array manually by putting a list inside the `np.array()` function:

np_odds = np.array([1, 3, 5, 7, 9])
np_odds

Or by specifying the name of a list you previously created:

evens = [2, 4, 6, 8, 10]
np_evens = np.array(evens)
np_evens

**Note**: If you just type the name of an array, you'll see the the contents of the array, embedded inside `array()`, as shown above. If you `print()` the array, you'll see only its contents:

print(np_evens)

Either way above is acceptable, but remember that in Jupyter, you need to use `print()` to see the output of anything other than the last returned value:

np_evens
np_odds

print(np_evens)
np_odds

NumPy arrays can only contain values of one type. Values are converted to a different type to enforce this:

np.array([1, 'two', False])

Above, the int `1` and the Boolean `False` were converted to a string, because the string 'two' couldn't be converted to any other type.

Below, we only have ints and Booleans. Booleans are converted to ints:

np.array([1, 2, False, True])

Unlike lists, operations are applied to np arrays element-wise (i.e., applies operation to each element in the array).

So for a list, this is probably *not* your intended outcome:

print(evens * 2)

But for a NumPy array:

print(np_evens * 2)

### 2D arrays

A NumPy array with two dimensions (rows and columns).

Can create from a regular python list of lists (note the two lists are inside another list/set of square brackets):

my_2d_array = np.array([[0, 1, 2], [3, 4, 5]])

my_2d_array

#### Indexing 2D Arrays:
Specify in format [*rows*, *columns*]. As with lists, `:` selects entire row/column, and you can use negative indexing

my_2d_array[0, :]

my_2d_array[1, :]

Column only:

my_2d_array[:, 0]

Last coumn:

my_2d_array[:, -1]

Select single value by specifying a particular row and column:

my_2d_array[1, 1]

`.shape` *attribute* gives shape (rows, cols) of 2D numpy array:

my_2d_array.shape

### NumPy Array Functions

np.random.rand(10)

# Some random numbers:
my_data = np.random.rand(10)
print(my_data)

#### Mean

np.mean(my_data)

#### Median

np.median(my_data)

#### Standard Deviation

np.std(my_data)

If you don't like long numbers, you can apply the .round() method to the output:

std_dev = np.std(my_data).round(3)
print(std_dev)

#### Correlation 

Between two arrays:

# Final grades
grades = np.array([67, 74, 44, 92, 88])

# hours per week spent working on course
hours = np.array([5.2, 7, 2.0, 9.25, 7.5])

Does more hours spent on the course translate into a better grade?

np.corrcoef(grades, hours)

Yes! The correlation is positive and strong (approximately .979)