print('这里将两个4*4的矩阵进行加、减或乘的运算。')
a1=[]
a2=[]
a3=[]
a4=[]
b1=[]
b2=[]
b3=[]
b4=[]
c1=[]
c2=[]
c3=[]
c4=[]

a=[a1,a2,a3,a4]
b=[b1,b2,b3,b4]
c=[c1,c2,c3,c4]

i=0#行
j=0#列
while i<4:
    while j<4:
        print('请输入a矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        a[i].append(num)
        j=j+1
    j=0
    i=i+1
#a矩阵输入完毕，下面是b矩阵
i=0
j=0
while i<4:
    while j<4:
        print('请输入b矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        b[i].append(num)
        j=j+1
    j=0
    i=i+1

print('请问您要进行加法，减法还是乘法？加法请输入1，减法请输入2，乘法请输入3')
deci=int(input())

if deci==1:
    i=0
    j=0
    while i<4:
        while j<4:
            num=a[i][j]+b[i][j]
            c[i].append(num)
            j=j+1
        j=0
        i=i+1
    print('结果是',c)
        
if deci==2:
    i=0
    j=0
    while i<4:
        while j<4:
            num=a[i][j]-b[i][j]
            c[i].append(num)
            j=j+1
        j=0
        i=i+1
    print('结果是',c)
        
if deci==3:
    i=0#a中第几行
    j=0#b中第几列
    k=0#跑动数
    num=0
    while i<4:
        while j<4:
            while k<4:
                num1=a[i][k]*b[k][j]
                num=num+num1
                j=j+1
            c[i].append(num)
            j=j+1
        j=0
        i=i+1
    print('结果是',c)
