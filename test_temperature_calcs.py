from temperature_calcs import convert


def test_k_to_c():
    assert convert("kelvin", "celcius", 10) == -263


def test_c_to_k():
    assert convert("celcius", "kelvin", 10) == 283


def test_f_to_c():
    assert convert("farenheit", "celcius", 41) == 5


def test_c_to_f():
    assert convert("celcius", "farenheit", 5) == 41


def test_k_to_f():
    assert convert("kelvin", "farenheit", 278) == 41


def test_f_to_k():
    assert convert("farenheit", "kelvin", 41) == 278
