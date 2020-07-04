# Getting Help with Python

Python is a widely-used language and there is lots of information on the web about it. But, sometimes it's hard to know where to start!

**Python**, and associated packages, have official documentation. The official documentation for Python is at [https://docs.python.org/3/](https://docs.python.org/3/)

Two core Python packages we'll use are NumPy and pandas.

**NumPy**'s official reference documentation is at [https://numpy.org/doc/1.19/reference/index.html](https://numpy.org/doc/1.19/reference/index.html)

**pandas**' official reference documentation is at [https://pandas.pydata.org/docs/user_guide/index.html#user-guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

However, in practice these reference guides don't provide the easiest entry point for finding the information you probably want, such as "How do I...?" or "What are the options for command X?". More often, doing a search for your question is the best way to get results.

One thing you will often find, especially if you're trying to figure out how to use a command or function, is the **application programming interface** (**API**). The API will give you the name of the command, and the different **arguments** it takes. Arguments are bits of information you provide to the command (typically inside parentheses) that are either required for the command to run, or optional extra information. For example, [this is the API for the NumPy command to compute the mean of a set of numbers](https://numpy.org/doc/stable/reference/generated/numpy.mean.html):
`numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)`

The command itself is the first part before the parentheses (`numpy.mean`) and the arguments are in the parentheses. Each argument is separated by a comma from the other arguments. Required arguments are generally first in the list, and don't include an `=` sign. The arguments with `=` signs are generally optional. The NumPy API at the link above also explains what each argument is; for simplicity here, the `a` is the set of data you want to compute the mean from (which is required; how could the function give you a mean if it didn't have data to do that from?) and the other arguments are all options that might be required to get the result you desire.

APIs may look pretty complicated at first, but they can be very helpful in breaking down a command and understanding how to use it better. By contrast, when you search the web for answers to programming questions, often you'll get example code that shows a particular way to use a function/ This is also useful, but in order to adapt that to your problem (or understand what it's actually doing), you may want to check the API for that function to learn more.

```{admonition} Pro Tip:
When working from examples that you find on the web, resist the temptation to copy and paste them, and instead re-type them yourself. While you may make a few more errors (and it's slower), *it's a much better learning technique*. Although you are, hopefully, reading the code you copy, and trying to understand it, you tend to learn and retain more if you type it out yourself (just like taking notes is more effective than just reading a book or listening to a lecture).
```
