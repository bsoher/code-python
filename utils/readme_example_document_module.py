# -*- coding: utf-8 -*-
"""This module provides tools to work with complex numbers

Note. Module docstrings are placed on the top line of the module

Classes:
    ComplexNumber

Functions:
    util_copy_complex(cplx1) -> ComplexNumber
    util_subtract(cplx1,cplx2) -> ComplexNumber

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_module_simple_docs.py

Note Again. The docstrings for Python Modules should list all the available 
classes, functions, objects and exceptions that are imported when the module 
is imported. They should also have a one-line summary for each item.

Also Note. The example below is a trivial one. There is a lot more info 
that could be put into each section. Please take the time to check out 
some of the resource links below.

Another Note. This example demonstrates documentation in the `Google Style'. 
For more information on this style see: 

.. https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
.. Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html#Comments

"""

module_level_variable1 = 12345
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

def util_copy_complex(cplx1): 
    """ 
    The utility function to copy a ComplexNumber. 
  
    Extended description of function could be added here. 
  
    Parameters:
        cplx1 (ComplexNumber): The object to be copied.
  
    Returns:
        ComplexNumber: A complex number which contains the copy.
  
    """
    cp1 = ComplexNumber(cplx1.real, cplx1.imag)
    
    return cp1 
    

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


"""
When I type help() for this module in a Python prompt, I get:

>>> import example_module_simple_docs
>>> help(example_module_simple_docs)

Help on module example_module_simple_docs:

NAME
    example_module_simple_docs - This module provides tools to work with complex numbers

FILE
    d:\users\bsoher\code\repository_svn\_mrshub\example_module_simple_docs.py

DESCRIPTION
    Note. Module docstrings are placed on the top line of the module

    Classes:
        ComplexNumber

    Functions:
        util_copy_complex(cplx1) -> ComplexNumber
        util_subtract(cplx1,cplx2) -> ComplexNumber

    Example:
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections support any reStructuredText formatting, including
        literal blocks::

            $ python example_module_simple_docs.py

    Note Again. The docstrings for Python Modules should list all the available
    classes, functions, objects and exceptions that are imported when the module
    is imported. They should also have a one-line summary for each item.

    Also Note. The example below is a trivial one. There is a lot more info
    that could be put into each section. Please take the time to check out
    some of the resource links below.

    Another Note. This example demonstrates documentation in the `Google Style'.
    For more information on this style see:

    .. https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
    .. Google Python Style Guide:
       http://google.github.io/styleguide/pyguide.html#Comments

CLASSES
    ComplexNumber

    class ComplexNumber
     |  This is a class for operations on complex numbers.
     |
     |  Attributes:
     |      real (float): The real part of complex number.
     |      imag (float): The imaginary part of complex number.
     |
     |  Methods defined here:
     |
     |  __init__(self, real, imag)
     |      The constructor for ComplexNumber class.
     |
     |      Parameters:
     |          real (float): The real part of complex number.
     |          imag (float): The imaginary part of complex number.
     |
     |  add(self, num)
     |      The function to add two Complex Numbers.
     |
     |      Parameters:
     |          num (ComplexNumber): The complex number to be added.
     |
     |      Returns:
     |          ComplexNumber: A complex number which contains the sum.

FUNCTIONS
    util_copy_complex(cplx1)
        The utility function to copy a ComplexNumber.

        Extended description of function could be added here.

        Parameters:
            cplx1 (ComplexNumber): The object to be copied.

        Returns:
            ComplexNumber: A complex number which contains the copy.

    util_subtract(cplx1, cplx2)
        The utility function to subtract two Complex Numbers.

        Parameters:
            cplx1 (ComplexNumber): The first complex number object.
            cplx2 (ComplexNumber): The second complex number object.

        Returns:
            ComplexNumber: A complex number which contains the difference.

DATA
    module_level_variable1 = 12345


>>>

"""