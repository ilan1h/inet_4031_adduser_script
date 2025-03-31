#!/usr/bin/python3

# INET4031
# Ilan Aguilar Sanchez
# 3/24/25
# D3/30/25

#import os (operating system) lets the program interact and run on the operating system
import os
#import re (regular expression) allows for the program to check if a string has a certain character(s)
import re
#import sys to make sure inputs and outputs can interacted in the program
import sys 

def main():
    for line in sys.stdin:

        #match is looking for the "#" character at the beginning of the line
        #this "#" is used to block certain lines from the "create=users.input" file, so the program doesn't error out
        match = re.match("^#", line)

        #each individual entry is categorized by the ":", making sure there are no overlapping fields
        fields = line.strip().split(':')

        #"if" is checking is match is valid or when there are not exactly 5 fields, when true, it will skip the rest of the program
        if match or len(fields) != 5:
            continue

        #the username and password are stored in fields 0 and 1, respectively, while gecos is built using fields 3 and 2, which are last and first name of the user
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        #if there are multiple groups within a username, it will split the groups into two indivdual groups
        groups = fields[4].split(',')

        #clarification of the account creation for the specific user
        print("==> Creating account for %s..." % (username))
        #this is the creation of the account in the adduser file. Using gecos for the last and first name, username for the username, and not needing a password right away
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        
        #before running "os.system(cmd)" is important to print out "cmd" to know the outcome. When "os.system(cmd)" becomes uncommented, it will change the system
        print(cmd)  
        os.system(cmd)  

        #clarification of the password creation for the specific user
        print("==> Setting the password for %s..." % (username))
        #a password will be created, and the user will only need to enter it once as it is "echo'd/repliacted" and seperated by the new line. It is sudo'd to make sure the password is set to the username correctly
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        #before running "os.system(cmd)" is important to print out "cmd" to know the outcome. When "os.system(cmd)" becomes uncommented, it will change the system
        print(cmd) 
        os.system(cmd)

        for group in groups:
            #if looks for groups that do contain the "-" characteor in the field, if they do not contain the "-", it will assign the username to the group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
