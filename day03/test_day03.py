from is_prime import is_prime
from factorial import factorial
from fibonacci import fibonacci


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(25) == False
    assert is_prime(1) == False
    assert is_prime(0) == False


def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(0) == 1


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(7) == 13