# Getting Help on an Assignment 

**Note**: *This section applies only to students following this textbook as part of a course. The authors of the book do not have the capcity to provide everyone who finds the book on the internet with individualized help.*

The primary way that you will interact with the teaching team while working on an assignment is via a GitHub [**Pull Request**](https://docs.github.com/en/pull-requests). For each assignment, a pull request called  `Feedback` is automatically created for you by GitHub Classroom. This is how you should pose questions about the assignment to the teaching team. 

In a typical GitHub workflow, a Pull Request is a series of changes to a a repository, combined with comments from contributors. It's called a "Pull Request" because the idea is that someone could build some new feature, bugfix, etc. for a project and request that it be merged (pulled) into the main project. Pull requests allow developers to view the proposed code and comment on it, suggest additional changes, etc. before the code is accepted and merged into the main project. A cool thing about the Comments in Pull Requests is that you can tag a specific person, *and* a specific line(s) of code in a file. 

In GitHub Classroom, we are using the Pull Request workflow in a slightly different way. Your assignment isn't part of a bigger project (until we get to team assignments), but Pull Requests is simply a useful tool for chatting back and forth, within a repository. Because you can tie a comment to specific lines of code, it makes it quite easy to ask your TA deattiled questions and have them immediately be able to see where in your file the question is coming from.

Just keep in mind that what GitHub calls "Comments", you can use to ask questions.

## Creating a Comment to Get Help

You can create a comment either on the GitHub website, or directly from within VS Code. We recommend working within VS Code, and so that's what we will explain here. 

With your assignment repository open in VS Code, find the `GitHub Pull Request` icon (note: this icon will only be visible if you are working on a GitHub repository in VS Code that has an existing Pull Request. Thus should already be the case for course assignments, but something to keep in mind if you're working with other repositories). Click on the icon to open the Pull Request. You will see a list of all the Pull Requests for the repository. There should be one called `Feedback`. Click on that one to open it.

If you click on the name of the Pull Request (`Feedback`) in the top left, you will see the same view that you would see on GitHub's website, with the history of changes and comments. Below that is a list of modified files, and below that is the history of commits (changes) that have been made to the repository.

Below that segment of the window is another region that has a box which reads "Leave a comment". This is where you can type your question. You can also @mention someone (e.g., your TA) to make sure they see your comment. However, this will only create a general comment in the repository. There is a better way to create a comment that is tied to a specific line of code.

## Creating a Comment on a Specific Line of Code

First off, make sure that you have committed all changes in the file that you have a question about, and pushed them to GitHub. This is important because you want to ensure that your question is based on the most recent version of your code.

Open the file that you have a question about, and find the line that you have a question about. In between the line numbers that appear along the left side of the window, and the line itself, there is a vertical bar that is normally grey. If you position your cursor over this line, you should see a `+` sign appear. Click on the `+` sign, and you will see a box that says, "Start discussion". **@mention your TA**, otherwise they won't get a notification of your question. Then type your question in that box, and click the blue `Add Comment` button. This will create a comment that is tied to that specific line of code. The comment will continue to appear in your file, which can be annoying if you're trying to continue working. To hide it, click on the `^` in the top right corner of the comment. Avery line in your file that has a comment associated with it will show a distinctive icon (like a chat bubble) in the left margin. You can click on that icon to toggle revealing/hiding the comment.

## Getting a Response to Your Question

Your TA will respond to your question by creating a comment in the same way that you did. You will receive a notification in VS Code, and you can click on the notification to see the comment. You can then respond to the comment, and the conversation can continue.

