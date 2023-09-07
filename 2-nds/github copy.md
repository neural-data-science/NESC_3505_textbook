```{figure} images/github_octocat.png
---
align: left
width: 65px
```
# GitHub

Recall that [**GitHub**](https://github.org) is a service that provides online hosting for software development. 

## Repositories

The core of GitHub are **repositories**. These are, essentially, projects. One can create a repository (or, if you're cool, a "repo") and upload source code for a project to it, including virtually any type of file. This could include source code, image files, Markdown files, Jupyter notebooks, Microsoft Word documents, or anything else. Generally, everything in a repository is relevant to a specific project. So if you are building a software application, all the files necessary for that application are stored in its GitHub repository. Repositories are owned either by an individual (technically, by an individual GitHub account), or by a GitHub organization (any GitHub user can create an organization, for example for a team, project, company, etc.). The repository's owner can add other people to the repository and control access to it. Access control includes determining who can make changes to the repository, as well as whether it is public (visible to anyone on the web), or private (visible only to authorized accounts).

Typically when working on a project, files are edited on an individual's computer (or a cloud-based service like JupyterHub). To do this, the individual would first **clone** (copy) the repository to their own computer (using a program called `git`), and then edit the file(s) as necessary. After each change to the project is made, the individual saves the file, and then (in a separate step) performs a **commit** to their local copy of the repository. The commit includes a short written description of the change, which helps track the history of changes and, in some cases, why those changes were made. After the change (or a set of changes) is completed, the individual can then **push** the changes from their local computer to the central GitHub repository in the cloud, which is typically called the **master**.

## Branching

Since the master version of the repository is, in a sense, the "one true" version of the project, it is not always a Good Idea to routinely merge every change into the master branch as one works. Especially when one is working on software that is already "live" and in use, pushing all changes directly to the master runs the risk of breaking something and causing all kinds of trouble. Instead, the best practice is to create a **branch** of the master. A branch is simply a "snapshot" copy of the master as of the time the branch was made (technically, the master is also considered a branch, so you may come across the term "master branch"; but generally if someone says "branch", they mean a working copy of the master). An individual can work on making changes to their branch, test these and make sure nothing breaks, and then merge the branch back into the master. Branches can also help minimize conflicts between developers, especially if one developer makes an error or otherwise decides they need to "rewind" their changes to a previous version. If everyone was working directly on the master, then rewinding to a particular date to undo one's own changes might also undo changes that another developer made to another part of the project. Branches provide a level of organization and control to ensure that each developer's work is "sandboxed" and safe from the activities of other contributors.

```{figure} images/git_workflow.png
---
align: left
---
Git workflow, showing separate branches made by two developers working simultaneously. At each merge, git will check for any conflicts between changes in the branch, and the master branch, and highlight these for the developer to resolve.
```

## Collaboration

GitHub provides features that facilitate collaboration. One feature, already noted, is that when multiple people are working on a project, GitHub provides a mechanism for identifying and resolving conflicts (e.g., two people attempt to push different changes to the same file). As well, rather than pushing every change directly to the master repository, many collaborative workflows instead involve **pull requests**, whereby the author "proposes" their change to the other contributors of the repository, often leading to discussion and suggestions for further changes. Only once the owners of the repository agree with the change is the pull request approved and merged into the master version.

This highlights the fact that GitHub is also a social platform to facilitate collaboration on a project. Pull requests provide a way for contributors to discuss the best way to approach solving a problem, and — since all pull requests are saved as part of the repository — provides a history of the discussions that led to each decision. GitHub also allows people to report issues with the software. Issues can be reported by users of the software, who are not involved in its development but wish to bring a problem to the attention of the developers, so that it can be fixed. All active issues appear on the repository's GitHub page, and when fixed, they can be marked as "resolved" and the person who reported the issue will be notified. As you might imagine, an issue report in many cases will lead to a developer working on a solution, then generating a pull request to address the issue. GitHub easily allows pull requests to be associated with specific issues, to facilitate tracking the resolution of issues.

GitHub repositories also have other useful tools for projects, including an optional wiki (which could be used for more extensive documentation) and "project boards" that allow project management through tools like to-do lists. As well, every repository has an "Insights" section that allows anyone to view the history of the project, including when changes were made, who made them, etc.. This can provide insights into who made major contributions to projects, and when active periods of development occurred.

## Software Distribution

GitHub also supports software development, and distribution, in other ways. Many software projects use GitHub as their means of distributing the software to end users, by directing them to the project's GitHub page and providing a download link. The main GitHub page for a project also allows the developer to display a file, in Markdown format, on the page, which can provide basic information and documentation about the software.

## Forking

A final important tool that GitHub provides is **forking**. Forking is almost the same as branching; it also involves making a new copy of the repository for editing. The difference is that, typically, branching is done only by the core developers of a team. Many software projects, however, are open-source, meaning that they are free for others to copy and modify. Thus someone who wanted to make a copy of a project, examine its code, and potentially adapt or modify it, or include it as part of another project they were working on, would fork the repository. Forking creates a new repository on Github, with its own URL and master branch, that is owned by the person who did the forking, rather than by the owners of the original repository. However, GitHub tracks forking, so the GitHub page for a repository will show the number of forks that have been made, and provide links to them.

### Summary: GitHub workflow

The GitHub workflow is as follows:
- Make changes to a file on your computer
- Save the file
- Commit the file to your local copy of the repository
- Push the file to GitHub
- Repeat
