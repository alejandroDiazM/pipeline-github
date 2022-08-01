from main import print_test, even_numbers

def test_print():
    result = print_test()
    assert type(result) == str

def test_number_even():
    result = even_numbers()
    assert result[0] == 2