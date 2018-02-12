## Getting Started
You should be register in [SMSC](https://www.smsc.com.ar/usuario/iniciar/) and then get an alias and apikey. 

## Install
```
pip install smsc
```

## Examples
```
# imports
from smsc import SMSC

# create an instance
sms = SMSC(alias='your_alias', apikey='your_api_key')

# send an sms
result = sms.send(area_code='123', local_number='4567890', msj='Holla world!')

# sms sents
result = sms.sent()

# sms sents
result = sms.sent()

# sms recieved
result = sms.received()

# get status
result = sms.status()

# get balance
result = sms.balance()

# cancel queue sms
result = sms.cancel_queue()
```

## Exceptions
``` AreaCodeSMSCError ```
``` LocalNumberSMSCError ```
``` PhoneNumberLongSMSCError ```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
