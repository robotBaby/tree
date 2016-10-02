#!/usr/bin/env python3
import sys
import os
import string


def dfsTree(curPath, prefix):
    files = [x for x in os.listdir(curPath) if x[0] != '.']
    files = sorted(files)
    dirN, fileN = 0, 0
    for i, fname in enumerate(files):
        if i < len(files) - 1:
            curPrefix, subdirPrefix = "├── ", "│   "
        else:
            curPrefix, subdirPrefix = "└── ", "    "
        print(prefix + curPrefix + fname)
        if os.path.isfile(os.path.join(curPath, fname)):
            fileN += 1
        else:
            dirN += 1
            tdirN, tfileN = dfsTree(os.path.join(curPath, fname), prefix + subdirPrefix)
            dirN, fileN = dirN + tdirN, fileN + tfileN
    return dirN, fileN


def tree(path):
    print(path)
    dirN, fileN = dfsTree(path, "")
    print()
    print(str(dirN) + (" directories, " if dirN != 1 else " directorie, ") + str(fileN) + (" files" if fileN != 1 else " files"))


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    tree(path)
