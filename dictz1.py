fname=input("Enter the file name:")
if len(fname)<1:fname='mbox-short.txt'
di={}
fh=open(fname)
for line in fh:
    line=line.rstrip()
    piecesList=line.split()
    #for item in piecesList:
    for item in piecesList:
        di[item]=di.get(item,0)+1
bigname=None
bigcount=None
for k,v in di.items():
    if bigcount is None or bigcount <v :
        bigname=k
        bigcount=v
print(bigname,bigcount)
