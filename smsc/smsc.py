"""
SMSC API: Main module
"""
import requests
import urllib

from smsc.validations import validate_phone_number, validate_priority, validate_phone_numbers


class SMSC(object):
    def __init__(self, alias, apikey, apiversion='0.3', lineid=None):
        """
        :param alias: Alias of SMSC
        :param apikey: ApiKey of SMSC
        :param apiversion: API version that you use (optional)
        :param lineid: Private line ID (optional)
        """
        self.alias = alias
        self.apikey = apikey
        self.lineid = lineid
        self.apiversion = apiversion

    def _url(self, cmd, **kwargs):
        url = 'https://www.smsc.com.ar/api/{}/?'.format(self.apiversion)
        params = {
            'alias': self.alias,
            'apikey': self.apikey,
            'cmd': cmd
        }
        params.update(dict(kwargs.items()))
        return url+urllib.parse.urlencode(params)

    def send(self, area_code, local_number, msg, time=None, priority=None):
        """
        :param area_code: area code to send sms
        :param local_number: local number to send sms
        :param msg: message to send
        :param time: time to send sms (optional)
        :param priority: priority to send sms (optional)
        :return: JSON
        """
        validate_phone_number(area_code, local_number)
        kwargs = {
            'num': '{}-{}'.format(area_code, local_number),
            'msj': msg
        }
        if time:
            kwargs['time'] = time
        if priority:
            validate_priority(priority)
            kwargs['priority'] = priority
        r = requests.get(self._url(cmd='enviar', **kwargs))
        return r.json()

    def send_many(self, phone_numbers, msg, time=None, priority=None):
        """
        :numbers: array of tuple of numbers to send sms as follows:
        [(area_code1, local_number1), (area_code2, local_number2), (area_code3, local_number3), ...]
        :param msg: message to send
        :param time: time to send sms (optional)
        :param priority: priority to send sms (optional)
        :return: JSON
        """
        validate_phone_numbers(phone_numbers)
        kwargs = {
            'num': ','.join(['{}-{}'.format(*phone_number) for phone_number in phone_numbers]),
            'msj': msg
        }
        if time:
            kwargs['time'] = time
        if priority:
            validate_priority(priority)
            kwargs['priority'] = priority
        r = requests.get(self._url(cmd='enviar', **kwargs))
        return r.json()

    def sent(self, last_id=0, max_id=0):
        """
        :param last_id: A sms in particular
        :return: JSON array with the sms sent
        """
        kwargs = {
            'ultimoid': last_id,
            'maxid': max_id
        }
        r = requests.get(self._url(cmd='enviados', **kwargs))
        return r.json()

    def received(self, last_id=0):
        """
        :param last_id: A sms received in particular
        :return: JSON array with sms received
        """
        kwargs = {
            'ultimoid': last_id
        }
        r = requests.get(self._url(cmd='recibidos', **kwargs))
        return r.json()

    def status(self):
        """
        :return: JSON with service status
        """
        r = requests.get(self._url(cmd='estado'))
        return r.json()

    def balance(self):
        """
        :return: JSON with Balance of your account
        """
        r = requests.get(self._url(cmd='saldo'))
        return r.json()

    def cancel_queue(self):
        """
        Cancel sms queued
        :return: JSON
        """
        kwargs = {}
        if self.lineid:
            kwargs['lineid'] = self.lineid
        r = requests.get(self._url(cmd='cancelqueue', **kwargs))
        return r.json()
