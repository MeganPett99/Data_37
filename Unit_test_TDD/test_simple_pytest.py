from simple_calc import simple_calc


def test_add():
    calc = simple_calc()
    actual = calc.add(4, 5)
    expected = 9
    assert actual == expected

