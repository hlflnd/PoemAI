#coding=gbk
import random
import time
from Poem import Poem

#---------------------------------------------------------
template = "���ڵ�����Ϸź�.txt"     #ģ�����ƣ�����չ����
num = 1    #��ʫ����
save = True    #�Ƿ񱣴�
show = True   #�Ƿ����
#---------------------------------------------------------

with open(f"./дʫAI��ģ��s/{template}",'r') as f:
    p = f.read()

with open("./дʫAI�δʻ���.txt",'r') as f:
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
        f = open(f"./дʫAI�δ���s/{i+1}-{new_poem_title}.txt",'w')
        f.write(new_poem)
        f.close()