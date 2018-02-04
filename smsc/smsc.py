import requests
import urllib

from smsc.validations import validate_phone_number


class SMSC(object):
    def __init__(self, alias, apikey, apiversion='0.3', lineid=None):
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

    def send(self, area_code, local_number, msj, time=None):
        validate_phone_number(area_code, local_number)
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
