# GitHub Classroom

If you are taking this course for credit at Dalhousie University, you need to follow the instructions in this document to set up your GitHub account and join the course organization. If you are reading the textbook as an independent learner, you can still obtain all of the course materials for free, but the instructions are slightly different. See the [independent learner instructions](./github_materials.md) for more information. However, if you are a Dalhousie student, be sure to work from the GiHub classroom, because that is also where you will receive and submit assignments. Also, some of the materials may be updated specifically for the course, before they are updated in the textbook.

Before you can do the steps here, you need to have already [created a GitHub account](./github.md), and installed both [GitHub Desktop](./github_desktop.md) and [VS Code](./vscode.md).

To access the GitHub classroom for this course, find the link provided by your instructor on the course LMS (Brightspace). Click that link and follow the instructions to link your GitHub account to the classroom. As discussed before, it's required that your GitHub account shows your real name, so that your instructor can identify you. 

Once you have joined the classroom, you will see a list of lessons and assignments. Each assignment will have a link to a GitHub repository. Click the link for the first assignment. You will be taken to a page that asks you to select your name. Select it if it appears, otherwise you can continue without selecting your name. You'll then see a page that tells you it's cloning the GitHub Starter Course repository. Refresh the page until you see the message, "You're ready to go!". You should see two options at that point: one is a link to github.com, and the other is a button that says "Open in Visual Studio Code". We'll use the button later, but for now let's click the web link to see what a repository looks like in its native environment, on the GitHub website.

## Exploring the GitHub Repository view

When you open the assignment repository, you will see the default view of the repository, which is basically what every repository on GitHub looks like. It will look something like this:
![](./images/github_repo.png)

At the top left of the window is the name of the organization repository you are currently looking in. Note that when you use GitHub classroom, all of the repositories you clone from there will be owned by the organization associated with the course (e.g., `neural-data-science-2023-24`), and the name of your copy of the repository will have your GitHub user name attached to the end. Below this are tabs including `Code` (which you are currently viewing), `Issues`, `Pull requests`, `Actions`, `Projects`, `Wiki`, `Security`, and `Insights`. We'll explore some of these later, but for now we'll focus on the `Code` tab.

Below the tabs is the name of the repository, and then a few buttons. We'll ignore the buttons for now. Below these is a list of all the files in this repository. This first one is quite bare, with only a `.github` folder (which you should ignore and never mess with; it just contains the files GitHub uses to manage and sync the repository), and a file called `README.md`. The contents of the README file are displayed below the list of files. This is the default view of a repository, and it's standard for every repository to have a `README.md` file that explains what the repository is for and about, if not more detailed information (e.g., documentation). The `.md` extension indicates that this is a [Markdown](../2-nds/markdown.md) file, which is a simple text format that allows you to add formatting to text files. You can read more about Markdown [here](https://guides.github.com/features/mastering-markdown/).

If you scroll down the page, you will see the contents of the README file. Read it over, and explore some of the links if you're interested. The content is actually useful, and from here on we'll assume you've read this material and understand it.

The README file ends with a list of *Optional next steps*. You should do all of these steps, and then submit the assignment. We'll walk you through some of this, but some of it is left for you to figure out; the README provides you with all the resources you need to do all of these tasks.

## Open the Repository in VS Code

While still viewing the repository main page, click "Open in Visual Studio Code". This will open VS Code, and you will see a message that says something like, "Cloning into 'neural-data-science-2023-24-username'...". This means that VS Code is downloading the repository from GitHub and saving it to your computer. Once it's done, you will see a message that says "Successfully cloned 'neural-data-science-2023-24-username'". You will also see a new window open in VS Code, with the name of the repository at the top. This is the repository you just cloned from GitHub. You can now close the browser window that was open to GitHub.

## Explore the Repository in VS Code

The left side of VS Code contains a vertical row of icons, which is called the Activity Bar. Some of the icons there are present by default, while others represent extensions that you've installed. The top icon is the `Explorer`, which allows you to see all the files you have open. The typical way to work in VS Code is to open a particular folder (such as the folder containing a repository), in which case the Explorer will show you the files in your repository. You can click on a file to open it in the main VS Code Editor window. Click on the `README.md` file to view it in the editor.

