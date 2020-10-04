fname=input("Enter the file name:")
fh=open(fname)
sum=0
import re
for line in fh:
    y=re.findall('[0-9]+',line)
    # if y!=[]:
    for num in y:
        sum=sum+int(num)
print(sum)
