How To Document Your ... Libraries Code
---------------------------------------

The libs directory is for shared code libraries. These are usually going to
be one or more modules that are associated into a subdirectory that contains
an __init__.py file that allow them to be imported into a program as a 
package, rather than individually as modules. 

We leave it to you to ensure that all the modules qualify as a 'library'.
However, we'd ask for a higher level of documentation if you are going to 
put your code here. All modules should be tested to work as described. Ideally
they will contain unit-test level data/test() functionality embedded within
each module.

Please see: code-python/howto_document_code_extensive.txt  for a selection
of comments on documentation that we found inspiring.


Documenting Your Library
------------------------

- Please add documentation at:
	- PACKAGE level  - in the __init__.py file
	- MODULE level   - right at the top of each module file
	- FUNCTION level - within each function
	- You can do a README file if you want, but that does not show up 
	  auto-magically using the help() call at the python command line.
	  
- Add an Example for using your code in each MODULE docstring. This will show 
  up when users type help()

- Embed a test using the :: if __name__ == "__main__": :: functionality.

- Embed a simple data set on which to run the test, otherwise document where 
  to get the test data.

- Best case, embed a test and data AND a comparison to known results to 
  demonstrate that code is working correctly


Some helpful (?) Guidelines
============================

Docstrings for Python PACKAGES
------------------------------
The docstrings for a Python package is written in the package's __init__.py 
file.

It should contain all the available modules and sub-packages exported by the 
package.

Docstrings for Python MODULES
------------------------------
The docstrings for Python Modules are located at the top of the module file
before any other code. 

The docstring should list all the available classes, functions, objects and 
exceptions that are imported when the module is imported. It should also have 
a one-line summary for each item.

Docstrings for Python FUNCTION
-------------------------------
The docstring for a function or method should summarize its behavior and 
document its arguments and return values.

It should also list all the exceptions that can be raised and other optional 
arguments.

Docstrings for Python CLASSES
-----------------------------
The docstrings for classes should summarize its behavior and list the public 
methods and instance variables.

The subclasses, constructors, and methods should each have their own docstrings.

Docstring Formats/Styles
------------------------
We can write docstring in many formats like the Google format, the NumPy 
documentation format, or reStructured text (reST) format.

We recommend using the Google format if possible (it was that or NumPy and 
flipped a coin). 

Here are links to some popular Styles - 

Google - https://google.github.io/styleguide/pyguide.html
NumPy  - https://numpydoc.readthedocs.io/en/latest/

