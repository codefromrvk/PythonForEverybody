# Write a program that prompts for a file name,
#  then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average
#  of those values and produce an output as shown below.
# Do not use the sum() function or a variable
# named sum in your solution.
count=0
total=0
fname=input("Enter your file name:")
fh=open(fname)
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        linevar=line
        count=count+1
        pos=linevar.find('0')
        num=float(line[pos:])
        total=total+num
avg=total/count
print("Average spam confidence:",avg)

# help given
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     print(line)
# print("Done")
