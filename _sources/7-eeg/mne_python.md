```{figure} images/mne_logo.png
---
align: left
width: 150px
```
# MNE-Python

[MNE-Python](https://mne.tools/) is an open-source Python package for working with EEG and MEG data. It was originally developed as a Python *port* (translation from one programming language to another) of a software package called MNE, that was written in the C language by MEG researcher Matti Hämäläinen. The letters "MNE" originally stood for *minimum norm estimation*, which is an algorithm for localizing the sources of MEG and EEG data. The original MNE software grew from an implementation of that algorithm to a much more full-fledged package capable of performing a wider range of processing and visualization tasks on MEG/EEG data — so now the name "MNE" is more of a brand, than a descriptor of the capabilities of the software. Although minimum norm estimation can still be performed using MNE-Python, it does far more even than the MNE-C package did.

MNE-Python moved the development of the software to an open source model, using a language (Python) that was more accessible and familiar to the scientific community, and hosing the project on [GitHub](https://github.com/mne-tools/mne-python). This has greatly facilitated the development of the software, as it has benefitted from the contributions of hundreds of people around the world.

As you might expect from your experience so far, MNE-Python is designed to used by writing Python code that employs the MNE package. Although it has some interactive tools, such as interactive plots, by and large MNE-Python is used by writing scripts in .py text files, or Jupyter notebooks. It is very tightly integrated with the scientific Python stack, notably packages you are already familiar with such as [NumPy](https://numpy.org), [pandas](https://numpy.org), [matplotlib](https://matplotlib.org/) (which is used to generate all MNE-Python's 2D plots), and [scikit-learn](https://scikit-learn.org/stable/).

MNE is very well-documented. [The MNE website](https://mne.tools/stable/index.html) has a large number of tutorials and examples of how to perform specific operations, as well as a complete [API](https://mne.tools/stable/python_reference.html). You will find this API immensely useful in understanding this chapter and working with MNE.

# Organization of the MNE package

One useful thing to know at the outset is that there are a lot of tools (functions, classes, methods, etc.) included with MNE-Python, all of which are documented in the [API](https://mne.tools/stable/python_reference.html). These are organized into *submodules* according to their functions. MNE is not the only package that does this; many Python packages do — this is just the first time we've encountered it in this course. 

For example, there are many different functions for importing data in a wide range of formats (since most neuroimaging equipment manufacturers use unique, proprietary data formats), as well as for saving data after it's been processed by MNE-Python. These are all organized within the `mne.io` submodule ("io" standing for "input-output"). While this organization is useful, it does mean that when using an MNE function, you might need to type a relatively long bit of text. You are already familiar with specifying the package along with the name of the function in that package you want to run. For example, to create a NumPy array, you would first import the package:

    import numpy as np

and then run the command:

    np.array()

In other words, you can't just type `array` because Python needs to know what package that function is part of. With MNE submodules, you often will need to use a chain of `module.submodule.function` specifications, such as

    import mne
    mne.io.read_raw_brainvision('my_EEG_file.vhdr')

In this example, we want to run a function called `read_raw_brainvision()` (which reads raw EEG data from the BrainVision file format). However, that function is part of the `mne.io` submodule, which is part of the `mne` package. So we need to specify `mne.io.read_raw_brainvision()`. 

Sometimes, if you only want to use one function in a submodule, you can import it directly. For example, if you only want to use the `read_raw_brainvision()` function, you could import it directly and then run it without specifying the submodule:

    from mne.io import read_raw_brainvision
    read_raw_brainvision('my_EEG_file.vhdr')

# MNE classes

Working with MNE, you will be working with Python *classes*. We've already worked extensively with classes, including NumPy's `Array` class, and pandas' `DataFrame`. However, it's worth reviewing and expanding on what you already know. The [Python documentation](https://docs.python.org/3/tutorial/classes.html) tells us that "Classes provide a means of bundling data and functionality together." A class is a type of **object**, which can in turn have **instances**. Putting this concretely in the MNE context, one important set of MNE classes are for storing data of different kinds. These include `mne.io.Raw`, `mne.Epochs`, and `mne.Evoked` (note the use of capital letters here, which indicates that these are classes). `mne.io.Raw` is a class specifically for raw data (EEG or other types of data as imported from a data file). When we import a data file, e.g., using the `mne.io.read_raw_brainvision()` function mentioned above, we assign it to a variable name, e.g.:

    raw = mne.io.read_raw_brainvision('my_raw_EEG_file.vhdr')

`raw` is thus an instance of the `mne.io.Raw` class (again pay attention to the fact that the *class* uses upper-case naming but the *instance* uses lower-case, which is a Python standard).

While this may sound a bit arcane at first, it's important to understand because classes are special, and understanding the properties of classes helps you understand how to work with data in MNE. Classes specify **attributes** that an instance of that class can have. Attributes are "states" of the instance — which in the case of an MNE data class are usually properties of that data. So one critical attribute of the `mne.io.Raw` class is `_data`, which contains the actual data values (e.g., microvolt values at each time point, for each electrode, in an EEG data set). But others include `info`, which includes meta-data about the data set, such as the number of electrodes, labels of the electrodes, their positions on the scalp, and the sampling rate (how many times per second EEG data was recorded). 

The attributes of a class instance are accessed via dot-notation, so to see the data for the raw file we imported in the example above, we'd run:

    raw._data

Whereas to see the meta-data we'd run:

    raw.info

Note that because these are *attributes* of the class, we don't put parentheses after them.

Classes can also specify **methods**, and indeed MNE classes do this. For example, the `mne.io.Raw` class specifies over three dozen different methods, allowing the user to do things such as plot the raw data, `mne.io.Raw.plot()`, plot the locations of the electrodes on the head, `mne.io.Raw.plot_sensors()`, apply filters to it, `mne.io.Raw.filter()`, copy it, `mne.io.Raw.copy()`, or even convert it to a pandas DataFrame, `mne.io.Raw.to_data_frame()`. Note that, as these are methods, parentheses are required after the method name. Virtually all MNE methods have a range of mandatory and/or optional arguments that affect their output.

MNE also has **functions** that perform different tasks. As in the rest of Python, functions are run by specifying the function name, with arguments in parentheses. The main difference between functions and methods is that methods are applied by specifying the name of the instance that you want to apply them to, followed by a period then the method name:

    raw.plot()

whereas functions are "free-standing" and, if they take a data input, it's supplied as an argument inside the parentheses:

    plot_raw(raw)

The two examples just provided would both achieve the same goal; as is so often the case with Python, there are just many different ways of doing the same thing.

MNE has an extensive and detailed [API](https://mne.tools/stable/python_reference.html) describing all of its classes, attributes, methods, and functions.