import os, zipfile

with zipfile.ZipFile('aaa.zip','w', zipfile.ZIP_STORED) as target:
    for i in os.walk('aa'):
        for n in i[2]:
            path = ''.join((i[0], '\\', n))
            name = '\\'.join(path.split('\\')[1:])
            print(path)
            print(name)
            target.write(path, name)