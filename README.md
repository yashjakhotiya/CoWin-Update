# CoWin-Update
Is the CoWin website updated for registration?

This is a _very hacky_ PYTHON3 script to lookup the CoWin portal if they re-deployed their JS frontend to update validations (inspired from [@umanghome](https://twitter.com/umanghome/status/1387133294613983232)) and sound an alarm when they do.

1. `pip install -r requirements.txt`
2. `python can_i_register.py`

I tested this on Windows Powershell. If you want to test the alarm somewhere else, you might want to do,

```
from playsound import playsound
playsound('alarm.wav')
```
