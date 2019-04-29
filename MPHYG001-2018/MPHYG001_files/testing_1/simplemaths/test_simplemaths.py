#!/usr/bin/env python

from pytest import raises
from simplemaths.simplemaths import SimpleMaths
from numpy.testing import assert_allclose

class TestSimpleMaths():
    def test_initialization(self):
        with raises(ValueError):
            x = SimpleMaths(3.3)
            x = SimpleMaths('string')
            x = SimpleMaths([1,2])

    def test_square(self):
        number = [0, 1, 2, 5]
        classes = []
        for i in number:
            classes.append(SimpleMaths(i))
        result = [f.square() for f in classes]
        ob = SimpleMaths(1)
        result_fac = [ob._factorial(n) for n in number]
        
        assert_allclose(result, [0,1,4,25])
        assert_allclose(result_fac, [1,1,2,120])

    def test_square_neg(self):
        x = SimpleMaths(3)
        y = SimpleMaths(-2)
        with raises(AssertionError):
            assert_allclose([x.square(),y.square()], [10, -4])
    
    def test_power(self):
        obj = SimpleMaths(2)
        number = [0, 1, 2, 5]
        result = [obj.power(n) for n in number]
               
        assert_allclose(result, [1,2,4,32])

    def test_odd_or_even(self):
        number = [0, 1, 2, 3]
        classes = []
        for i in number:
            classes.append(SimpleMaths(i))
        result = [f.odd_or_even() for f in classes]

        assert result ==['Even','Odd','Even','Odd']
        
        ob = SimpleMaths(25)
        with raises(AssertionError):   
            assert ob.odd_or_even() == 'Even'
        
    def test_square_root(self):
        number = [0, 1, 4]
        classes = []
        for i in number:
            classes.append(SimpleMaths(i))
        result = [f.square_root() for f in classes]

        assert result ==[0,1,2]
        
        ob = SimpleMaths(2)
        with raises(AssertionError):   
            assert ob.square_root() ==2




    pass
