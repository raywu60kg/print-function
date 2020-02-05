# print-function
[![image](https://img.shields.io/pypi/v/print-function.svg)](https://python.org/pypi/print-function)
[![image](https://img.shields.io/pypi/dm/print-function.svg)](https://python.org/pypi/print-function)
[![Build Status](https://travis-ci.org/raywu60kg/print-function.svg?branch=master)](https://travis-ci.org/raywu60kg/print-function)
<!--[![image](https://img.shields.io/pypi/pyversions/print-function.svg)](https://python.org/pypi/print-function)-->
### Install
```
$ pip install print-function
```

### Usage
If we put `from ___future___ import *` on our python script, it will overwrite our print and become like

```python
from ___future___ import *
print("123")
print("BabyRage!", flush=True)

# output 
b'\xe5\xa4\xa9\xe7\x8e\x89\xe8\x8a\xb1\xe8\xa5\xbf\xe7\xbe\x8e'
'            ╭─────────╮'
'            |BabyRage!|'
'            ╯─────────╯'
'       ███]▄▄▄▄▄▄▄▃～～～'
' ▂▄▅█████████▅▄▃▂'
'[████████████████]'
'◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙ ◤ '
``` 

The normal `print` will be the unicode from random nonsense word and with the option  `flush=True`, it will be a tank(嬰靈戰車) help you to log things
