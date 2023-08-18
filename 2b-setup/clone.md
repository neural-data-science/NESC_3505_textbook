# Clone a Repository from GitHub

This page is provided as a reference, primarily for people who are not using GitHub Classroom. If you are using GitHub Classroom, you should follow the instructions in the [Open the Repository in VS Code](./repo_in_vscode.md) page instead.

## Clone a Repository Using GitHub Desktop

Although you can clone a GitHub repository from within VS Code, it's a lot easier to do it using GitHub Desktop. If you don't already have GitHub Desktop installed, you can download it from [desktop.github.com](https://desktop.github.com/). Once you have it installed, open it up and log in to your GitHub account.

```{note}
**Before you clone a repository, read this!** GitHub Desktop by default creates a folder in your `Documents` folder to store cloned repositories. If your `Documents` folder is tied to a cloud storage service like Apple's iCloud or Microsoft's OneDrive, usind the `Documents` folder for GitHub repositories can create all kinds of problems. This is because those cloud services will often save space on your computer by removing the content of files from your computer, sotorign them in the could, and then downloading them when you need them. If you try to synchronize a local repository with GitHub and your cloud service has offloaded files to the cloud, then the content of those files will be lost. This is bad. So, if you are using a cloud storage service, you should create a new folder for your GitHub repositories that is not in your `Documents` folder. For example, you could create a folder called `GitHub` in your home directory (i.e., beside your `Documents` folder, not inside it), and use that instead.
```

Next, find the repository you want to clone on GitHub's website. To get the `github-starter-course` repository that we're starting with in this book, you can use the following URL: [https://github.com/neural-data-science/github-starter-course](https://github.com/neural-data-science/github-starter-course). Once you're on the repository's page, click the green `Code` button, and select `Open with GitHub Desktop`. This will open GitHub Desktop and prompt you to choose a location on your computer to save the repository (the default is `Documents/GitHub` --- see note about about why this location can be problematic). Once you've chosen a location, click `Clone`. This will download the repository from GitHub and save it to your computer.

## Open the Cloned Repository in VS Code

Now that you've cloned the repository, you can open it in VS Code. Open VS Code and click `File -> Open...` from the menu. Navigate to the folder where you saved the repository, and click `Open`. This will open the repository in VS Code. Now you can edit the files in the repository, and commit and push your changes to GitHub.

At this point you can jump back to the [Open the Repository in VS Code](./repo_in_vscode.md) page and continue from there.