Title: Waht every Python project should have
Date: 2017-01-09 20:21
Modified: 2017-01-09 22:37
Category: Python
Tags: project, python, tips
Authors: Vlad Calin

Well, over the years, the Python community grew a lot and a lot of tools that serve 
different purposes appeared in sight. For a Python newbie, it is overwhelming because 
there are so many tools that he doesn't even know where to begin.

But generally, there are some elements that every Python project should have in 
order to facilitate some basic operations such as installation, maintainance and testing.


## requirements.txt

Firstly, the ``requirements.txt`` file is crucial for the sanity of those who want to install your project.
It is basically a text file which contains the dependencies to be installed via ``pip``, one per line. 

It is that simple. And that powerful. 

You can also have multiple ``requirements.txt`` files that serve different purposes. For example,
you can have a ``requirements.txt`` that have general dependencies listed that your project need to run, a ``requirements_dev.txt`` where
you have listed some dependencies that enable some debugging mechanisms and a ``requirements_docs.txt`` that has listed some
requirements that are used when generating the documentation (such as ``Sphinx`` and the desired ``theme``).


## setup.py

A ``setup.py`` file is crucial for your project if you want to be installable via ``pip``. It is easy to write, very configurable and takes care of a lot of things such as importing, project metadata, updating the sources, installing the dependencies, and much more.

You can check the [setuptools](https://setuptools.readthedocs.io/en/latest/) documentation for more information on this. 

## A proper structure

## Tests

## Documentation