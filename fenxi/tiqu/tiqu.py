from __future__ import unicode_literals
import numpy as np
import scipy as sp
import codecs
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_yahei_consolas = FontProperties(fname="C://Windows//Fonts//simsun.ttc")

import codecs
#for name in novel_names['\ufeff斗破苍穹'][:10]:

with codecs.open('设定三灵阵.txt', encoding="utf8") as f:
    # 去掉结尾的换行符
    data = [line.strip() for line in f]

novels = data[::2]
names = data[1::2]

novel_names = {k: v.split() for k, v in zip(novels, names)}




def find_main_charecters(novel, num=10):
    with codecs.open('大主宰.txt'.format(novel), encoding="utf8") as f:
        data = f.read()
    count = []
    for name in novel_names[novel]:
        count.append([name, data.count(name)])
    count.sort(key=lambda x: x[1])
    _, ax = plt.subplots()

    numbers = [x[1] for x in count[-num:]]
    names = [x[0] for x in count[-num:]]
    ax.barh(range(num), numbers, color='red', align='center')
    ax.set_title(novel,
                 fontsize=14,
                 fontproperties=font_yahei_consolas)
    ax.set_yticks(range(num))
    ax.set_yticklabels(names,
                       fontsize=14,
                       fontproperties=font_yahei_consolas)
    plt.show()

find_main_charecters("\ufeff大主宰")

#designed by pwy