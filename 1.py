maxlist=[]
minlist=[]
i=0

#构造列表
while i<7:
    print('这是9月',i+20,'号')
    a=int(input('请输入当天最高气温'))
    b=int(input('请输入当天最低气温'))
    maxlist.append(a)
    minlist.append(b)
    i=i+1

#取最值
maxtem=max(maxlist)
mintem=min(minlist)
maxdate=maxlist.index(maxtem)
mindate=minlist.index(mintem)

print('这一周中第',maxdate+1,'天最热','最高温度为',maxtem,'度\n')
print('这一周中第',mindate+1,'天最冷','最低温度为',mintem,'度\n')

j=0
k=0#连续天数
while j<7:
    c=(maxlist[j]+minlist[j])/2
    j=j+1
    if c<20:
        k=k+1
        if k==5:
            print('已经入秋')
    else:
        k=0

if k<5:
    print('还没入秋')

