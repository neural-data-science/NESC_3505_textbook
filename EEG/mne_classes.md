# MNE classes

Working with MNE, you will be working with Python *classes*. We've already worked extensively with classes, including NumPy's `Array` class, and pandas' `DataFrame`. However, it's worth reviewing and expanding on what you already know. The [Python documentation](https://docs.python.org/3/tutorial/classes.html) tells us that "Classes provide a means of bundling data and functionality together." A class is a type of **object**, which can in turn have **instances**. Putting this concretely in the MNE context, one important set of MNE classes are for storing data of different kinds. These include `mne.io.Raw`, `mne.Epochs`, and `mne.Evoked` (note the use of capital letters here, which indicates that these are classes). `mne.io.Raw` is a class specifically for raw data (EEG or other types of data as imported from a data file). When we import a data file, e.g., using the `mne.io.read_raw_brainvision()` function mentioned above, we assign it to a variable name, e.g.:

    raw = mne.io.read_raw_brainvision('my_EEG_file.vhdr')

`raw` is thus an instance of the `mne.io.Raw` class (again pay attention to the fact that the *class* uses upper-case naming but the *instance* uses lower-case, which is a Python standard).

While this may sound a bit arcane at first, it's important to understand because classes are special, and understanding the properties of classes helps you understand how to work with data in MNE. Classes specify **attributes** that an instance of that class can have. Attributes are "states" of the instance — which in the case of an MNE data class are usually properties of that data. So one critical attribute of the `mne.io.Raw` class is `_data`, which contains the actual data values (e.g., microvolt values at each time point, for each electrode, in an EEG data set). But others include `info`, which includes meta-data about the data set, such as the number of electrodes, labels of the electrodes, and the sampling rate (how many times per second EEG data was recorded). The attributes of a class instance are accessed via dot-notation, so to see the data for the raw file we imported in the example above, we'd run:

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
