import unittest
from smsc.utils import sms_is_limited, sms_length, sms_rest, sms_parse


class TestUtils(unittest.TestCase):
    msg_is_limited = 'abcdefghijklmnopqrstuvwxyzáéíóúñ'
    msg_is_not_limited = 'abcdefghijklmnopqrstuvwxyz'

    def test_is_limited(self):
        self.assertTrue(sms_is_limited(msg=self.msg_is_limited))
        self.assertFalse(sms_is_limited(msg=self.msg_is_not_limited))

    def test_sms_length(self):
        length, capacity = sms_length(msg=self.msg_is_limited)
        self.assertEqual(length, len(self.msg_is_limited))
        self.assertEqual(capacity, 70)
        length, capacity = sms_length(msg=self.msg_is_not_limited)
        self.assertEqual(length, len(self.msg_is_not_limited))
        self.assertEqual(capacity, 160)

    def test_sms_rest(self):
        rest = sms_rest(msg=self.msg_is_limited)
        self.assertEqual(rest, 70-len(self.msg_is_limited))
        rest = sms_rest(msg=self.msg_is_not_limited)
        self.assertEqual(rest, 160-len(self.msg_is_not_limited))

    def test_sms_parse(self):
        parsed = sms_parse(msg=self.msg_is_limited*3)
        self.assertEqual(len(parsed), 2)
        parsed = sms_parse(msg=self.msg_is_not_limited * 3)
        self.assertEqual(len(parsed), 1)
