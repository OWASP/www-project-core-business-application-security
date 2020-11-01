#!/usr/bin/env python
# This script uses a list op IP-adresses of SAProuters connected to the internet and
# run the SAPROUTER -L command against it to see if the configuration is safe

#import the necessary modules
import sys 			#for parsing command line opts
import subprocess	#for running OS command SAPROUTER
import time
import glob
 
# if file is specified on command line, parse, else ask for file
if sys.argv[1:]:
    print "File: %s" % (sys.argv[1])
    logfile = sys.argv[1]
else:
    logfile = raw_input("Please enter a file with RAProuter IP adresses to parse: ")
 
 
 
try:
    # open the file with IP adresses and open a logfile for the output
    file = open(logfile, "r")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    log = open('log%s.txt' % timestr, 'a')

    # read through the file
    for text in file.readlines():
       #strip off the \n
        text = text.rstrip()
       #write the IP-adress in the output for reference purposes later as the output only display a resolved hostname normally
        log.write(text)
       #run saprouter -L command and wait for it to finish
        log.flush()
        process = subprocess.Popen(['saprouter', '-L', '-H', text], stdout=log, stderr=log, shell=True)
        ret_code = process.wait()
        log.flush()
        log.write('_________________________________________________________________________________________________________________________________\n')

		#cleanup and close file
    file.close()
	
#catch any standard error (we can add more later)
except IOError, (errno, strerror):
    print "I/O Error(%s) : %s" % (errno, strerror)
