import os
import sys
import json
import re

args = sys.argv


# use args length to determine which starting dir to use

if len(args) < 2:
    startDir = os.getcwd()

if len(args) > 1:
    startDir = args[1]
    print(startDir)




tally = {
    'files': 0,
    'dirs': 0
}

fileTypeTally = {}

mostCurlyBraces = ('key', 0)

# exclude package library directories
excludeDirs = set(['node_modules', 'vendor', ''])

#exclude auto-generated files
excludeFiles = set(['_ide_helper.php', 'package-lock.json', 'composer.lock', '_ide_helper_models.php', '.phpunit.result.cache', 'main.bundle.js', 'main.bundle.js.map'])

for dirPath, dirs, files in os.walk(startDir):
    dirs[:] = [dir for dir in dirs if dir not in excludeDirs]
    files[:] = [file for file in files if file not in excludeFiles]
#     for dir in dirs:
    tally['dirs'] += 1

    for file in files:
        name, ext = os.path.splitext(file)
        tally['files'] += 1

        path = dirPath + '/' + file;
        print('file: ' + path)
        with open(path) as openFile:
            print(path)
            try:
                readFile = openFile.read()

            except Exception as e:
                print(e)

            else:
                # regex eliminates double curlies as found in blade and react
                braces = ''.join(re.findall('(?<!{){(?!{)|(?<!})}(?!})', readFile))
                print(braces)
                bracePairCount = 0
                if len(braces) % 2 != 0:
                    continue
                # until we run out of braces or if we don't have an even number
                while len(braces) > 0:
                    
                    splitBraces = ''.join(braces.split("{}", 1))

                    # if no braces are removed from the string, there are no remaining pairs so break
                    if splitBraces == braces:
                        break

                    # otherwise, increment the brace pair count and set braces to equal splitBraces
                    bracePairCount += 1
                    braces = splitBraces

                print(bracePairCount)
                if bracePairCount > mostCurlyBraces[1]:
                    mostCurlyBraces = (path, bracePairCount)

                print(mostCurlyBraces)


# Playing with counting file types
        if ext and ext in fileTypeTally:
# increment filetype
            fileTypeTally[ext] += 1
        elif ext:
#  add new file type
            fileTypeTally.update({ext: 1})



print(tally)

print(mostCurlyBraces)

for ext, count in fileTypeTally.items():
    print(ext, count)

# sys.exit - set code break with sys.exit(0)

#         #   fileTypeTally[ext] = 0
#
#         # with open(file) as openFile:
#         #     read = openFile.read()
#         #     fileContents.append(read)
