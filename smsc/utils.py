"""
This module provide utilities for sms
"""
import math


def sms_is_limited(msg):
    """
    :param msg: <str>
    :return: <bool> True if msj contain special characters else False
    """
    for i in msg:
        if ord(i) > 127:
            return True
    return False


def sms_length(msg):
    """
    :param msg: <str>
    :return: <int>, <int> len of message and capacity of sms
    """
    if sms_is_limited(msg):
        return len(msg), 70
    return len(msg), 160


def sms_rest(msg):
    """
    :param msg: <str>
    :return: <int> return the difference between length of message and capacity of sms
    """
    if sms_is_limited(msg):
        return 70 - len(msg)
    return 160 - len(msg)


def sms_parse(msg, offset=0):
    """
    :param msg: <str>
    :param offset: <int> (optional) offset for a previous message
    :return: [<str>, ...] sms to send and substring with te message
    """
    if sms_is_limited(msg):
        array_len = math.ceil(len(msg)/(70-offset))
        subarray_len = 70-offset
    else:
        array_len = math.ceil(len(msg)/(160-offset))
        subarray_len = 160-offset
    result = [msg[i*subarray_len:i*subarray_len+subarray_len] for i in range(array_len)]
    return result
