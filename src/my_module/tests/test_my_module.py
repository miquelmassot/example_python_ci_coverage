from my_module import my_module

from my_module.tools import really_important_function


def test_my_function():
    ret = really_important_function()
    assert ret


def test_main():
    ret = my_module.main()
    assert ret is None
