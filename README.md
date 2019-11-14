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
b'\xe5\xb8\x9d\xe7\x8e\x8b\xe8\xa7\x80\xe6\x8c\x87\xe7\xa5\x96'
'            ╭─────────╮'
'            |BabyRage!|'
'            ╯─────────╯'
'          ███]▄▄▄▄▄▄▄▃～～～'
' ▂▄▅████████████▅▄▃▂'
'[██████████████████████]'
'◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙ ◤ '
``` 

The normal will be the unicode from random nonsense word and with the option  `flush=True`, it will be a tank(嬰靈戰車) help you to log things