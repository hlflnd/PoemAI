#coding=gbk
import random
import time
from Poem import Poem

#---------------------------------------------------------
template = "立在地球边上放号.txt"     #模板名称（带拓展名）
num = 1    #作诗数量
save = True    #是否保存
show = True   #是否输出
#---------------------------------------------------------

with open(f"./写诗AIの模板s/{template}",'r') as f:
    p = f.read()

with open("./写诗AIの词汇量.txt",'r') as f:
    words = f.read().split();

def GetWord():
    return random.choice(words)

poem = Poem(p)

for i in range(num):
    new_poem = eval(poem.Struct())
    new_poem_title = new_poem.split("\n")[0]
    if show:
        print(new_poem)
        print()
        time.sleep(0.1)
    if save:
        f = open(f"./写诗AIの大作s/{i+1}-{new_poem_title}.txt",'w')
        f.write(new_poem)
        f.close()