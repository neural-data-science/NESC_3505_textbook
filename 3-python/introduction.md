# Introducing Python

This chapter covers the material for about the first month of the course, which is a basic introduction to Python. This is not an introduction to computer science. Our focus is no how to use Python as a tool for working with data. As such, our focus is on:
- learning the fundamentals of Python
- learning the fundamentals of programming logic
- using Python for data science, including:
    - reading data
    - manipulating/processing data (e.g., extracting specific data, splitting data according to variables, applying functions, combining data)
    - exploratory data analysis
    - basic statistical analyses of data sets

Each section of this chapter is a *lesson*, which will probably take you about 1-1.5 hours to complete. Each lesson is a Jupyter notebook, and you can download all of the Jupyter notebooks (and any necessary data files) for each chapter from GitHub. Video walkthroughs of each lesson are available on the course [YouTube channel](https://www.youtube.com/playlist?list=PLtfEWMIgWS22MMZjPIzBRE2cHhMcvEKwp).

The best way to work through this material is to watch the video while working through the lesson yourself in VS Code, and be [typing in the code](../1-intro/actually_write_code.md) (not cutting and pasting) to follow along with the instructor. The copies of these chapters in this textbook serve more as a reference that you can check back with later.

```{note}
After working through the lessons, either you can keep going with the course materials, or you may want to practice and reinforce the basics you've learned. If you want more practice, try free sites like [Coding Bat](https://codingbat.com/python) or [HackerRank](https://www.hackerrank.com/domains/python).
```

## Origins of this material

The lessons introducing Python are adapted from a workshop created by the [Software Carpentry](http://swcarpentry.github.io/python-novice-gapminder/index.html) foundation. It uses freely-available open source data from [Gapminder](https://www.gapminder.org), an independent Swedish foundation whose mission is to "fight devastating ignorance with a fact-based worldview everyone can understand." Gapminder is perhaps most famous for the TED talks given by its co-founder, the late Dr. Hans Rosling (the other founders were Ola Rosling and Anna Rosling Rönnlund). Dr. Rosling's TED talk, [*The best statistics you’ve ever seen*](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen?language=en), became one of the most watched TED talks ever (nearly 15m views as of Feb. 4, 2021). The Gapminder data we will be working with here are a subset of those used in Dr. Rosling's talk. Specifically, the data are gross domestic product (GDP) of countries from around the world, over a time period from 1952 – 2007.

While we could introduce Python with virtually any data (including neuroscience data),  the Gapminder data are relatively easy to understand without deep technical knowledge of a domain (GDP is a measure of a country's wealth, and the data reflect how this change over time), the data files are open source and so support open sharing and transparency in science, and Dr. Rosling's talks provide a colourful and interesting introduction to the data. We have adapted the Software Carpentry (SC) version of the workshop based on experience teaching it, and finding that some parts of the SC workshop were unclear, or assumed certain background knowledge (particularly mathematics) that was not universally held by our target audience, or that concepts in the SC workshop were presented in a sequence that was not intuitive to us. We have great respect for the SC organization and its aims, and adapting and customizing the workshop is in the spirit of the open source movement and open educational resources.
