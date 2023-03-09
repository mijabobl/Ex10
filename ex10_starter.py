import sys
import glob
import os
from os.path import getsize

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
# TODO: Use the glob.glob() function to obtain the list of filenames
# TODO: use os.path.getsize to find each file's size
# TODO: Add a test to only display files that do not have a size of zero
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

path = r'C:\Users\rebjo\OneDrive\Desktop\IntoTech\*.*'
print("files in another directory")
print(glob.glob(path))

filez = glob.glob("*.*")
print("files in this directory")
print(filez)
print()

for f in filez:
    if getsize(f) > 0:
        print(f, getsize(f))

size = 0                                    #none of this works
for files in os.walk(path):                 #just running some ideas through!
    size = os.path.getsize(filez)           #trying to find files in a directory
print("file size is ", size)                #and get the size in a loop
print()                                     #and print them

filePath = r'C:\Users\rebjo\PycharmProjects\Exercise10\ex10_starter.py'
fileSize = os.path.getsize(filePath)
basename = os.path.basename(filePath)
if fileSize > 0:
    print(basename, "contains", fileSize, "bytes")
else:
    print("i wont display this file, its nothing")



print("hdir is: ", hdir)