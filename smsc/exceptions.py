class BaseSMSCError(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class AreaCodeSMSCError(BaseSMSCError):
    pass


class LocalNumberSMSCError(BaseSMSCError):
    pass


class PhoneNumberLongSMSCError(BaseSMSCError):
    pass

class PriorityOutOfRangeError(BaseSMSCError):
    pass
