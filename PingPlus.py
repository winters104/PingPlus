##PingPlus
##Ping with extra bits
##https://github.com/rmgr/PingPlus

import os,time,argparse,urllib2
###
#1st run? Get this https://raw.github.com/samuel/python-ping/master/ping.py
###
try:
    import ping
except ImportError:
    print ('First run, downloading pure Python Ping Implementation.')
    print ('https://raw.github.com/samuel/python-ping/master/ping.py')
    try:
        pingpy = urllib2.urlopen('https://raw.github.com/samuel/python-ping/master/ping.py')
        output = open('ping.py','wb')
        output.write(pingpy.read())
        output.close()
        print ('Ping.py downloaded successfully.')
        import ping
    except:
        print ('Download failed. Submit a bug report at https://github.com/rmgr/PingPlus')
        print ('Sorry :(')
        exit()

#Handle arguments

parser = argparse.ArgumentParser(description='Pings an ip with logging and interval options')
parser.add_argument('-i','--interval', help="time between pings",required=False)
parser.add_argument('-t','--timestamp', action="store_true", help="attach time to each ping", required=False)
parser.add_argument('-c','--count', help="maximum number of pings", required=False)
parser.add_argument('-l','--log', help="log output to a file", required=False)
parser.add_argument('destination',help="destination to ping")
args = parser.parse_args()

if args.count == None:
    count = -1
else:
    count = int(args.count)

if args.log == None:
    log = -1
else:
    log = open(args.log+'.txt','w')
    
if args.interval == None:
    interval = 5 #Default to 5 seconds if no interval is specified.
else:
    interval = args.interval
    
looping = True

#Lets get to pinging
while looping:
    #Logging will require a reimplementation of ping.verbose_ping or something- looking at that later

    if args.timestamp == True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    ping.verbose_ping(args.destination,2,1)
    if count > 0:
        count = count - 1
    if count == 0:
        looping = False
    time.sleep(float(interval))
