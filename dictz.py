# 9.4 Write a program to read through the mbox-short.txt
#  and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and
#  takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps
#  the sender's mail address to a count
#  of the number of times they appear in the file.
#  After the dictionary is produced, the program reads
#  through the dictionary using a maximum loop to find the most prolific committer.
fname=input("Enter the file name:")
counts={}
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        piecesList=line.split()
        print(piecesList)
        name=piecesList[1]
        counts[name]=counts.get(name,0)+1
        print(counts[name])
bigname=None
bigcount=None
for k,v in counts.items():
    if bigcount is None or bigcount <v :
        bigname=k
        bigcount=v
print(bigname,bigcount)

# help code
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)



# d={2:1,'b':3,'c':56}
# print(d)
# for k,v in d.items():
#     print(k,v)
# stuff = {}
# print(stuff.get('candy',-1))#if candy not there return -1
# print(stuff)
