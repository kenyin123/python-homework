print('这里将两个4*4的矩阵进行加、减、乘的运算。')
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

i=0#行
j=0#列
while i==0:
    while j<4:
        print('请输入a矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        a1.append(num)
        j=j+1
    i=i+1
while i==1:
    j=0
    while j<4:
        print('请输入a矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        a2.append(num)
        j=j+1
    i=i+1
while i==2:
    j=0
    while j<4:
        print('请输入a矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        a3.append(num)
        j=j+1
    i=i+1
while i==3:
    j=0
    while j<4:
        print('请输入a矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        a4.append(num)
        j=j+1
    i=i+1

#a矩阵输入完毕，下面是b矩阵
i=0
j=0
while i==0:
    while j<4:
        print('请输入b矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        b1.append(num)
        j=j+1
    i=i+1
while i==1:
    j=0
    while j<4:
        print('请输入b矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        b2.append(num)
        j=j+1
    i=i+1
while i==2:
    j=0
    while j<4:
        print('请输入b矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        b3.append(num)
        j=j+1
    i=i+1
while i==3:
    j=0
    while j<4:
        print('请输入b矩阵中第',i+1,'行，第',j+1,'列的数')
        num=float(input())
        b4.append(num)
        j=j+1
    i=i+1
a=[a1,a2,a3,a4]
b=[b1,b2,b3,b4]

#加法
i=0
j=0
while i==0:
    while j<4:
        num=a[i][j]+b[i]+b[j]
        c1.append(num)
        j=j+1
    i=i+1
while i==1:
    j=0
    while j<4:
        num=a[i][j]+b[i]+b[j]
        c2.append(num)
        j=j+1
    i=i+1
while i==2:
    j=0
    while j<4:
        num=a[i][j]+b[i]+b[j]
        c3.append(num)
        j=j+1
    i=i+1
while i==3:
    j=0
    while j<4:
        num=a[i][j]+b[i]+b[j]
        c4.append(num)
        j=j+1
    i=i+1
