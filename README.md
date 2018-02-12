## Getting Started
You should be register in [SMSC](https://www.smsc.com.ar/usuario/iniciar/) and then get an alias and apikey. 

## Install
```
pip install smsc
```

## Usage
Create an instance
```
from smsc import SMSC
sms = SMSC(alias='your_alias', apikey='your_api_key')
```

Send an SMS
```
result = sms.send(area_code='123', local_number='4567890', msj='Hello world!')
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

## Contributing
1. Fork it ( https://github.com/joaquinmoine/smsc-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
