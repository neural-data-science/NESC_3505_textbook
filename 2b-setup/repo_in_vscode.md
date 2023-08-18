# Open the Repository in VS Code

While still viewing the main page on the Web for the `github-starter-course` repository, click `Open in Visual Studio Code`. This will open VS Code, and you will see a message that says something like, `Cloning into 'neural-data-science-2023-24-username'...`. This means that VS Code is downloading the repository from GitHub and saving it to your computer. Once it's done, you will see a message that says `Successfully cloned 'neural-data-science-2023-24-username'`. You will also see a new window open in VS Code, with the name of the repository at the top. This is the repository you just cloned from GitHub. You can now close the browser window that was open to GitHub.

```{note}
If you do not see a button to open the repository in VS Code, you can click the green `Code` button, select the `Codespaces` tab, and then `Create codespance on main`. A Codespace is an environment very similar to VS Code, but runing in the cloud rather than on your computer. This may however cost you money if you don't have a verified student account. Your other alternative is to skip to the section [Clone this Repository](./clone.md)
```

## Explore the Repository in VS Code
The left side of VS Code contains a vertical row of icons, which is called the Activity Bar. Some of the icons there are present by default, while others represent extensions that you've installed. The top icon is the `Explorer`, which allows you to see all the files you have open. The typical way to work in VS Code is to open a particular folder (such as the folder containing a repository), in which case the Explorer will show you the files in your repository. You can click on a file to open it in the main VS Code Editor window. Click on the `README.md` file to view it in the editor.

### Edit the README File
Once you have the README file open in the VS COde editor, add some text to it. Something like `[your name] was here`. Save the modified file (File -> save from the menu, or Ctrl-S on Windows or Cmd-S on Mac). 

### Make Your First Commit
A git **commit** means you are "committing" the changes you've made to a file to your repository...
- explain save vs commit vs. push/sync
- importance of regular commits, period pushes

## Create a New Markdown File
One of the "next steps" at the bottom of the README file is to create a new Markdown file in the repository. To do this in VS Code, click on the `Explorer` icon in the Activity Bar. If this was already selected, then clicking will hide the list of files in the repository. Oops. If that happened, click the `Explorer` icon again to reveal the list of files. But if you already see the list of files (which is just the `README.md` file and the `.git` folder), you're good to go.

To create a new file, right-click on the top-level folder (`github-starter-course`), and select `New File...`. In the explorer, you'll see a blank space where you can type the name of the new file. Call it `test_file.md`. Adding `.md` is important because that will cause VS Code to automatically recognize it as a Markdown file.

This will open the new, empty Markdown file in the main editor window of VS Code. Add some text, following the instructions in the README file, writing something about, "what you learned and what you are still confused about! Experiment with different styles!"