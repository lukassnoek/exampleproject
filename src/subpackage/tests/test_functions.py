"""
IMPORTANT: never run the tests from the file directly, as they
won't work because of the relative imports; just run them
from the command line by: pytest [options]
"""

import pytest
import numpy as np
import os
from ..functions import demean, Demeaner

arr = np.random.randn(100, 100)


def test_demean():

    arr_out = demean(arr, to_file=True)

    # Just a bunch of assert statements is enough!
    assert(arr_out.shape == arr.shape)

    written_file = os.path.join(os.getcwd(), 'arr_out.npy')
    assert(os.path.isfile(written_file))
    os.remove(written_file)


# Pytest's parametrize decorators are really neat;
# they can test you functions with a bunch of options
# without explicitly defining them.
@pytest.mark.parametrize('standardize', [True, False])
def test_Demeaner(standardize):

    dmn = Demeaner(arr=arr, to_file=False)
    arr_out = dmn.demean(standardize=standardize)

    np.testing.assert_almost_equal(arr_out.mean(axis=0),
                                   np.zeros(arr_out.shape[1]),
                                   decimal=10)

    if standardize:
        # Here, I'm using assert functions from numpy
        np.testing.assert_almost_equal(arr_out.std(axis=0),
                                       np.ones(arr_out.shape[1]),
                                       decimal=10)
