import os
import sys
import json

args = sys.argv


# use args length to determine which starting dir to use

if len(args) < 2:
    startDir = os.getcwd()

if len(args) > 1:
    startDir = args[1]
    print(startDir)


fileContents = []

tally = {
    'files': 0,
    'dirs': 0
}

fileTypeTally = {}

curlyCount = {}

excludeDirs = set(['node_modules', 'vendor'])

for dirPath, dirs, files in os.walk(startDir):
    dirs[:] = [dir for dir in dirs if dir not in excludeDirs]
#     for dir in dirs:
    tally['dirs'] += 1

    for file in files:
        name, ext = os.path.splitext(file)
        tally['files'] += 1

        if ext in('.php'):
            path = dirPath + '/' + file;
            print('file: ' + path)
            with open(path) as openFile:
                read = openFile.read()
                fileContents.append(read)
                print(fileContents)
                sys.exit(0)
# Playing with counting file types
        if ext and ext in fileTypeTally:
# increment filetype
            fileTypeTally[ext] += 1
        elif ext:
#  add new file type
            fileTypeTally.update({ext: 1})

print(tally)
print(fileContents)
for ext, count in fileTypeTally.items():
    print(ext, count)

# sys.exit - set code break with sys.exit(0)

#         #   fileTypeTally[ext] = 0
#
#         # with open(file) as openFile:
#         #     read = openFile.read()
#         #     fileContents.append(read)
