#!/usr/bin/python3

from math import ceil
import sys
import random

if len(sys.argv) < 2:
    print("Usage: {} <number_of_chunks>".format(sys.argv[0]))
    sys.exit(1)

try:
    chunks = int(sys.argv[1])
    if chunks <= 0:
        raise ValueError("Number of chunks must be greater than zero.")
except ValueError as e:
    print("Error: {}".format(e))
    sys.exit(1)

iput = sys.stdin.read()

lst = iput.split(",")

# Repos with files over 100 MB -> error: GH001: Large files detected
lst.remove("developtools_profiler")
lst.remove("developtools_smartperf_host")
lst.remove("device_soc_rockchip")
lst.remove("global_i18n")
lst.remove("third_party_mindspore")
lst.remove("multimedia_audio_framework")
lst.remove("multimedia_av_codec")

# error: GH008: Your push referenced at least 1 unknown Git LFS object
lst.remove("device_board_hihope")

# send-pack: unexpected disconnect while reading sideband packet
lst.remove("third_party_vk-gl-cts")

# fatal: destination path '/github/workspace/hub-mirror-cache/update_updater' already exists and is not an empty directory.'
lst.remove("update_updater")

# LFS upload to github failed
lst.remove("xts_acts")

# Timeout gitee clone
lst.remove("docs")

# fatal: pack exceeds maximum allowed size (2.00 GiB)   
lst.remove("kernel_linux_6.6")

n = 1
size = ceil(len(lst) / chunks)
print("%d chunks with a chunk size of %d" % (chunks, size))

random.shuffle(lst) # shuffle the list to better distribute the workload between the chunks

while lst:
    chunk, lst = lst[:size], lst[size:]
    filename = 'repo_list' + str(n) + '.txt'
    repos = ','.join(chunk)
    print("Filename for output: %s" % filename)
    print("List of repos to write: %s" % repos)
    with open(filename, 'w', encoding="utf-8") as text_file:
        text_file.write("%s" % repos)
    n = n+1
