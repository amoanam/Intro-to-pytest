""""
This module contains basic unit tests for math operations.
Their purpose is to show you how to use pytest
"""
import pytest
# A most basic test function
@pytest.mark.math
def test_one_plus_one ():
    assert 1 +1 == 2
    
    
    
# A test function to show assertion introspection
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    
    
    
# A test function to verify an exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)
    
    
# Parameterized Test Cases
# for instance, we have to write test cases for multiplication test ideas

# two positive integers
# identity; multiply any number by 1
# zero; multiplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats


# example
"""""
def test_multiply_two_positive_ints():
    assert 2 * 3 ==6
    
def test_multiply_identity():
    assert 1 * 99 == 99
    
def test_multiply_zero():
    assert 5 * 0 == 0
    
"""

# DRY priciple; Don't repeat yourself

# So, Parametrized Test function

products = [
    (2, 3, 6),           #positive integers
    (1, 99, 99),         #identity
    (0, 99, 0),          #Zero
    (3, -4, -12),        #positive by negative
    (-5, -5, 25),        #negative by negative
    (2.5, 6.7, 16.75)   #floats
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b ==product