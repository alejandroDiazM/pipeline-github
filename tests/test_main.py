from ..main import even_numbers, print_test

def test_print():
    result = print_test()
    assert type(result) == str

def test_number_even():
    result = even_numbers()
    assert result[0] == 2