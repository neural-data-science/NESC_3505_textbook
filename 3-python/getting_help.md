# Getting Help with Python

Python is a widely-used language and there is lots of information on the web about it. But, sometimes it's hard to know where to start! The lessons in this course will introduce you to Python, and the chapters in this book are meant as a starting point for reference. The chapters follow the DataCamp lessons, which can be handy if you remember which lesson you learned something in. However, the assignments and projects in this course are designed to make you go beyond the material as it was taught. You will inevitably need to rely on other educational resources and reference materials on the web

**Python**, and associated packages, have official documentation. The official documentation for Python is at [https://docs.python.org/3/](https://docs.python.org/3/)

Two core Python packages we'll use are NumPy and pandas.

**NumPy**'s official reference documentation is at [https://numpy.org/doc/1.19/reference/index.html](https://numpy.org/doc/1.19/reference/index.html)

**pandas**' official reference documentation is at [https://pandas.pydata.org/docs/user_guide/index.html#user-guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

However, in practice these reference guides don't provide the easiest entry point for finding the information you probably want, such as "How do I...?" or "What are the options for command X?". More often, doing a search for your question is the best way to get results.

The sites you find in those searches will likely be many, but a common one is [Stack Overflow](https://stackoverflow.com), a huge Q&A site. One of the strengths of Stack Overflow is that it allows users to vote (up or down) questions and answers, which helps in evaluating the quality of these. Stack Overflow also limits whose votes count; only the votes of registered users who have developed a positive reputation on the site are counted. Reputation is gained by asking questions that received positive votes.  

## APIs
One thing you will often find, especially if you're trying to figure out how to use a command or function, is the **application programming interface** (**API**). The API will give you the name of the command, and the different **arguments** it takes. Arguments are bits of information you provide to the command (typically inside parentheses) that are either required for the command to run, or optional extra information. For example, [this is the API for the NumPy command to compute the mean of a set of numbers](https://numpy.org/doc/stable/reference/generated/numpy.mean.html):
`numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)`

The command itself is the first part before the parentheses (`numpy.mean`) and the arguments are in the parentheses. Each argument is separated by a comma from the other arguments. Required arguments are generally first in the list, and don't include an `=` sign. The arguments with `=` signs are generally optional. The NumPy API at the link above also explains what each argument is; for simplicity here, the `a` is the set of data you want to compute the mean from (which is required; how could the function give you a mean if it didn't have data to do that from?) and the other arguments are all options that might be required to get the result you desire.

APIs may look pretty complicated at first, but they can be very helpful in breaking down a command and understanding how to use it better. By contrast, when you search the web for answers to programming questions, often you'll get example code that shows a particular way to use a function or method. This is also useful, but in order to adapt that to your problem (or understand what it's actually doing), you may want to check the API for that function to learn more.

:::{tip} 
When working from examples that you find on the web, resist the temptation to copy and paste them, and instead re-type them yourself. While you may make a few more errors (and it's slower), *it's a much better learning technique*. Although you are, hopefully, reading the code you copy, and trying to understand it, you tend to learn and retain more if you type it out yourself (just like taking notes is more effective than just reading a book or listening to a lecture).
:::

## Artifical Intelligence (AI) - Assisted Coding

There are a number of tools that can help you write code. These tools are often referred to as **artificial intelligence (AI)**-assisted coding tools. These tools can help you write code by suggesting code completions, or by suggesting code that you might want to use. They are quite remarkable and are quickly revolutionizing the way that people write code. In this class, we will primarily use GitHub Copilot, which is a plugin for Visual Studio Code. You can learn more about GitHub Copilot [here](https://copilot.github.com/).

GitHub Copilot may well replace many of the more conventional ways that both learners and experienced coders get help, as well. It generates code suggestions based on natural language input that you type directly into your code files, such as, "I want to compute the mean of a set of numbers". In the past one would conduct a Web search on a prompt like the above, then having to review and filter many possible responses, and possibly try a few before finding one that works right (especially if your need is more complicated than computing a mean). GitHub Copilot generates code suggestions directly from your prompts without all that searching and filtering, right in your code file. AI assitants can make coding much more efficient, and allow data scientitsts to focus on the more creative aspects of their work. The two biggest challenges in using AI assistants at this point in time ar, firstly, that you still need to know how what you want to do with your data, and be able to break that down into a series of component steps. This is called **programmic thinking** and is a skill that you will develop in this course. The second challenge is that AI assistants are prone to error. And as you get into more specialized needs, there may be fewer good examples of prior code in the AI assistant's training data that perform similar tasks, meaning the AI-generated code may be less accurate. Thus you still need to know how to write and read Python code, and how to debug it.

For these reasons, we will teach you how to use an AI coding assistant in this course, but we will also teach you how to code without one. This will help you develop your programmic thinking skills, and will also help you to understand the code that the AI assistant generates for you.