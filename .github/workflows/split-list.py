#!/usr/bin/python3

from math import ceil
import sys

iput = sys.stdin.read()

lst = iput.split(",")
# Remove hiviewdfx_* as mapping it takes hours, to be debugged
lst.remove("hiviewdfx_hiview_lite")
lst.remove("hiviewdfx_hiview")
lst.remove("hiviewdfx_hilog_lite")
lst.remove("hiviewdfx_hilog")
lst.remove("hiviewdfx_hievent_lite")
lst.remove("hiviewdfx_hidumper_lite")
lst.remove("hiviewdfx_hidumper")
lst.remove("hiviewdfx_hicollie")
lst.remove("hiviewdfx_hichecker")
lst.remove("hiviewdfx_hiappevent")
lst.remove("hiviewdfx_faultloggerd")
lst.remove("hiviewdfx_blackbox")
lst.remove("hiviewdfx_blackbox_lite")
lst.remove("hiviewdfx_hitrace")
lst.remove("hiviewdfx_hisysevent")

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
