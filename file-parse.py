import os
import sys
import re

sen_re = re.compile('Seria.*\s(\d+-\d+)')
prt_re = re.compile('ssh.* -p.*\s(\d+)')


def get_values(lines):
    sen = sen_re.match(lines[-2]).group(1)
    prt = prt_re.match(lines[-1]).group(1)
    return sen, prt

path = '.'
if len(sys.argv) > 1:
    path = sys.argv[1]

file_names = os.listdir(path)
for file_name in file_names:
    with open(path +file_name) as f:
        sn, prt = get_values(f.readlines())
        output = '{file_name}:{serial_number}:{port}'.format(
            file_name = file_name,
            serial_number = sn, 
            port = prt
        )
        print(output)