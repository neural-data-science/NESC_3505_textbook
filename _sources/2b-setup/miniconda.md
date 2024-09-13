# Miniconda

:::{note}
This step is an optional *alternative* to installing Anaconda as described in the previous section. If you already installed Anaconda, you can skip this step and go to the next section.
:::

## What is Miniconda?

Miniconda is a minimal installer for conda, a package manager, environment manager, and Python distribution. It is much smaller than Anaconda, because it only installs the conda package manager and Python. You can then install the packages you need, when you need them, using conda. This is a good option if you want more control over the packages you install, or if you have limited disk space.

One of the nice things about Miniconda being a package manager, is that you can create a Python *environment* that contains a specific version of Python, and specific versions of the packages you need. This is useful if you are working on multiple projects that require different versions of Python or different packages. You can create a new environment for each project, and switch between them as needed. In this course, you'll only need to work with one environment however.

The other nice thing about Miniconda is that you can define all the packages you want in an environment using a text file. This makes it easy to install all the packages you need, and also to share your environment with others. This is a great way to do reproducible research, because along with sharing your data and analysis code, you can also share the exact version of Python and all the packages you used. This is important because, over time, packages change, and the precise syntax of the code may change. Thus, others could download your analysis code, but not be able to run it if they were using a different version of a package than you were. By sharing the environment, you ensure that they are using the same version of Python and all the packages you used.

## Download and Install Miniconda

To install Miniconda, you need to download the installer from the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html). You should download the installer for the latest version of Python 3, and for the operating system you are using. **Be sure to install the version whose name ends in `pkg`.** The installer is a small file, and should download quickly. Once it's downloaded, you can run it to install Miniconda on your computer.

## Running Miniconda

Miniconda isn't actually an app you can "run". It installs itself onto your computer, and sets its version of Python as the default for your computer. You would run Python from the command line in a terminal window (Terminal on a Mac; on Windows, you need to run the `miniconda prompt` app). But in practice, you won't be running Python from the command line; you'll be running it from within VS Code, which we'll install in the next section. VS Code will "see" the version of Python that Miniconda installed.

## Getting the Packages You Need

Once you have installed Miniconda, you can install the packages you need for this course. You can do this by creating a new environment, and then installing the packages into that environment. We have created a file that defines a `neural_data_science` environment, which you can download from [this link](https://github.com/neural-data-science/python_environment/blob/main/neural_data_science.yml), by clicking on the icon with a down arrow (it says `download raw file` if you mouse over it). Save this file to your computer. We'll actually use it to install the environment later, once we've installed VS Code.
