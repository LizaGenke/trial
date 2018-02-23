from compute import divide
from compute import multiply

import pytest

@pytest.mark.parametrize(
    'a, b, x', [(1,2,0.5),(4,2,2)]
)
def test_divide(a, b, x):
    res = divide(a,b)
    print(x)
    assert res == pytest.approx(x) #better, because can occur some imprecisions due to type

def test_multiply():
    assert multiply(2,2)==4
    
    