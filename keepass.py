
import csv
from pykeepass import PyKeePass

kp = PyKeePass('E:\坚果云\PwdDB\pwdDB.kdbx', password="Zz960518")

groups = kp.find_groups(name="Chrome", first=True)

for entry in groups.entries:
    print(entry.password)

with open('C:\\Users\\XZX\\Desktop\\Chrome 密码.csv', encoding="utf-8") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        kp.add_entry(groups, title=row['name'] + "-" + row['url'], username=row['username'], password=row['password'], url=row['url'])
        print(row)

kp.save()