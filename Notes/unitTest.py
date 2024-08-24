# you can write your own program to test your code
# test for calculator program that we wrote previously
# from calculator import square


# def main():
#    test_square()


# def test_square():
#   if square(2) != 4:
#       print("2 squared was not 4")
#   if square(3) != 9:
#        print("3 squared was not 9")
# another way to write same code:
# 'assert' is a keyword that is used make something true
# def test_square():
#    try:
#        assert square(2) == 4
#        assert square(3) == 9    # if not true, it will give 'AssertionError'
#    except AssertionError:
#        print("AssertionError")


# 'pytest' is a third party tool of python that automates the test code that you write for your program
# there are some other tools that comes with python itself
# unit Tests is the test for units/functions that you have written



# if __name__ == '__main__':
#    main()



# another way using pytest

from calculator import square
import pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("Cat")


# making different functions to handle error:
# pytest handles the try, except and printing of these errors, so you don't have to do it urself
# write pytest fileName on terminal
# return something by function to test it using assert keyword.
# we can also carry out test for the entire folder using pytest.

# we can also test for exceptions raised in files using pytest library  - pytest.raises(error name)
 

