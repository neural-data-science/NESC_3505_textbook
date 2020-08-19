# Organization of MNE-Python

One useful thing to know at the outset is that there are a lot of tools (functions, classes, methods, etc.) included with MNE-Python, all of which are documented in the [API](https://mne.tools/stable/python_reference.html). These are organized into *submodules* according to their functions. For example, there are many different functions for importing data in a wide range of formats (since most neuroimaging equipment manufacturers use unique, proprietary data formats), as well as for saving data after it's been processed by MNE-Python. These are all organized within the `mne.io` submodule ("io" standing for "input-output"). While this organization is useful, it does mean that when using an MNE function, you might need to type a relatively long bit of text. You are already familiar with specifying the package along with the name of the function in that package you want to run. For example, to create a NumPy array, you would first import the package:

    import numpy as np

and then run the command:

    np.array()

In other words, you can't just type `array` because Python needs to know what package that function is part of. With MNE submodules, you often will need to use a chain of `module.submodule.function` specifications, such as

    import mne
    mne.io.read_raw_brainvision()

to import a data file saved in the BrainVision format.
