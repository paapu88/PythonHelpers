# example
#  python3 ~/Dropbox/Apu/replace.py --stringOld ".example" --stringNew ".tinyYolo3lFloat32" --suffixes [".py", ".md"]
#
# by markus.kaukonen@iki.fi

import pathlib
import argparse

parser = argparse.ArgumentParser(description='In current directory and all its subdirectories, in files ending in any of the suffixes: replace stringOld by stringNew')
parser.add_argument('-sOld', '--stringOld', dest = 'stringOld', help='String to be replaced in all files', required=True)
parser.add_argument('-sNew', '--stringNew', dest = 'stringNew', help='The new rplacing string in all files', required=True)
parser.add_argument('--suffixes', nargs='+', dest='suffixes',
                                help='List of suffixes of accepted files',
                                default=None)
suffixes = ['.py', '.md']
kill = '.example'
replace = '.tinyYolo3lFloat32'
p = pathlib.Path('./')
filenames = []
for i in p.glob('**/*'):
    if i.suffix in suffixes:
            filenames.append(i)
#print(filenames)
for filename in filenames:
    with open(filename) as f:
        file_str = f.read()

    # do stuff with file_str
    file_str = file_str.replace(kill, replace)

    with open(filename, "w") as f:
        f.write(file_str)
