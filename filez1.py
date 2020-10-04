fh=open("mybox-short.txt")

for line in fh:
    line=line.rstrip()
    print(line.upper())
