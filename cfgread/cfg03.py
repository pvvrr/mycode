#!/usr/bin/env python3
## create file object in "r"ead mode

counter = 0 # counter to count the lines in file
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    for x in configlist:
        counter = counter + 1

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(" No of lines in config file : ", counter)


