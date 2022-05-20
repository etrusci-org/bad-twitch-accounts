#!/usr/bin/env python3

import os
import json
import datetime


srcFile = os.path.join('src', 'data.json')
outFile = [
    {
        'fileName': os.path.join('list', 'plain.txt'),
        'lineFormat': '{username}\n',
    },
    {
        'fileName': os.path.join('list', 'cmd-slash.txt'),
        'lineFormat': '/ban {username} {reason}\n',
    },
    {
        'fileName': os.path.join('list', 'cmd-dot.txt'),
        'lineFormat': '.ban {username} {reason}\n',
    },
]


def bakeList():
    with open(srcFile, 'r') as fSrc:
        data = json.load(fSrc)
        dtNow = datetime.datetime.utcnow()
        nfoText = 'last update: {0} UTC\n\n'.format(dtNow)
        for listFileConf in outFile:
            with open(listFileConf['fileName'], 'w') as fList:
                fList.write(nfoText)
                for v in sorted(data, key=lambda v: v['username'].lower()):
                    fList.write(listFileConf['lineFormat'].format(**v))


if __name__ == '__main__':
    bakeList()
