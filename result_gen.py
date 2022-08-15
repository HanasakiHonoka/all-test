


import random,math

list = '''40742
45151
47040
48069
48790
49941
48179
41758
35583
29846
25239
22501
16749
12619
11607
11875
11811
8587
8974
8459
7309
7643
7814
6814
5814
3814
3814
3814
'''

day_b = list.split('\n')

for i in range(len(day_b)):
    item = int(int(day_b[i]) - 10000)
    print(item)
    # print(item + random.randint(5000, 6500))
    # print("%.2f" % (math.log(item) - 1))