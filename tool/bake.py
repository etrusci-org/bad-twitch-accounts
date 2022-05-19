#!/usr/bin/env python3

import os
import json
import datetime


f = {
    'src': os.path.join('src', 'data.json'),
    'plain': os.path.join('list', 'plain.txt'),
    'command': os.path.join('list', 'command.txt'),
}


def bakeList():
    with open(f['src'], 'r') as srcFile:
        srcData = json.load(srcFile)

        with open(f['plain'], 'w') as plainFile, open(f['command'], 'w') as commandFile:
            dtNow = datetime.datetime.utcnow()
            nfoText = 'last update: {0} UTC\n\n'.format(dtNow)

            plainFile.write(nfoText)
            commandFile.write(nfoText)

            for v in sorted(srcData, key=lambda v: v['username'].lower()):
                plainFile.write('{username}\n'.format(**v))
                commandFile.write('/ban {username} {reason}\n'.format(**v))


if __name__ == '__main__':
    bakeList()
