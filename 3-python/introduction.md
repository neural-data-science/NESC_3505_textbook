# Introducing Python

This chapter covers the material for about the first month of the course, which is a basic introduction to Python. This is not an introduction to computer science. Our focus is on how to use Python as a tool for working with data. As such, our focus is on:
- learning the fundamentals of Python
- learning the fundamentals of programming logic
- understanding and debugging code
- using Python for data science, including:
    - reading data
    - manipulating/processing data (e.g., extracting specific data, splitting data according to variables, applying functions, combining data)
    - exploratory data analysis
    - basic statistical analyses of data sets

Each section of this chapter is a *lesson*, which will probably take you about 1-1.5 hours to complete. Each lesson is a Jupyter notebook, and you can download all of the Jupyter notebooks (and any necessary data files) for each chapter from [the course's GitHub page](https://github.com/neural-data-science). If you're taking the course at Dalhousie University, you can also get the notebooks from the course GitHub Classroom. Video walkthroughs of each lesson are available on the course [YouTube channel](https://www.youtube.com/playlist?list=PLtfEWMIgWS22MMZjPIzBRE2cHhMcvEKwp).

The best way to work through this material is to watch the video while working through the lesson yourself in VS Code, and be [typing in the code](../1-intro/actually_write_code.md) (not cutting and pasting) to follow along with the instructor. The copies of these chapters in this textbook serve more as a reference that you can check back with later.

## Deactivate AI for Now
If you followed the instructions in the previous chapter, you will have set up VS Code to use the GitHub Copilot AI assistant. However, for these first lessons we recommend that you turn off Copilot. This is because the first lessons are designed to teach you the fundamentals of Python, and we want you to be typing in the code yourself, taking the time to understand it, and even making errors that you need to debug. This is how you learn. If you use Copilot, you will be tempted to just cut and paste the code, and you won't learn as much. At best, it will just ]be generating a lot of suggested code that distracts you from the code you're trying to write.

You can turn off Copilot by clicking on the Copilot icon (which looks kind of like a cute alien face) in the bottom left corner of the VS Code window, and then clicking on the "Turn off" button. If you're not sure which button this is, just slowly move your cursor over the bottom right icons until you see `Deactivate Copilot` You can turn it back on again later, when you want to, by clicking that same icon again.

```{note}
After working through the lessons, either you can keep going with the course materials, or you may want to practice and reinforce the basics you've learned. If you want more practice with basic Python, try free sites like [Coding Bat](https://codingbat.com/python) or [HackerRank](https://www.hackerrank.com/domains/python).
```

## Origins of this material

The lessons introducing Python are adapted from a workshop created by the [Software Carpentry](http://swcarpentry.github.io/python-novice-gapminder/index.html) foundation. Software Carpentry releases their material as open source, under a license [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) that allows others to re-use and adapt the material, as long as the original source is attributed as I'm doing here.

The lessons use freely-available open source data from [Gapminder](https://www.gapminder.org), an independent Swedish foundation whose mission is to "fight devastating ignorance with a fact-based worldview everyone can understand." Gapminder is perhaps most famous for the TED talks given by its co-founder, the late Dr. Hans Rosling (the other founders were Ola Rosling and Anna Rosling Rönnlund). Dr. Rosling's TED talk, [*The best statistics you’ve ever seen*](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen?language=en), became one of the most watched TED talks ever (nearly 15m views as of Feb. 4, 2021). The Gapminder data we will be working with here are a subset of those used in Dr. Rosling's talk. Specifically, the data are gross domestic product (GDP) of countries from around the world, over a time period from 1952 – 2007.

While we could introduce Python with virtually any data (including neuroscience data),  the Gapminder data are relatively easy to understand without deep technical knowledge of a domain (GDP is a measure of a country's wealth, and the data reflect how this change over time), the data files are open source and so support open sharing and transparency in science, and Dr. Rosling's talks provide a colorful and interesting introduction to the data. 

 The original Software Carpentry workshop was created by [Christina Koch](https://software-carpentry.org/team/#koch_christina), [Milad Fatenejad](https://software-carpentry.org/team/#fatenejad_milad), [Tom Wright](https://software-carpentry.org/team/#wright_tom), [Paul Ivanov](https://software-carpentry.org/team/#ivanov_paul), [Greg Wilson](https://software-carpentry.org/team/#wilson_greg), and [Jens Nöckel](https://software-carpentry.org/team/#nockel_jens). The original workshop was created in 2014, and has been updated since then. 
 
 We have adapted the Software Carpentry (SC) version of the workshop based on experience teaching it, and finding that some parts of the SC workshop were unclear, or assumed certain background knowledge (particularly mathematics) that was not universally held by our target audience, or that concepts in the SC workshop were presented in a sequence that was not intuitive to us. A section on pandas dataframes has also been added. We have great respect for the SC organization and its aims, and adapting and customizing the workshop is in the spirit of the open source movement and open educational resources.
