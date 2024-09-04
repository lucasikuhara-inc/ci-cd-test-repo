from double import double
import numpy as np


def test_double():
    x = double(np.array([1, 2]))
    assert x.sum() == 6
