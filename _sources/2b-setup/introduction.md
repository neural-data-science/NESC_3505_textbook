# Some Assembly Required

This is our first hands-on chapter, where you will set up the necessary accounts, and install the necessary software, to get up and running with the tools you will need in this course.

There are some platforms, like [Google Collab](https://colab.research.google.com/] (which is free to use) and [CoCalc](https://cocalc.com/) (which is nominally free but allows paid upgrades for more computing resources), that allow you to run Python code in the cloud. These are great for learning, because you can basically just go to a website and start coding. However, they are not always ideal for doing real work. For example, if you're working with real neural (or other) data, you would need to upload it to the cloud of the service provider you're using. This could be a violation of the research ethics and/or privacy laws of your institution or location, or you might have large data files that make this challenging.

## GitHub Codespaces

For working through this textbook, we provide a cloud-based solution called **GitHub Codespaces**. This is a service provided by GitHub that allows you to run a virtual machine in the cloud, and code in a web-based version of Visual Studio Code. This is a great way to get started, because you don't need to install anything on your own computer. And, because all the course materials are distributed via GitHub already, it's very easy to use these to work through the course materials. However, it can be slow, and you may run into limitations on the amount of data you can store or process. As well, Codespaces run as *containers*, which means they come pre-packages with a set of files inside them, but can't access files outside the codespace. This means it's not trivial to import new data, or use them outside of the course materials. (You can certainly do it, but teaching you how is beyond the scope of this textbook.)

## Installing and Running Python on Your Own Computer

If you want to run Python and do data science on your own computer, instead of using Codespaces, you will need to install some software. This chapter will walk you through the steps to do this. We will install **Visual Studio Code** (VS Code), a powerful code editor that will allow you to write and run Python code on your own computer. We will also install a number of other packages that are necessary in order to run Python in VS Code, and do everything taught in this course. If you start by using Codespaces, it will be easy later to switch to VS Code, because the user interface in Codespaces is virtually identical to VS Code.

The number of software tools, packages, websites, and logins required in this chapter might seem in intimidating at first. Try not to be discouraged by this; take your time and work through the steps one at a time. You may also want to watch the associated [YouTube video](https://youtu.be/tF6_xp3LU8A), which will walk you through the steps in real time with the advantage of seeing each step performed. But again, if you just want to get started with learning, you can follow the section on using Codespaces and skip the rest of this chapter.

Either way, the first thing you'll need to do is setup an account with GitHub. This is needed to access the course materials, and you'll also need it whether you use Codespaces or VS Code.
