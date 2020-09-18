# Lesson 2: Intermediate Python

[View this lesson on DataCamp](https://learn.datacamp.com/courses/intermediate-python-for-data-science)

## Chapter 1: Matplotlib
This chapter introduces the basics of Matplotlib - how to make, configure, and show plots
### Lineplots

| |  |
|------------------ |----------------|
|`plt.plot(x,y)`    |create lineplot |
|`plt.show()`       |show plot       |
|`plt.title()`      |set plot title  |
|`plt.xlabel()`     |set x-axis label|
|`plt.ylabel()`     |set y-axis label|
|`plt.xscale('log')`|set x-axis to log scale|
|`plt.xticks()`     |define x-axis increments|
|`plt.yticks()`     |define y-axis increments|

### Scatterplots
Same as above, but with the scatter method
`plt.scatter(x,y)`

|Argument        |Function           |
|----------------|-------------------|
|`s=`            |size; sets dot size|
|`c=`            |colour, sets dot color|
|`alpha=`         |set data point transparency|

### Histograms 

|||
|--------------|----------------|
|`plt.hist()`  |create histogram, the `bins=` argument allows you to specify the number of bins|
|`plt.clf()`   |clean up plot a plot that's already been created so you can start fresh|

## Chapter 2: Dictionaries & pandas

### Dictionaries
Dictionaries are immutable, and composed of {'key':value} pairs

maritimes = {'NS':'Halifax', 'NB':'Fredricton', 'PEI':'Charlottetown'}

Calling `.keys()` prints all keys from a specified dictionary

maritimes.keys()

Calling dict['key'] will return the value that corresponds with that key

maritimes['NS']

Values can be added to dictionaries

maritimes['NFLD'] = 'St. Johns'
print(maritimes)

...and deleted using `del()`

del(maritimes['NFLD'])
print(maritimes)

### pandas DataFrames

Pandas dataframes are a way of storing tabular data. While we could store a data table in a 2D NumPy array (as we previously learned), a pandas dataframe has a number of advantages. It's more like an Excel spreadsheet, in that it can have column names (labels) and row indexes (the equivalent of column names, but for rows). As well, pandas offers a variety of methods that make it easier and more intuitive to work with data than a NumPy array.

To import the pandas package we use the convention:

import pandas as pd

To convert an object, such as a NumPy array, to a pandas DataFrame, we use pd.DataFrame():

# Create np array
import numpy as np

x = np.array(([1,2,3,4],[5,6,7,8]))
print(x)

# convert to DataFrame
df = pd.DataFrame(x)
df

Note above the pretty formatting that Jupyter applies when viewing a DataFrame. That alone makes it easier to work with than a NumPy array!

Note above that the column labels and indices are by default just sequential numbers, starting from zero as is the norm in Python.

Often we'll be reading data from a file rather than creating DataFrames from scratch. To load the contents of a CSV file into a DataFrame, use `pd.to_csv()`. Here we'll load a small CSV file containing 10 reaction times (RTs):

df = pd.read_csv('rt_data.csv')
df

Note above that the first imported column is `Trial_Num`, which starts at 1, but the index, by default, starts from zero. We can tell pandas that we want the trial number to act as the index, which could make our life easier later on when working with this data:

df = pd.read_csv('rt_data.csv', index_col='Trial_Num')
df

### Slicing pandas dataframes
dataframe[#:#] allows you to slice specified rows based on integer index

|Slicing with `.loc` |                   |
|--------------------|-------------------|
|`.loc['']`         |slice specified row based on string index --> pandas series|
|`.loc[['']]`       |slice specified row based on string index --> pandas dataframe|
|`.loc[[''], ['']]` |slice specified rows and columns --> pandas sub-dataframe|
|`.loc[:, ' ']`     |slice all rows and specified columns --> pandas series|
|`.loc[:, [' ']]`   |slice all rows and specified columns --> pandas sub-dataframe|


|Slicing with `.iloc` |                   |
|--------------------|-------------------|
|`.iloc[#]`          |slice specified row based on integer index|
|`.iloc[[#]]`        |slice specified row based on unterger index --> pandas dataframe|
|`.iloc[[#], [#]]`   |slice specified rows and columns --> pandas sub-dataframe|
|`.iloc[:, #]`       |slice all rows and specified columns --> pandas series|
|`.iloc[:, [#]]`     |slice all rows and specified columns --> pandas sub-dataframe|

## Chapter 3: Logic, Control Flow, & Filtering

### Comparison Operators 
|               |               |
|---------------|---------------|
|`==`           |"are equal"    |
|`<` and `>`    |"is less than" and "is greater than" |
|`<=` and `>=`  |"less than or equal to" and "greater than or equal to"|
|`!=`           |"is not equal to"|

### Boolean Operators
|Operator          |Function       |
|------------------|---------------|
|and               |require 2 or more specified objects|
|or                |require at least one specified object|
|not               |anything but specified object|
|`np.logical_and()`|"and" statement, can be passed multiple comparison criteria|
|`np.logical_or()` |"or" statement, can be passed multiple comparison criteria|
|`np.logical_not()`|"not" statement, can be passed multiple comparison criteria|

### Conditional Statements

```
if condition :
     expression
elif condition : 
     expression
else :
     expression
```

`if` - check if initial specified condition holds True. If so, perform specified expression(s).

`elif` - (else if) if the `if` condition is False, check whether this secondary condition holds True. If so, perform secondary specified expression(s)

`else` - if all `if` or `elif` conditions are False, perform specified expression. 

Note that `elif` and `else` are *not required* in `if` statements. When you write an `if` statement with no `elif` oe `else` options, and the `if` statement is not True, then Python simply moves on as if nothing ever happened.

<div class="alert alert-block alert-info">
Always be sure your `if`, `elif`, and `else` lines end with colons!
</div>

x = 11

if x < 10: 
    print("Smaller than 10")
else:
    print("Larger than 10")

A most complex example, to tell the season based on the month:

month = 'January'

if month == 'June' or month == 'July' or month == 'August':
    print('Summer!')
elif month == 'September' or month == 'October' or month == 'November':
    print("Fall")
elif month == 'December' or month == 'January' or month == 'February':
    print("Winter")
else:
    print("Spring")


## Chapter 4: Loops

### `while` Loops 
While loops will execute the code many times, as long as the condition is true ("as long as *x* is true, do *y*")

Format:

```
while condition:
    expression
```



Count to 10, by twos:

x = 0

while x <= 10:
    print(x)
    x = x + 2

The code below stops once `x` becomes less than 6

x = 20

while x > 6:
    x = x/2
    print(x)

### `for` Loops
For loops are used to iterate over data types, and perform functions on each element

General Format:

```
list = [x, y, z]
for item in list :
      expression
```
      
See the example using the list 'odd' below

odd = [1, 3, 5, 7, 9]
for value in odd:
    print(value)

Use `enumerate()` to access index information (number of the current item in the sequence) during iteration:

names = ['Xhelal', 'Erika', 'Hezekiah', 'Antonia', 'Yaser']

# Just print the names
for x in names:
    print(x)

# Enumerate and show the names
for value in enumerate(names):
    print(value)

#### To loop over a list of lists:

lol = [['something', 4.2], ['something_else', 5.4]]

# Each list in our list has two entries; 
# if we just specify one variable to iterate over, we get each whole sub-list:
for this in lol :
      print(this)

<div class="alert alert-block alert-info">
Note above that when we iterate through a list (or dictionary, or array, as you'll see below), we make a new "dummy" variable name (and *iterator* to use inside the list for each entry from the list. In the example above we called the iterator `this`.
</div>

# But if we specify two variables, it assigns one to each entry within the sub-lists:
for this, that in lol:
    print(this)

for this, that in lol:
    print(that)

#### To loop over a dictionary

Remember that dicts are key:value pairs. Python iterates over the *keys* of dicts:

names_ages = {'Xhelal':22, 'Erika':25}

for name in names_ages :
    print(name)
#     print(names_ages[name])

If you want the *values* instead, you need to use indexing, where you use the iterator as the index to the original dict name:

for name in names_ages:
    print(names_ages[name])

Print key then value:

for name in names_ages:
    print(name)
    print(names_ages[name])

#### To loop over a numpy array:

1D arrays:

import numpy as np

odds = np.array([1, 3, 5, 7, 9])

for x in odds : 
    print(x + 100)

2D arrays:

odds_evens = np.array([[1,2], [3,4], [5,6], [7,8], [9,10]])
print(odds_evens)

for x in np.nditer(odds_evens):
    print(x * 100)

#### To loop over a dataframe

The beauty of pandas DataFrames is that they provide methods that automatically iterate over rows or columns, and they do so in ways that are much more efficient (and elegant code) than using a `for` loop. So in most cases you should first consider how do do what you want without a `for` loop. But, if you really want to, here is how. 

Recall the DataFrame we created above, called `df`:


df

Let's multiply each value in each row by 1000:

# Original data is in seconds; print out RTs in milliseconds instead:
for index, row in df.iterrows() :
    print(row * 1000)

## Chapter 5: Hacker Statistics

### Random number generators

Generate a random number:

import numpy as np

np.random.rand()

Run it again, and we'll get a differnt number (which is the point of 'random', right?)

np.random.rand()

By default, the output of `np.random.rand()` is a random number between 0 and 1, drawn from a **uniform distribution** — in other words, any value is as likely as any other value in the range of 0–1. (One could also specify a different distribution, like a normal distribution with a mean of 0.5, where the value was most likely to be close to the centre of the distribution, i.e., close to 0.5).

If you want a random number in a different range, such as 0-100, you can simply multiply the result:

np.random.rand() * 100

However, if you want to specify a less rounded range, like, say, 78–94, and don't want to figure out the multiplier to do that, there is a "convenience function" that will allow you to specify the range. This is, arguably, more pythonic becuase it is more explicit/obvious to someone else reading your code:

np.random.randint(78, 94)

If you want more than one random number, you can generate a list (1d NumPy array) by giving the command a single numeric argument:

np.random.rand(5) 

You can generate a 2d NumPy array by giving it two arguments in the familiar (row, column) format:

np.random.rand(5, 2) 

You can't chain the `rand()` and `randint()` commands, but the `randint()` takes an additional `size=` argument that allows you to specify the number/shape of the outputs:

np.random.randint(10,100, size=10)

np.random.randint(10,100, size=(5, 2)) # note size is a tuple

### Seeds

Sometimes, however, we want to generate the same random number every time. This may seem counter-intuitive, but it may be useful, for example if we want to write reproducible code that generates the same output every time it's run. One scientific application of this is simulations: sometimes, scientists want to create simulated data and test their algorithms on that, rather than on real data. They might want to do this because simulated data has known properties (e.g., you know the "truth"), whereas in real data, the point of analysis is often to identify certain properties that are not known. So if you are trying a new analysis method, and you don't know what the "true" result is because you're working with real data, it can be hard to validate the algorithm. If you use simulated data, you can get around that. 

As a simple example, we might want to simulate some human reaction time (RT) data. We might want to specify that it has a particular mean, but the simulated data would be a set of randomly-generated numbers that, when averaged, produced that mean. If we wanted to write some Python code in a Jupyter notebook to run this simulation, we might want it to generate the same simulated data each time — especially if this was example code that we were sharing with other scientists who would want to reproduce our results. In this case, we would want to specify the random **seed** — the number that "seeds" the random number generator to produce number or set of numbers.

Below we specify a seed of 42 ([the answer to the Ultimate Question of Life, the Universe, and Everything](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy)), and show that each time we do so, then call `np.random.rand()`, we get the same random number:

np.random.seed(42)
np.random.rand()

np.random.seed(42)
np.random.rand()

np.random.seed(42)
np.random.rand()

Importantly though, we do need to explicitly call `np.random.seed(42)` each time we want to generate that same random number, otherwise the seed will reset the next time we run the command:

np.random.seed(42)
print(np.random.rand())
# Remember we need to "print" outputs if we want more than just the last command's
# output in a Jupyter notebook)

print(np.random.rand())

print(np.random.rand())

np.random.seed(42)
print(np.random.rand())

np.random.seed(42)
print(np.random.rand())