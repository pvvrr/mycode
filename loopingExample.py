#!/usr/bin/python3

COUNTER = 0

with open("dracula.txt","r") as foo:
    with open("vampytimex.txt","w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                COUNTER += 1
                fang.write(line)

print(COUNTER)

