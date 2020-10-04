import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
d={}
for line in fh:
    if not line.startswith('From: '): continue
    line=line.strip()
    pieces = line.split()
    email = pieces[1]
    # print(pieces)
    # lst.append(email)
    z=pieces[1].split("@")

    if z[1] not in d:
        d[z[1]]=1
    else:
        for i,v in d.items():
            if z[1]==i:
                v=v+1
                u={z[1]:v}
                d.update(u)
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    print(row)
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC '
for row in cur.execute(sqlstr):
    print(row[0],row[1])

largest=None
for h,s in d.items():
    if largest==None:
        largest=s
        name=h
    elif s>largest:
        largest=s
        name=h
print(name,largest)

#     z=row[0].split("@")
#     if z[1] in lst:
#         s=s+row[1]
#     else:
#         lst.append(z[1])
#         s=row[1]
# print(lst)
# d={}
# for i in lst:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# print(d)


cur.close()
