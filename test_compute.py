from compute import divide
from compute import multiply

import numpy as np
import pytest

@pytest.mark.parametrize(
    'a, b, x', [(1,2,0.5),(4,2,2)]
)
def test_divide(a, b, x):
    res = divide(a,b)
    print(x)
    assert res == pytest.approx(x) #better, because can occur some imprecisions due to type


def test_divide_zero():
    x = divide(2, 0)
    assert np.isinf(x)

def test_multiply():
    assert multiply(2,2)==4
    
    