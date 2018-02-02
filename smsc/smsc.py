import re
import requests

from .exceptions import AreaCodeSMSCError, LocalNumberSMSCError, PhoneNumberLongSMSCError


class SMSC(object):
    def __init__(self, alias, apikey, apiversion='0.3', lineid=None):
        self.alias = alias
        self.apikey = apikey
        self.lineid = lineid
        self.apiversion = apiversion

    def _url(self, cmd, **kwargs):
        url = 'https://www.smsc.com.ar'
        basic = '/api/{}/?alias={}&apikey={}&cmd={}'.format(self.apiversion, self.alias, self.apikey, cmd)
        extra = ''
        for k, v in kwargs.items():
            extra += '&{}={}'.format(k, v)
        return url+basic+extra

    def _validate_phone_number(self, area_code, local_number):
        if re.match(r'^\d{2,4}$', area_code):
            raise AreaCodeSMSCError(area_code, 'area_code: This param is invalid')
        if re.match(r'^\d{6,8}$', local_number):
            raise LocalNumberSMSCError(local_number, 'local_number: This param is invalid')
        if re.match(r'^\d{10}$', area_code+local_number):
            raise PhoneNumberLongSMSCError(area_code+local_number, 'The number should be 10 digits')

    def send(self, area_code, local_number, msj, time=None):
        self._validate_phone_number(area_code, local_number)
        kwargs = {
            'num': '{}-{}'.format(area_code, local_number),
            'msj': msj
        }
        if time:
            kwargs['time'] = time
        r = requests.get(self._url(cmd='enviar', **kwargs))
        return r.json()

    def sent(self, last_id=0):
        kwargs = {
            'ultimoid': last_id
        }
        r = requests.get(self._url(cmd='enviados', **kwargs))
        return r.json()

    def received(self, last_id=0):
        kwargs = {
            'ultimoid': last_id
        }
        r = requests.get(self._url(cmd='recibidos', **kwargs))
        return r.json()

    def status(self):
        r = requests.get(self._url(cmd='estado'))
        return r.json()

    def balance(self):
        r = requests.get(self._url(cmd='saldo'))
        return r.json()

    def cancel_queue(self):
        kwargs = {}
        if self.lineid:
            kwargs['lineid'] = self.lineid
        r = requests.get(self._url(cmd='cancelqueue', **kwargs))
        return r.json()
