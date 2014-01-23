#PingPlus

Ping with extra bits.

##Usage

```
PingPlus.py [-h] [-i INTERVAL] [-t] [-c COUNT] [-l LOG] destination
Pings an ip with logging and interval options
positional arguments:
  destination                         destination to ping   

optional arguments:   
  -h, --help                          show this help message and exit   
  -i INTERVAL, --interval INTERVAL    time between pings   
  -t, --timestamp                     attach time to each ping   
  -c COUNT, --count COUNT             maximum number of pings   
  -l LOG, --log LOG                   log output to a file - THIS DOESN'T WORK YET.
```

##Wanna contribute?
Find something I've done wrong or want to add a feature? Feel free to fix it and chuck me a pull request! Otherwise you're always welcome to drop me a message on the issue tracker on [Github](https://github.com/rmgr/PingPlus/issues).

##Credit
I'm using [Samuel Stauffer's](https://github.com/samuel/python-ping) great Python Ping implementation.

