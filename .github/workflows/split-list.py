#!/usr/bin/python3

from math import ceil
import sys

iput = sys.stdin.read()

lst = iput.split(",")
# Remove hiviewdfx_hisysevent as mapping it takes hours, to be debugged
lst.remove("hiviewdfx_hisysevent")
# Remove hiviewdfx_hitrace as a clone of this repo can take up to 5h
lst.remove("hiviewdfx_hitrace")
# Remove hiviewdfx_hiview as the creation of this repo can take up to 4.5h
lst.remove("hiviewdfx_hiview")

chunks = 8
n = 1
size = ceil(len(lst) / chunks)

while lst:
    chunk, lst = lst[:size], lst[size:]
    filename = 'repo_list' + str(n) + '.txt'
    repos = ','.join(chunk)
    print("Filename for output: %s" % filename)
    print("List of repos to write: %s" % repos)
    with open(filename, 'w', encoding="utf-8") as text_file:
        text_file.write("%s" % repos)
    n = n+1
