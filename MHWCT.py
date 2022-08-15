
correspondence = '''
 樱火龙	 Pink Rathian
 金火龙	 Gold Rathian
 雌火龙	 Rathian
 苍火龙	 Azure Rathalos
 银火龙	 Silver Rathalos
 火龙	 Rathalos
 黑角龙	 Black Diablos
 角龙	 Diablos
 麒麟	 Kirin
 黑龙	 Fatalis
 战痕黑狼鸟	 Scarred Yian Garuga
 黑狼鸟	 Yian Garuga
 激昂金狮子	 Furious Rajang
 金狮子	 Rajang
 钢龙	 Kushala Daora
 炎妃龙	 Lunastra
 炎王龙	 Teostra
 黑轰龙	 Brute Tigrex
 轰龙	 Tigrex
 熔岩龙	 Lavasioth
 迅龙	 Nargacuga
 霜刃冰牙龙	 Frostfang Barioth
 冰牙龙	 Barioth
 惶怒恐暴龙	 Savage Deviljho
 恐暴龙	 Deviljho
 土砂龙	 Barroth
 爆锤龙	 Uragaan
 煌黑龙	 Alatreon
 狱狼龙	 Stygian Zinogre
 雷狼龙	 Zinogre
 猛爆碎龙	 Raging Brachydios
 碎龙	 Brachydios
 硫斩龙	 Acidic Glavenus
 斩龙	 Glavenus
 雷颚龙	 Fulgur Anjanath
 蛮颚龙	 Anjanath
 大贼龙	 Great Jagras
 水妖鸟	 Coral Pukei-Pukei
 毒妖鸟	 Pukei-Pukei
 歼世灭尽龙	 Ruiner Nergigante
 灭尽龙	 Nergigante
 冥赤龙	 Safi'jiiva
 冥灯龙	 Xeno'jiiva
 熔山龙	 Zorah Magdaros
 搔鸟	 Kulu-Ya-Ku
 泥鱼龙	 Jyuratodus
 痹毒龙	 Viper Tobi-Kadachi
 飞雷龙	 Tobi-Kadachi
 浮眠龙	 Nightshade Paolumu
 浮空龙	 Paolumu
 霜翼风漂龙	 Shrieking Legiana
 风漂龙	 Legiana
 大痹贼龙	 Great Girros
 凶爪龙	 Ebony Odogaron
 惨爪龙	 Odogaron
 骨锤龙	 Radobaan
 雾瘴尸套龙	 Blackveil Vaal Hazak
 尸套龙	 Vaal Hazak
 岩贼龙	 Dodogama
 绚辉龙	 Kulve Taroth
 红莲爆鳞龙	 Seething Bazelgeuse
 爆鳞龙	 Bazelgeuse
 眩鸟	 Tzitzi-Ya-Ku
 贝希摩斯	 Behemoth
 冰鱼龙	 Beotodus
 猛牛龙	 Banbaro
 冰呪龙	 Velkhana
 溟波龙	 Namielle
 天地煌啼龙	 Shara Ishvalda
 古代鹿首精	 Ancient Leshen
 鹿首精	 Leshen

'''

table = {}
def work():
    raw = open("D:\Kit\CT Table\MonsterHunterWorld.CT", 'r', encoding='utf-8')
    new = open("./res/MonsterHunterWorld_1.CT", 'w', encoding='utf-8')

    lines = raw.readlines()
    for line in lines:
        for key, val in table.items():
            # print(key, val)
            line = line.replace(key, val)
        new.writelines([line])

    raw.close()
    new.close()

    pass

def gen_table():
    lines = correspondence.strip().split("\n")
    for line in lines:
        items = line.split("\t")
        table[":"+items[1].strip()]=":"+items[0].strip()

def test():
    text = '''
    1:Rathalos
4:Zorah Magdaros
7:Great Jagras
9:Rathian
10:Pink Rathian
11:Azure Rathalos
12:Diablos
13:Black Diablos
14:Kirin
16:Kushala Daora
17:Lunastra
18:Teostra
19:Lavasioth
20:Deviljho
21:Barroth
22:Uragaan
24:Pukei-Pukei
25:Nergigante
26:Xeno'jiva
27:Kulu-Ya-Ku
28:Tzitzi-Ya-Ku
29:Jyuratodus
30:Tobi-Kadachi
31:Paolumu
32:Legiana
33:Great Girros
34:Odogaron
35:Radobaan
36:Vaal Hazak
37:Dodogama
39:Bazelgeuse
    '''
    lines = text.strip().split('\n')
    for line in lines:
        for key, val in table.items():
            # print(key, val)
            line = line.replace(key, val)

        print(line)

if __name__ == '__main__':
    gen_table()
    work()
    # test()