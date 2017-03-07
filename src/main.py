"""
This could be your main analysis, importing functions
from `subpackage/functions.py`

You can document some more stuff here.
"""

import numpy as np
from subpackage.functions import demean

arr = np.random.randn(100, 100)
arr_out = demean(arr, to_file=False)


