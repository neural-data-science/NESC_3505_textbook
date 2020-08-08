# Lesson 5: Merging DataFrames with pandas

[View this lesson on datacamp](https://learn.datacamp.com/courses/merging-dataframes-with-pandas)

## Chapter 1: Preparing Data
To read a single file into a dataframe, use the following format:

`variable = pd.read_csv('filename.csv')`

It is also possible to use a for loop to read in multiple files:
First, create a list of the files
filenames = ['filename1.csv', 'filename2.csv', 'filename3.csv']

dataframes = []

`for filename in filenames:
    dataframes.append(pd.read_csv(filename))`

#create a list of the files
filenames = ['filename1.csv', 'filename2.csv', 'filename3.csv']
#create an empty list to append the files to
dataframes = []

for filename in filenames:
    dataframes.append(pd.read_csv(filename))

|Method                    |Funciton               |
|--------------------------|-----------------------|
|`.sort_index()`           |sort index - default is by ascending order, specifying `ascending=False` reverses order|
|`.sort_values()`          |sort column values by increasing numerical order by default|
|`.reindex()`              |reorders rows based on a new index column|
|`.ffill()`                |forward fill; replace NaN with last preceding non-null value|
|`.str.replace('', '')`    |replace first specified string with second down a column|
|`.multiply()`             |performs multiplication along specified column/row and broadcasts output|

