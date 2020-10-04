# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname=input("Enter the file name:")
if len(fname)< 1: fname="mbox-short.txt"
fh=open(fname)
count={}
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        piecesList=line.split()
        timeString=piecesList[5]
        s=timeString.split(':')
        hour=s[0]
        count[hour]=count.get(hour,0)+1
# alternative
# lst=sorted([(k,v) for k,v in count.items()])
# for k,v in lst:
#     print(k,v)
lst=[]
for k,v in count.items():
    a=(k,v) #manually creating tuple inside a list; here a is a tuple
    lst.append(a)
lst=sorted(lst)
for k,v in lst:
    print(k,v)
