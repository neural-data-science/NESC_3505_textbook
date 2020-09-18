# Lesson 2: Intermediate Python

[View this lesson on DataCamp](https://learn.datacamp.com/courses/intermediate-python-for-data-science)

## Chapter 1: Matplotlib
This chapter introduces the basics of Matplotlib - how to make, configure, and show plots
### Lineplots
|                   |                |
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
|              |                |
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

maritimes['NFLD'] = 'ST Johns'

And deleted using `del()`

del(maritimes['NFLD'])
print(maritimes)

### Pandas dataframes
Pandas dataframes are a way of storing tabular data

`pd.DataFrame()` - converts an object to a dataframe 

`pd.read_csv('file.csv')` - read in a csv file, argument `index_col=` allows you to set the index column (ie. row labels)

#### Slicing pandas dataframes
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
**if** - check if initial specified condition holds True --> if so, perform specified expression(s)

**elif** - if "if" condition is False --> check whether secondary condition holds True --> if so, perform secondary specified expression(s)

**else** - if all "if" or "elif" conditions are False, perform specified expression

**Format:**

`if condition :
     expression
elif condition : 
     expression
else :
     expression`

## Chapter 4: Loops

### While Loops 
While loops will excecute the code many times, as long as the coniditon is true ("as long as x is true, do y")

Format:

`while condition:
    expression`

For example: The code below is excecuted twice; it stops once x becomes less than 6

x = 20
while x > 6:
    x = x/2
    print(x)

### For Loops
For loops are used to iterate over data types, and perform functions on each element

General Format:

`list = [x, y, z]
for item in list :
      expression`
      
See the example using the list 'odd' below

odd = [1, 3, 5, 7, 9]
for value in odd:
    print(value)

Use `enumerate()` to access index information during iteration

for value in enumerate(odd):
    print(value)

To loop over a list of lists, use the following format:

`list = [['something', 4.2], ['something_else', 5.4]]`

`for this, that in list :
      expression`

To loop over a dictionary:

`dict = {'key1':value1, 'key2':value2}`

`for key, value in dict :
    expression`
    

To loop over a numpy array:

1D format:

`for x in my_array :
     expression`
     
2D format:

`for x in np.nditer(my_array) :
     expression`

To loop over a dataframe:
 
`for label, row in filename.iterrows() :
      expression that uses label and row information`

## Chapter 5: Hacker Statistics

### Random number generators
`np.random.seed(#)` - sets seed, makes your results reproducible between simulations

`np.random.rand(#, #)` - generate random float between first and second arguments. If no arguments are provided, it will generate a float between 0 and 1

`np.random.randint(#, #)` - generate random integer between specified arguments

