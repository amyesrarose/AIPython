'''
1) How to read a file
2) how to write into a file
3) How to append the data inside a file




Syntax:
file = open("filePath","mode").  mode is permission level

mode -

r -> read
r+ -> read+write
a -> append
w -> write(override)
w+ - write + read


methods:
read()
readline()
readines()
write()

*******file.seek(0) -> return cursor(position to first line)
readline -> reads line and move cursor to the new line ***


cvs, txt,pdf


use. file.close() when done to prevent corraptions

with open("prompt.pdf","r") as fileData: 
dat1= fileData.read()
perint(data1)

r+ -> read primary action, it needs to be in my system
w+ -> primary is writing,  sile does not have to be in the my system , it can create itself

'''