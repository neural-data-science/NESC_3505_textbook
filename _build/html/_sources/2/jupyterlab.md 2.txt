```{figure} images/jupyter_logo.svg
---
align: left
width: 65px
```
# JupyterLab

[**JupyterLab**](https://jupyterlab.readthedocs.io/en/stable/) is a full-fledged *environment* for working with Jupyter notebooks, that runs through a web browser. It allows you to navigate the filesystem on the computer it's running on; and open, edit, and run not only Jupyter notebook files, but other types of files (like text files); access the documentation for the language you are using; and use a terminal to access the command line. You can have many windows open at once, and arrange them in a tabbed environment.

The example below shows the list of files in the current directory on the left, an open Python notebook file in the middle, with a terminal below it, and on the right the launcher (which allows you to create new files and terminal windows), and the JupyterLab documentation.   

```{figure} images/jupyterlab.png
---
align: left
width: 600px
```

In this course, virtually all of your work will be performed in JupyterLab.

## JupyterHub

JupyterLab can be run and installed on any Mac, Windows, or Linux computer. However, to avoid the pain of setup and to facilitate your work (including submitting and grading work), we have set up a server that you will connect to through a web browser on your own computer, and log in to with a personal account.

Behind the scenes, [JupyterHub](https://jupyter.org/hub) is the service that's running on a server somewhere that makes this happen. You really don't need to know much about JupyterHub, except that we use the term to mean "the server you connect to to run JupyterLab".
