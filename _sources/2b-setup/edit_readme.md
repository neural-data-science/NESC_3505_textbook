# Edit the README File
Once you have the README file open in the VS Code editor, add some text to it. Something like `[your name] was here`. Save the modified file (File -> save from the menu, or Ctrl-S on Windows or Cmd-S on Mac). 

## Preview Your Changes in Markdown

VS Code has built-in support for Markdown. For example, you may have noticed the *syntax highlighting* in the README file: for example, the headings, bold text, links, etc. are all highlighted in different colours. This is because VS Code recognizes that the file is written in Markdown, and it knows how to highlight the different elements of Markdown. We will see that VS Code does this for Python as well, but for now we're just interested in Markdown.

While the syntax highlighting is nice, we are still viewing the "raw" markdown, not how it would appear when formatted. When you first viewed the README file on the GitHub website, you would have seen it formatted nicely --- rather than seeing `#` symbols, you would have seen a large heading. Rather than seeing the `**` symbols, you would have seen bold text. And so on.

VS Code also has a built-in Markdown previewer. To see it, click on the `Open Preview to the Side` icon in the top right corner of the editor window (note that there is a row of icons above this, that aren't specific to the README file. Just move your cursor around and read the little tips that pop up, until you find the Preview one). This will open a second window beside the README file, which shows a preview of the file. As you scroll through the file in one window, the other view will scroll as well. The preview is another tab in your VS Code Editor, so when you're done with it you can click the `x` in that tab to close it.

## Commit Your Changes to `README.md`

If you look at the Source Control icon in the Activity Bar (the third icon from the top, with the three circles and two lines), you'll see that it has a number 1 beside it. This means that there is one file that has been changed, but not yet committed. Click on the Source Control icon to open the Source Control panel. You'll see a list of files that have been changed, under `Changes`. In this case, there is only one file, `README.md`. Click  `+` icon beside the file name to "stage" it. This means that you want to commit this file. Once you've staged the file, it moves to the `Staged Changes` section. You can stage multiple files at once, if you want to commit them all together. Right now we just have one file to commit. 

Next, write a commit Message in the box above the blue `Commit` button. Remember, this has a 50 character limit and should succinctly describe the change you made to the file. For example, you could write, "Add my name to README file". Once you've written your commit message, click the blue `Commit` button. This will commit your changes to the file, but it will not push them to GitHub. You can see that the number beside the Source Control icon has changed to 0, because there are no more changes to commit. As well, the blue button's label changes to `Sync Changes`. 

## Push Your Changes to GitHub

Pushing to GitHub is as simple as clicking that `Sync Changes` button. Do that now, and you're done!

```{note}
GitHub has a robust system for going "back in time" through the commit history of a project that can allow you do undo changes and restore earlier versions of files. We're not going to explain it now, and we hope you don't need to do it during this course. But for now, just know it's possible and of course there are extensive resources on the Internet about how to do it.
```

## Summary: GitHub workflow

Remember that the GitHub workflow is as follows, and you should develop the habit of doing these steps regularly:
- Make changes to a file on your computer
- Save the file
- Commit the file to your local copy of the repository
- Push the file to GitHub
- Repeat



