#!/usr/bin/python3
import re

with open ('testing.txt', 'r') as file:
    for line in file:
        matches=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
        print('\n'.join(map(str, matches)))
