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




## Create a New Markdown File
One of the "next steps" at the bottom of the README file is to create a new Markdown file in the repository. To do this in VS Code, click on the `Explorer` icon in the Activity Bar. If this was already selected, then clicking will hide the list of files in the repository. Oops. If that happened, click the `Explorer` icon again to reveal the list of files. But if you already see the list of files (which is just the `README.md` file and the `.git` folder), you're good to go.

To create a new file, right-click on the top-level folder (`github-starter-course`), and select `New File...`. In the explorer, you'll see a blank space where you can type the name of the new file. Call it `test_file.md`. Adding `.md` is important because that will cause VS Code to automatically recognize it as a Markdown file.

This will open the new, empty Markdown file in the main editor window of VS Code. Add some text, following the instructions in the README file, writing something about, "what you learned and what you are still confused about! Experiment with different styles!"