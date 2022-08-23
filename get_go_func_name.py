import os, sys, re

if len(sys.argv) < 3:
    print('python "file_path" "pattern"')
    exit(0)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if re.search(sys.argv[2], line):
            if line[-1] == '\n':
                line = line[:-1]
            if line[-2:] == " {":
                line = line[:-2]
            print(line)