# Editing, Pushing, and Committing

Unlike many cloud services that automatically synchronize all your changes, the `git` application and GitHub cloud service require that you do this manually, and explicitly. This is a bit more work than you may be used to, but it's a good habit to get into. When coding, you might try different ways of solving a problem before you find one that works. There's no point in auto-saving a bunch of failed attempts. Moreover, the history of changes you make to your code on GitHub is important, because it allows you to go back to a previous version if you discover a mistake or bug later on. So again, you might not want that history littered with a bunch of failed attempts --- you just want to *commit* the solution you decide to use to the GitHub history. 

## What is a Commit?

A git **commit** means you are "committing" the changes you've made to a file to your repository. You can also add changes to a number of files in a single commit, which might be useful if those files interact with each other, so that your changes to one file were also associated with changes to other files. 

Another benefit (that might feel like a hassle at first) of committing is that GitHub requires you to write a short (maximum 50 characters) **commit message** that describes the changes you've made. These become part of the history of the repository, which can be viewed by anyone with access to that repository. The message can be accompannied by a slightly longer Comment if you feel the need, but in general you only need to write a short message. Commit messages are vital to the history of a repository, because they document what changes were made when. So in general, they should be informative and descriptive. For example, if you are fixing a bug, you might write a commit message like, "Fix bug calculating mean of list". If you are adding a new feature, you might write, "New function to calculate the median of a list". If you are making a change to a file that is not code, you might write, "Add new section to README file".

## Committing is Not Pushing

When you commit changes to a file, these changes are **only saved to your local copy of the repository**. This is an additional "safety net" feature that ensures when you push changes to GitHub, that you are confident you really want to. Pushing is a separate step from committing, and it's important to understand the difference between committing and pushing. **Committing** is committing your changes to your local copy of the repository. *Pushing* is updating the repository on GitHub with the commits that you have made to your local copy. 

You should build good habits for committing and pushing right from the start. The danger is that you do a lot of work without committing, and end up with a few challenges. One is that if you've made many changes, you may not remember them all, and regardless it would be too much to describe in a 50 character message. For another, if you made many changes before committing, your commit history becomes less helpful if you discover an error and need to backtrack. Large commits also pose challenges in pushing to GitHub --- they can take a very long time, and encouter errors. So it's best to commit often, and push regularly.

The habit you should get into is committing each time you think you've solved a problem or made meaningful progress on a project or assignment. When you're working, it would be a good idea to make a commit at least every hour, if not more frequently. If you have trouble establishing this habit, try setting a 20 minute timer on your phone, and commit every time it goes off. It doesn't hurt to push each commit as you make it.

In the next section, we'll put this into practice.

## Summary: GitHub workflow

The GitHub workflow is as follows:
- Make changes to a file on your computer
- Save the file
- Commit the file to your local copy of the repository
- Push the file to GitHub
- Repeat
