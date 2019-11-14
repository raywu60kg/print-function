# print-function
### Install
```
$ pip install print-function
```

### Usage
If we Put `from ___future___ import print` on our python script, it will overwrite our print and become like

```python
from ___future___ import print
print("123")
print("attack", flush=True)

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

The normal will be the unicode from random nonsense word and with the option  `flush=True`, it will be a tank(嬰靈戰車) help you to log things