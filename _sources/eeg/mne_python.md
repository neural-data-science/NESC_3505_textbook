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
