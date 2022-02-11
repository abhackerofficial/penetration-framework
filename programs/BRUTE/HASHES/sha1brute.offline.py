#!/bin/python2

import hashlib
import time
import sys
import getopt

sha1_hash = raw_input('\033[4mpsf\033[0m set(\033[91mhash/sha1\033[0m) > ')
pwdfile = raw_input('\033[4mpsf\033[0m use(\033[91mwordlist/path\033[0m) > ')

try:
    pwdfile = open(pwdfile,"r")
except:
    print ("\n\033[91m(\033[0m!\033[91m)\033[0m Invalid wordlist path!\033[0m\n")
    quit()
counter = 1
for password in pwdfile:
    hash_obj = hashlib.sha1(password.strip())
    filesha1 = (hash_obj.hexdigest())
    start = time.time()
    print "\033[91mChecking passowrd %d: %s\033[0m" % (counter, password.strip())

    counter += 1
    end = time.time()
    t_time = (end - start)

    if sha1_hash == filesha1:
        print "\n\033[92mPassword Found :) \nPassword is : %s\033[36m" % password
        print "\033[92mTime taken: \033[0m", t_time, "seconds\033[0m"
        time.sleep(0.125)
        break
else:
    print "\n\033[1;32m[\033[1;31m!\033[1;32m]\033[1;31mPassword not Found! :(\033[0m"