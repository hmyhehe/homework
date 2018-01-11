import gensim
import jieba
import numpy as np
import scipy as sp
import codecs
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_yahei_consolas = FontProperties(fname="C://Windows//Fonts//simsun.ttc")

with codecs.open('Name.txt', encoding="utf8") as f:
    # 去掉结尾的换行符
    data = [line.strip() for line in f]

novels = data[::2]
names = data[1::2]

novel_names = {k: v.split() for k, v in zip(novels, names)}

with codecs.open("斗气.txt", encoding="utf8") as f:
    kungfu_names = [line.strip() for line in f]
with codecs.open("地域.txt", encoding="utf8") as f:
    bang_names = [line.strip() for line in f]

for name in kungfu_names:
    jieba.add_word(name)

for name in bang_names:
    jieba.add_word(name)

novels=["斗破苍穹",
        "大主宰" ]
sentences = []

for novel in novels:
    print ("处理：{}".format(novel))
    with codecs.open('{}.txt'.format(novel), encoding="utf8") as f:
        sentences += [list(jieba.cut(line.strip())) for line in f]

model = gensim.models.Word2Vec(sentences,
                               size=100,
                               window=5,
                               min_count=5,
                               workers=4)
#for k, s in model.most_similar(positive=["牧尘"]):
    #print (k,s)
all_names = np.array(list(filter(lambda c: c in model, novel_names["\ufeff斗破苍穹"])))
word_vectors = np.array(list(map(lambda c: model[c], all_names)))
import scipy.cluster.hierarchy as sch

Y = sch.linkage(word_vectors, method="ward")

_, ax = plt.subplots(figsize=(10, 40))

Z = sch.dendrogram(Y, orientation='right')
idx = Z['leaves']

ax.set_xticks([])
ax.set_yticklabels(all_names[idx],
                  fontproperties=font_yahei_consolas)
ax.set_frame_on(False)

plt.show()

#designed by pwy