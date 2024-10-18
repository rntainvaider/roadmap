import pytest
from task_two import Number

class TestNumber:
    def setup_method(self):
        self.converter_positive = Number(10)
        self.converter_negative = Number(-10)

    def test_conversion_to_octal(self):
        assert self.converter_positive.conversion_to_octal() == '0o12'
        assert self.converter_negative.conversion_to_octal() == '-0o12'

    def test_conversion_to_hexadecimal(self):
        assert self.converter_positive.conversion_to_hexadecimal() == '0xa'
        assert self.converter_negative.conversion_to_hexadecimal() == '-0xa'

    def test_conversion_to_binary(self):
        assert self.converter_positive.conversion_to_binary() == '0b1010'
        assert self.converter_negative.conversion_to_binary() == '-0b1010'