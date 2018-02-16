import unittest
from smsc.validations import validate_area_code, validate_local_number, validate_length_phone_number


class TestValidations(unittest.TestCase):

    def test_validate_code_area(self):
        valid_code = '123'
        invalid_code = '12345'
        self.assertTrue(validate_area_code(valid_code))
        self.assertFalse(validate_area_code(invalid_code))

    def test_validate_local_number(self):
        valid_number = '123123'
        invalid_number = '123123123'
        self.assertTrue(validate_local_number(valid_number))
        self.assertFalse(validate_local_number(invalid_number))

    def test_validate_length_phone_number(self):
        valid_number = '1234567890'
        invalid_number = '123456789'
        self.assertTrue(validate_length_phone_number(valid_number))
        self.assertFalse(validate_length_phone_number(invalid_number))
