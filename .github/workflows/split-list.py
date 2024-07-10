#!/usr/bin/python3

from math import ceil
import sys

iput = sys.stdin.read()

lst = iput.split(",")

# Repos with files over 100 MB -> error: GH001: Large files detected
lst.remove("developtools_profiler")
lst.remove("developtools_smartperf_host")
lst.remove("device_soc_rockchip")
lst.remove("global_i18n")
lst.remove("third_party_mindspore")

# error: GH008: Your push referenced at least 1 unknown Git LFS object
lst.remove("device_board_hihope")

# curl 92 HTTP/2 stream 5 was not closed cleanly: INTERNAL_ERROR (err 2)
lst.remove("multimedia_av_codec")
lst.remove("kernel_linux_5.10")
lst.remove("third_party_llvm-project")
lst.remove("kernel_linux_4.19")
lst.remove("kernel_linux")
lst.remove("third_party_typescript")

# send-pack: unexpected disconnect while reading sideband packet
lst.remove("third_party_vk-gl-cts")

# fatal: destination path '/github/workspace/hub-mirror-cache/update_updater' already exists and is not an empty directory.'
lst.remove("update_updater")

# FileNotFoundError('[Errno 2] No such file or directory: '/github/workspace/hub-mirror-cache/third_party_noto-cjk'')
lst.remove("third_party_noto-cjk")

# LFS upload to github failed
lst.remove("xts_acts")

# Timeout gitee clone
lst.remove("docs")
#lst.remove("")

chunks = 10
n = 1
size = ceil(len(lst) / chunks)
print("%d chunks with a chunks size of %d" %(chunks, size))

while lst:
    chunk, lst = lst[:size], lst[size:]
    filename = 'repo_list' + str(n) + '.txt'
    repos = ','.join(chunk)
    print("Filename for output: %s" % filename)
    print("List of repos to write: %s" % repos)
    with open(filename, 'w', encoding="utf-8") as text_file:
        text_file.write("%s" % repos)
    n = n+1
