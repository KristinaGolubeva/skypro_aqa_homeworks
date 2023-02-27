
import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize('num1, num2, result', [(4,5,9), (-3,-7,-10)])
def test_sum_positive_nums(num1,num2,result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-3, -7)
    assert res == -10

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-7, 7)
    assert res == 0

res = calculator.sum(3.2, 6.5)
res = round(res,1)
assert res == 9.7

res = calculator.sum(10, 0)
assert res == 10

numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1,2,3,4,5,6,7,8,9,5]
res = calculator.avg(numbers)
assert res == 5

res = calculator.div(10, 5)
assert res == 2

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        res = calculator.div(10, 0)