How To Document Your ... Snippets Code
--------------------------------------

The snips directory is for shared code that provides examples of how
to do something. The code may not be fully functional, especially if
it's showing how to do something in a bigger 'ecosystem', like doing
something in a GUI. 

IF YOUR CODE IS NON-FUNCTIONAL as written, you must document what it
is meant to show in the MODULE docstring.  


Documenting Your Snippet Module
-------------------------------

- Please add documentation at:
	- MODULE level - right at the top of the file
	- FUNCTION level - within each function
	  
- Try to add an Example for using your code in the MODULE docstring. This 
  will show up when users type help()

- If your code is funtional:
	- Embed a test using the :: if __name__ == "__main__": :: functionality.
	- Embed a simple data set on which to run the test.
	- Best case, embed a test and data AND a comparison to known results to 
      demonstrate that code is working correctly


