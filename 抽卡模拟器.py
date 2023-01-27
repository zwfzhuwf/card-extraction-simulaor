
from random import *
from plotly import *

#基础功能



shenyu=0

n=0
nn=[]
m=0
mm=[]

#次数
ti=0
tis=0
#概率
gailv=6
#判断保底类型，1为小，2为大
bad=1
#金光次数
chuj=0
wai=0
buwai=0
#出金时刻
cchu=[]
buwwai=[]

#方式选择
xuanz=input("选择抽卡方式('1'为原石,'2'为纠缠):")
if xuanz=='1':
    yuans=input('请输入抽卡花费:')
    try:
        int(yuans)
    except ValueError:
        print('tm输入正常数字')
    else:
        if int(yuans)<160:
            print('没钱还想抽卡？')
        else:
            cishu=int(int(yuans)/160)
            a=cishu
            shenyu=int(yuans)%160
elif xuanz=='2':
    jiuc=input('输入纠缠数量:')
    try:
        int(jiuc)
    except ValueError:
        print('tm输入正常数字')
    else:
        if int(jiuc)<1:
            print('你想白嫖？')
        else:
            cishu=int(jiuc)
            a=cishu
else:
    print('你干嘛，哎呦！')

#一个保底
while cishu>0:
    jing=randint(gailv,1000)
    print(f'还剩',cishu,'次')
    cishu=cishu-1
    ti=ti+1
    tis=tis+1
    if jing<=gailv:
        if bad==1:
            pan=randint(1,2)
            if pan==1:
                chuj=chuj+1
                wai=wai+1
                n=n+1
                nn.append(n)
                cchu.append(ti)
                bad=2
                ti=0
                gailv=6
            else:
                chuj=chuj+1
                buwai=buwai+1
                m=m+1
                mm.append(m)
                cchu.append(ti)
                buwwai.append(tis)
                ti=0
                tis=0
                gailv=6
        else:
            chuj = chuj + 1
            buwai = buwai + 1
            m = m + 1
            mm.append(m)
            cchu.append(ti)
            buwwai.append(tis)
            bad=1
            ti=0
            tis=0
            gailv=6
    if ti>=73:
        gailv=gailv+60
        if ti==89:
            gailv=1000

print('\n \n \n \n \n')

print(f'共抽取',a,'次')
if xuanz==1:
    print(f'剩余',shenyu,'原石')
print(f'出金',chuj,'次')
print(f'歪',wai,'次')
print(f'不歪',buwai,'次')
print(f'平均',int(a/chuj),'抽出金')
print(f'平均',int(a/buwai),'up')

#分析模块





