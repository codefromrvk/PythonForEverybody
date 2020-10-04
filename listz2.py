fh = open('mbox-short.txt')
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        piecesList=line.split()
        print(piecesList[2])

#or
# fh = open('mbox-short.txt')
# for line in fh:
#     line=line.rstrip()
#     wds=line.split()
#     #guardian
#     if len(wds)< 3 or wds[0]!='From':#cant interchange 'or' terms if len9wds is as 2nd term program blows
#         continue
#         print(wds[2])
