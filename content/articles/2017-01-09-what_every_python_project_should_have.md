Title: What every Python project should have
Date: 2017-01-09 20:21
Modified: 2017-01-10 11:54
Category: Python
Tags: project, python, tips
Authors: Vlad Calin

Over the past few years, the Python programming language gained a huge popularity boost
and its community grew faster than ever. With this growth, a lot of tools appeared that
help the community keep things organized and accessible. In this article I am going
to provide a short list of items every Python project should have in order to be
accessible and maintainable.

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

The project structure is crucial. With a well organized structure, it will e easier to organize things, locate certain
source files and encourages other people to contribute.

The root project directory should have a structure similar to

```
root/
		docs/
		tests/
		mymodule/
		scripts/
		requirements.txt
		setup.py
		README
		LICENSE
```

Of course, this is not the only way to organize your project, but this certainly is the most
used template.

## Tests

Unit testing is crucial for your project. It allows you to be confident in the stability
of your code. I recommend the ``unittest`` module for this job as it is built in and
is flexible enough to get the job done right. 

There are also other libraries that can be used for testing your project, such as
``test.py`` or ``nose``.

## Documentation

If you develop a project, I am sure that you don't write it just for yourself. Other people
must know how to use your project properly. And even if you write the project only for yourself
(although beats the purpose of open source), after a while of not developing it and when you
come back to it, you will surely not remember anything that is going on in your code (or API).

So, in order to achieve a reusable code base, you should:

- design a sane API that is easy to use and remember
- the same sane API should be flexible enough to allow easy configurations
- document the most relevant use-cases
- don't try to fit all cases. It should fit only the most usual 80% of cases.

In order to properly document your code, you should use a tool specialized for that job, such
as ``Sphinx`` or ``mkdocs``, so that you can generate nice-looking documentation with proper
reference links by writing in a popular markup language designed just for that (rst or markdown).

## Conclusion

After you familiarize yourself with the topics described above, you will surely be able to
produce nice structured projects and libraries that comply to the community standards. And 
don't forget to ALWAYS use PEP-8!