# Open the Repository in VS Code

```{note}
If you do not see a button to open the repository in VS Code (e.g., if you are an independent learner), you can clone it to your computer another way. Jump to the section [Clone a Repository](./clone.md), follow the instructions there, then come back to this page.
```

While still viewing the main page on the Web for the `github-starter-course` repository, click `Open in Visual Studio Code`. This will open VS Code, and you will see a message that says something like, `Cloning into 'neural-data-science-2023-24-username'...`. This means that VS Code is downloading the repository from GitHub and saving it to your computer. Once it's done, you will see a message that says `Successfully cloned 'neural-data-science-2023-24-username'`. You will also see a new window open in VS Code, with the name of the repository at the top. This is the repository you just cloned from GitHub. You can now close the browser window that was open to GitHub.

On your computer, by default the repository will be saved in `Documents/github-classroom/neural-data-science-2023-24-username`. Normally you'll access these through VS Code, but it's helpful to know where they live on your computer (and also to know not to delete them!).

```{note}
**Before you clone a repository, read this!** GitHub Classroom by default creates a `github-classroom` folder in your `Documents` folder to store cloned repositories. If your `Documents` folder is tied to a cloud storage service like Apple's iCloud or Microsoft's OneDrive, usind the `Documents` folder for GitHub repositories can create all kinds of problems. This is because those cloud services will often save space on your computer by removing the content of files from your computer, sotorign them in the could, and then downloading them when you need them. If you try to synchronize a local repository with GitHub and your cloud service has offloaded files to the cloud, then the content of those files will be lost. This is bad. So, if you are using a cloud storage service, you should create a new folder for your GitHub repositories that is not in your `Documents` folder. For example, you could create a folder called `GitHub` in your home directory (i.e., beside your `Documents` folder, not inside it), and use that instead.
```

## Explore the Repository in VS Code
The left side of VS Code contains a vertical row of icons, which is called the Activity Bar. Some of the icons there are present by default, while others represent extensions that you've installed. The top icon is the `Explorer`, which allows you to see all the files you have open. The typical way to work in VS Code is to open a particular folder (such as the folder containing a repository), in which case the Explorer will show you the files in your repository. You can click on a file to open it in the main VS Code Editor window. Click on the `README.md` file to view it in the editor.

## Edit the README File
Once you have the README file open in the VS Code editor, add some text to it. Something like `[your name] was here`. Save the modified file (File -> save from the menu, or Ctrl-S on Windows or Cmd-S on Mac). 

## Make Your First Commit

### What is a Commit?

A git **commit** means you are "committing" the changes you've made to a file to your repository. Unlike many cloud services that automatically synchronize all your changes, `git` and GitHub require that you do this manually, and explicitly. This is a bit more work than you may be used to, but it's a good habit to get into. In software development, you might try different ways of solving a problem before you find one that works. There's no point in auto-saving a bunch of failed attempts. Moreover, the history of changes you make to your code on GitHub is important, because it allows you to go back to a previous version if you discover a mistake or bug later on. So again, you might not want that history littered with a bunch of failed attempts --- you just want to *commit* the solution you decide to use to the GitHub history. You can also add changes to a number of files in a single commit, which might be useful if those files interact with each other, so that your changes to one file were also associated with changes to other files. 

Another benefit (that might feel like a hassle at first) of committing is that GitHub requires you to write a short (maximum 50 characters) **commit message** that describes the changes you've made. These become part of the history of the repository, which can be viewed by anyone with access to that repository. The message can be accompannied by a slightly longer Comment if you feel the need, but in general you only need to write a short message. Commit messages are vital to the history of a repository, because they document what changes were made when. So in general, they should be informative and descriptive. For example, if you are fixing a bug, you might write a commit message like, "Fix bug calculating mean of list". If you are adding a new feature, you might write, "New function to calculate the median of a list". If you are making a change to a file that is not code, you might write, "Add new section to README file".

### Committing is Not Pushing

When you commit changes to a file, these changes are **only saved to your local copy of the repository**. This is an additional "safety net" feature that ensures when you push changes to GitHub, that you are confident you really want to. Pushing is a separate step from committing, and it's important to understand the difference between committing and pushing. **Committing** is committing your changes to your local copy of the repository. *Pushing* is updating the repository on GitHub with the commits that you have made to your local copy. 

You should build good habits for committing and pushing right from the start. The danger is that you do a lot of work without committing, and end up with a few challenges. One is that if you've made many changes, you may not remember them all, and regardless it would be too much to describe in a 50 character message. For another, if you made many changes before committing, your commit history becomes less helpful if you discover an error and need to backtrack. Large commits also pose challenges in pushing to GitHub --- they can take a very long time, and encouter errors. So it's best to commit often, and push regularly.

The habit you should get into is committing each time you think you've solved a problem or made meaningful progress on a project or assignment. When you're working, it would be a good idea to make a commit at least every hour, if not more frequently. If you have trouble establishing this habit, try setting a 20 minute timer on your phone, and commit every time it goes off. It doesn't hurt to push each commit as you make it.




..
- explain save vs commit vs. push/sync
- importance of regular commits, period pushes

## Create a New Markdown File
One of the "next steps" at the bottom of the README file is to create a new Markdown file in the repository. To do this in VS Code, click on the `Explorer` icon in the Activity Bar. If this was already selected, then clicking will hide the list of files in the repository. Oops. If that happened, click the `Explorer` icon again to reveal the list of files. But if you already see the list of files (which is just the `README.md` file and the `.git` folder), you're good to go.

To create a new file, right-click on the top-level folder (`github-starter-course`), and select `New File...`. In the explorer, you'll see a blank space where you can type the name of the new file. Call it `test_file.md`. Adding `.md` is important because that will cause VS Code to automatically recognize it as a Markdown file.

This will open the new, empty Markdown file in the main editor window of VS Code. Add some text, following the instructions in the README file, writing something about, "what you learned and what you are still confused about! Experiment with different styles!"