## Getting Started
You should be register in [SMSC](https://www.smsc.com.ar/usuario/iniciar/) and then get an alias and apikey. 

## Install
```
pip install smsc-python
```

## Usage
Create an instance
```
from smsc import SMSC
sms = SMSC(alias='your_alias', apikey='your_api_key')
```

Send an SMS
```
result = sms.send(area_code='123', local_number='4567890', msg='Hello world!')
result = sms.send_many([('123', '4567890'), ('321', '6549870')], msg='Hello world!')
```

SMS sents
```
result = sms.sent()
```

SMS recieved
```
result = sms.received()
```

Get status
```
result = sms.status()
```

Get balance
```
result = sms.balance()
```

Cancel queue SMS
```
result = sms.cancel_queue()
```

`All results return an JSON with the keys 'code', 'message', 'data'`

## Exceptions
``` 
from smsc.exceptions import AreaCodeSMSCError, LocalNumberSMSCError, PhoneNumberLongSMSCError
try:
  result = sms.send(area_code='123', local_number='4567890', msj='Hello world!')
except AreaCodeSMSCError:
  ...
except LocalNumberSMSCError:
  ...
except PhoneNumberLongSMSCError:
  ...
```

## Utils
``` 
from smsc.utils import sms_is_limited, sms_length, sms_rest, sms_parse

sms_is_limited('abc') # return False
sms_is_limited('abcñ') # return True

sms_length('abc') # return 3, 160
sms_length('abcñ') # return 4, 70

sms_rest('abc') # return 157
sms_rest('abcñ') # return 66

sms_parse('long_text...') # return [['first_sms'], ['second_sms'], ...]
```

## Validations
```
from smsc.validations import validate_area_code, validate_local_number, validate_length_phone_number

validate_area_code('1324') # return True
validate_area_code('132456') # return False

validate_local_number('567890') # return True
validate_local_number('1234') # return False

validate_length_phone_number('1234567890') # return True
validate_length_phone_number('12345678') # return False
```

## Contributing
1. Fork it ( https://github.com/joaquinmoine/smsc-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
