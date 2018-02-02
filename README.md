A python client to the riksbanken.se SOAP api
---

https://www.riksbank.se/sv/statistik/sok-rantor--valutakurser/oppet-api/

Currently only used to print daily exchange rates in bash-friendly format.

Installation
###

```
# ./setup.py install
```

Use the cmdline
###

```
# currencyrates
SEKEURPMI=9.8292;SEKUSDPMI=7.855

```

Sammple use in a script:

```
#!/usr/bin/env bash

eval `currencyrates`
do_something $SEKEURPMI
or_something_else $SEKUSDPMI

```
