How To Document Your ... Utilities Code
---------------------------------------

The utils directory is for shared code that provides working function that are
not generally 'science'.  Yeah, it's a bit outre to define something by what
it is *not* but, here we are.  A utility module should be fully functioning, 
but have more to do with coding, file I/O, data formats, plotting, etc. than 
with sciency algorithmic stuff.


Documenting Your Modules
------------------------

- Please add documentation at:
    - MODULE level - right at the top of the file
    - FUNCTION level - within each function
    - You can do a README file if you want, but that does not show up 
      auto-magically using the help() call at the python command line.
      
- Try to add an Example for using your code in the MODULE docstring. This 
  will show up when users type help()

- Embed a test using the :: if __name__ == "__main__": :: functionality.

- Embed a simple data set on which to run the test, otherwise document where 
  to get the test data.

- Best case, embed a test and data AND a comparison to known results to 
  demonstrate that code is working correctly
  
- IF you are contributing a package here (ie. it has an __init__.py file)
  then please add a docstring at the top of __init__.py to give an overview
  of what this package does, and what each file contains. Consider if this
  contribution should be in the code-python/libs directory.


Example - Trival, but a start.  
-------
Note. The example below is a trivial one. There is a lot more info that could 
be put into each section. Please take the time to check out some of the 
resources in the code-python/_how_to_document directory.


# -*- coding: utf-8 -*-
"""This module provides tools to work with complex numbers

Classes:
    ComplexNumber

Functions:
    util_subtract(cplx1,cplx2) -> ComplexNumber

"""

module_level_variable1 = 12345
"""int: Module level variable documented inline."""


def util_copy_complex(cplx1): 
    """ 
    The utility function to copy a ComplexNumber. 
  
    Parameters:
        cplx1 (ComplexNumber): The object to be copied.
  
    Returns:
        ComplexNumber: A complex number which contains the copy.
  
    """
    return ComplexNumber(cplx1.real, cplx1.imag) 
    

def util_subtract(cplx1, cplx2):
    """
    The utility function to subtract two Complex Numbers.

    Parameters:
        cplx1 (ComplexNumber): The first complex number object.
        cplx2 (ComplexNumber): The second complex number object.

    Returns:
        ComplexNumber: A complex number which contains the difference.

    """
    re = cplx1.real - cplx2.real 
    im = cplx1.imag - cplx2.imag 

    return ComplexNumber(re, im)     


class ComplexNumber: 
    """ 
    This is a class for operations on complex numbers. 
      
    Attributes: 
        real (float): The real part of complex number. 
        imag (float): The imaginary part of complex number. 
    
    """
    def __init__(self, real, imag): 
        """ 
        The constructor for ComplexNumber class. 
  
        Parameters:
            real (float): The real part of complex number. 
            imag (float): The imaginary part of complex number. 
        
        """
        self.real = real
        self.imag = imag
        
  
    def add(self, num): 
        """ 
        The function to add two Complex Numbers. 
  
        Parameters:
            num (ComplexNumber): The complex number to be added. 
          
        Returns:
            ComplexNumber: A complex number which contains the sum. 
        
        """
        re = self.real + num.real 
        im = self.imag + num.imag 
  
        return ComplexNumber(re, im) 
