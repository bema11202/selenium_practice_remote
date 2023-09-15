import pytest


def test_my_first():
    print("I'm inside my first test!")

    my_validation = True
    assert my_validation, 'My validation failed due to True!'


def test_my_second():
    print("I'm inside my second test!")


def test_my_third():
    print("This must be my third test if it runs properly")


def test_my_fourth():
    print("This must be my fourth test if it runs properly")


def test_my_fifth():
    print("This must be my fifth test if it runs properly")