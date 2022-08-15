


import os
import re

def work():
    for root, dirs, files in os.walk("D:\WorkSpace\learn-note\doc"):
        for file in files:
            if file.split(".")[1] == "md":
                file_path = os.path.join(root, file)
                # print(file_path)
                with open(file_path, encoding="utf-8") as f:
                    count = 1
                    for line in f:
                        if re.match(r'!\[.*', line):
                            if "http" in line:
                                print(count,line)
                            # print(count, line)
                        count += 1
    pass

if __name__ == '__main__':
    work()