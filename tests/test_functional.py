import unittest
import mock
from mock import MagicMock
from smsc import SMSC

from smsc.utils import sms_is_limited, sms_length, sms_rest, sms_parse


class TestFunctional(unittest.TestCase):

    @mock.patch('smsc.smsc.requests')
    def test_send_mobile_number(self, mock_request):
        resp_mock = MagicMock()
        resp_mock.json.return_value = {'data': {'id': 16829892, 'sms': 1},
                                       'message': 'Mensaje enviado.',
                                       'code': 200
                                       }

        mock_request.get.return_value = resp_mock
        sms = SMSC(alias='test', apikey='test')
        resp = sms.send(area_code='011',
                        local_number='1531268974', msg='testing')
        assert mock_request.get.called
        assert resp == {'data': {'id': 16829892, 'sms': 1},
                        'message': 'Mensaje enviado.', 'code': 200}
