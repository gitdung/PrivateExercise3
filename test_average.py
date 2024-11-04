import pytest

def average(value, minimum, maximum):
    i = 0
    input_number = 0
    valid_number = 0
    sum_values = 0
    
    while i < len(value) and value[i] != -999 and input_number < 100:
        input_number += 1
        if minimum <= value[i] <= maximum:
            valid_number += 1
            sum_values += value[i]
        i += 1

    if valid_number > 0:
        return sum_values // valid_number 
    else:
        return -999

def test_average_tc1():
    assert average([-999], 1, 100) == -999

def test_average_tc2():
    assert average([10, -5, 150, -999], 1, 100) == 10

def test_average_tc3():
    assert average([50, 50, 50, 50, -999], 1, 100) == 50

def test_average_tc4():
    assert average([0, -999], 1, 100) == -999

def test_average_tc5():
    assert average([20, 30, 40, -999], 1, 50) == 30

def test_average_tc6():
    assert average([50, 150, -999], 1, 100) == 50

