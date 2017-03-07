"""
This is a description of the `functions.py` module. This is also parsed by
the Sphinx apidoc tool, and it's responsive to all ReST syntax/gimmicks.

For example, you make make notes:

.. note:: This is a note!

And warnings:

.. warning:: This is a warning.

Now, you can simply add docstrings to your functions/classes, and they will
turn up in your documentation when processed with sphinx-apidoc.

.. note:: You should use Numpy-docstrings instead of the regular
  Python docstrings. When using Numpy-docstrings, make sure to
  use the Sphinx-extension "napoleon" (`sphinx_ext_napoleon`),
  which is the engine to parse Numpy-docstrings!

"""

import numpy as np
import os
import os.path as op


def demean(arr, to_file=True):
    """ Preprocesses some file (see [1]_)

    Parameters
    ----------
    arr : array-like
        Numpy array with data to standardize.
    to_file : bool
        Whether to write the results to a file.

    Returns
    -------
    out_arr : array-like
        Demeaned numpy array.

    Note
    ----
    This is another heading!

    References
    ----------
    .. [1] Snoek. (2017). A sphinx/RTD/pytest/travis tutorial.

    """

    arr_new = arr - arr.mean(axis=0)
    if to_file:
        np.save(op.join(os.getcwd(), 'arr_out'), arr_new)

    return arr_new


class Demeaner(object):
    """ Docstrins can be put right below the class definition, but
    also within the __init__ method if desired (in this case,
    set `napoleon_include_init_with_doc` to `True` in conf.py.

    Also, set `napoleon_use_ivar` to `True` in conf.py, which
    enables the documentation of attributes.

    Parameters
    ----------
    arr : array-like
        Numpy array with data to standardize.
    to_file : bool
        Whether to write the results to a file.

    Attributes
    ----------
    arr_shape : tuple
        Shape of the array.

    """


    def __init__(self, arr, to_file):

        self.arr = arr
        self.to_file = to_file
        self.arr_shape = arr.shape

    def demean(self, standardize=True):
        """ Demeans array and optionally standardizes it.

        Parameters
        ----------
        standardize : bool
            Whether to standardize (divide by std).

        Returns
        -------
        arr_out : array-like
            Demeand array.

        """

        arr_out = demean(self.arr, to_file=False)

        if standardize:
            arr_out = arr_out / arr_out.std(axis=0)

        return arr_out