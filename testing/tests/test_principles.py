import sys
sys.path.append('../src')

from math_demo import add

def test_addition_basic():
    assert add(2,2) == 4
    print("Test BASIC ADDITION PASSED")

if __name__ == '__main__':
    test_addition_basic()