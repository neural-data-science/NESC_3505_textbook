```{figure} images/github_octocat.png
---
align: left
width: 65px
```
# GitHub

[**GitHub**](https://github.org) is a service that provides online hosting for software development. It is the largest repository of source code in the world, and is widely used for software development and distribution. A core feature of GitHub is that it allows for **version control**, meaning that as source code is updated, all changes are tracked. This enables developers to track changes, potentially undo those changes if they made errors, and also work collaboratively on development; if two developers make different changes to the same part of the source code at the same time, GitHub will identify those conflicts and provide mechanisms for resolving them.

If you have ever collaborated on a Google Doc, GitHub is similar in some ways. With a Google Doc, one person can start a text document and share it with other people. Multiple people can edit the document at the same time, and the entire history of edits is tracked, so that one can review the history and see who made what changes, and the document can be reverted to a previous version if necessary. However, GitHub is a much more complex and full-featured platform for software development.

In many areas of neural data science, GitHub has become *the* platform for developing and sharing code. Many software packages for specific neuroscience applications, like EEG or MRI analysis, are hosted on GitHub. Likewise, in the world of data science, development, and startups, GitHub is a ubiquitous tool. Therefore, it's an essential tool for you to learn. We will use GitHub in this class to distribute assignments, examples, and data, and you will use it to run your code (in Codespaces), use the Copilot AI assistant, and submit your assignments, as well as to collaborate with others on team projects.

## Repositories

The core of GitHub are **repositories**. These are, essentially, projects. One can create a repository (or, if you're cool, a "repo") and upload source code for a project to it, including virtually any type of file. This could include source code, image files, Markdown files, Jupyter notebooks, Microsoft Word documents, or anything else. Generally, everything in a repository is relevant to a specific project. So if you are building a software application, all the files necessary for that application are stored in its GitHub repository. Repositories are owned by an individual (technically, by an individual GitHub account), who can add other people to the repository and control access to it. Access control includes determining who can make changes to the repository, as well as whether it is public (visible to anyone on the web), or private (visible only to authorized accounts).

Typically when working on a project, files are edited on an individual's computer (or a cloud-based service like JupyterHub). To do this, the individual would first **clone** (copy) the repository to their own computer (using a program called `git`), and then edit the file(s) as necessary. After each change to the project is made, the individual saves the file, and then (in a separate step) performs a **commit** to their local copy of the repository. The commit includes a short written description of the change, which helps track the history of changes and, in some cases, why those changes were made. After the change (or a set of changes) is completed, the individual can then **push** the changes from their local computer to the central GitHub repository in the cloud, which is typically called the **master**. GitHub also has a variety of tools to check for *conflicts* that might occur if more than one person pushes changes to the same file at the same time, for working on *branches* of the repository that allow one to make changes without fear of "breaking" the main branch, as well as opportunities to run tests on newly-committed code to help prevent errors from being introduced. GitHHub repositories also provide a variety of communication tools for tracking issues, bugs, and feature requests, and for managing the development process.

## GitHub Copilot
[GitHub Copilot](https://copilot.github.com/) is an AI assistant that can suggest code for you based on natural language prompts, as well as aiding you in understanding and debugging code. It is based on a large language model (LLM), like the well-known Chat-GPT. But while Chat-GPT is trained on a large corpus of internet material, Copilot was trained on billions of lines of code from GitHub's public repositories. Because so much code is housed there (including lots of code from academic researchers and data scientists), GitHub was able to leverage their users' data to create a powerful tool. 

## GitHub Codespaces
GitHub Codespaces is a cloud-based development environment that allows you to develop and run code on remote servers, without having to install any software on your computer. In this class we will teach you how to use Codespaces, and you will typically have the option of doing your coding via Codespaces, or on your own computer using VS Code. The Codespaces environment looks identical to VS Code (GitHub is owned by Microsoft, who make VS Code), which means you will be using the same interface regardless of whether you're working on the cloud or your own computer.

## GitHub Classroom
GitHub supports education,with free upgrades to student accounts, and a dedicated [GitHub Classroom](https://classroom.github.com/) service which allows educators to create sites for individual classes, where assignments can be distributed as repositories, with students creating branches of the assignment, working on their branch, and then submitting their work as pull requests. Using GitHub classroom is a great way to get familiar with the GitHub workflow, before you need to use it "for real".

## Web Hosting

GitHub offers a number of other features and uses. While it was originally designed for software development, a GitHub repository can serve as free cloud storage for any project and virtually any type of file (within limits; files are limited to 100 MB and repositories to 100 GB). GitHub also offers [GitHub Pages](https://pages.github.com/), which allows you to host a website in a GitHub repository; instead of the repository's URL leading to a typical GitHub page, it shows the home page of the web site. This book is hosted on GitHub, as are all of the workbooks for this course. If you are taking this course for credit, you can gain bonus points by creating a profile of your work on GitHub Pages.

## Fun Facts

[Github](https://en.wikipedia.org/wiki/GitHub) was founded by three developers in 2008, and sold to Microsoft in 2018 for US$7.5 billion, making each of its founders billionaires before the age of 40. Beyond just being a bit mind-boggling, that should tell you something about the value (literally) of the GitHub service to the tech community. GitHub [reports](https://github.com/about) having over 50 million users and over 100 million repositories as of 2020. While anyone can create a free account and host public or private repositories, GitHub derives income from premium plans oriented towards large companies.

Although GitHub makes extensive use of the software tool `git`, they are distinct entities. The open-source software tool `git` was created in 2005 by Linus Torvalds, the creator of the Linux operating system, as a tool for [**distributed version control**](https://en.wikipedia.org/wiki/Distributed_version_control). Git can be used without a GitHub account; there are alternative public hosting sites for git repositories, and one can host a repository on virtually any computer.

GitHub builds extensively the functionality of the `git` tool in its cloud hosting and collaboration services, but ultimately the core tasks of cloning, branching, pushing, and merging are all performed by the `git` application. As well, when working on one's own computer, one can either perform git commands from the command line (in a terminal), or through a variety of desktop applications, including [GitHub Desktop](https://desktop.github.com/) and [GitKraken](https://www.gitkraken.com/).

This is an example of the power of open source software. The people who created GitHub and turned it into a multi-billion dollar business did not write git, and the developers of git did not share in the profits when GitHub was sold. Nonetheless, the git developers' work ultimately enabled the largest repository and distribution hub for free software in the world — something to be proud of, even if it didn't make them rich! On the other hand, had the git developers insistent on charging people to use git, then GitHub could not have offered its services to tens of millions of people for free.

GitHub's data is [very well backed up](https://youtu.be/fzI9FNjXQ0o), and the company has a [**Disaster Response Team**](https://github.blog/2019-07-08-githubs-disaster-response-team/) that can be deployed to help recover data in the event of a disaster. GitHub's [**Arctic Code Vault**](https://archiveprogram.github.com/) is a project to preserve open-source software for 1,000 years, by storing it in a vault in the Arctic.

GitHub's logo, seen at the top of this page, is called the **Octocat**, which has become a meme in its own right, and has its own GitHub page, the [**Octodex**](https://octodex.github.com/).

```{figure} images/mountietocat.png
---
align: center
width: 400px
```
