import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

#1.课程名称
text = open('title.txt','r',encoding='utf-8').read()
#2.中文分词
cut_text = jieba.cut(text)
#3.空格切分
result = " ".join(cut_text)
# print(result)
# 4.生成词云l
wc = WordCloud(
    font_path='msyhbd.ttc',     #字体文件
    background_color='white',   #背景颜色
    width=1000,
    height=600,
    max_font_size=100,            #字体大小
    min_font_size=20,
    mask=plt.imread('python.jpg'),  #背景图片
    max_words=1000
)
wc.generate(result)
wc.to_file('result.png')    #图片保存

#5.显示图片
plt.figure('title')   #图片显示的名字
plt.imshow(wc)
plt.axis('off')        #关闭坐标
plt.show()