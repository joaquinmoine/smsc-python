import re

from smsc.exceptions import AreaCodeSMSCError, LocalNumberSMSCError, PhoneNumberLongSMSCError


def validate_phone_number(area_code, local_number):
    if re.match(r'^\d{2,4}$', area_code):
        raise AreaCodeSMSCError(area_code, 'area_code: This param is invalid')
    if re.match(r'^\d{6,8}$', local_number):
        raise LocalNumberSMSCError(local_number, 'local_number: This param is invalid')
    if re.match(r'^\d{10}$', area_code + local_number):
        raise PhoneNumberLongSMSCError(area_code + local_number, 'The number should be 10 digits')
