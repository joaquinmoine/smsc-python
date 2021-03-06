import re

from smsc.exceptions import AreaCodeSMSCError, LocalNumberSMSCError, PhoneNumberLongSMSCError, PriorityOutOfRangeError


def validate_phone_number(area_code, local_number):
    if not re.match(r'^\d{2,4}$', area_code):
        raise AreaCodeSMSCError(area_code, 'area_code: This param is invalid')
    if not re.match(r'^\d{8,13}$', local_number):
        raise LocalNumberSMSCError(local_number, 'local_number: This param is invalid')
    if not re.match(r'^\d{10,13}$', area_code + local_number):
        raise PhoneNumberLongSMSCError(area_code + local_number, 'The number should be 10 digits')


def validate_phone_numbers(phone_numbers):
    for phone_number in phone_numbers:
        validate_phone_number(*phone_number)


def validate_area_code(area_code):
    """
    :param area_code: <str>
    :return: True if is valid, False otherwise
    """
    return bool(re.match(r'^\d{2,4}$', area_code))


def validate_local_number(local_number):
    """
    :param local_number: <str>
    :return: True if is valid, False otherwise
    """
    return bool(re.match(r'^\d{6,8}$', local_number))


def validate_length_phone_number(phone_number):
    """
    :param phone_number: <str>
    :return: True if is valid, False otherwise
    """
    return bool(re.match(r'^\d{10}$', phone_number))


def validate_priority(priority):
    """
    :param priority: <int>
    Raise an exeption if the priority is out of range
    :return: None
    """
    if not 1<=priority<=7:
        raise PriorityOutOfRangeError(priority, 'The priority must be between 1 and 7')
