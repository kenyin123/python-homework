d = 0
e = 0
f = 0

a = float(input ('请输入第一个值 '))
b = float(input ('请输入第二个值 '))
c = float(input ('请输入第三个值 '))

if a-b<=0 and a-c<=0:
    f=a
    if b-c<=0:
        e=b
        d=c
    else:
        e=c
        d=b
else:
    if b-c<=0:
        f=b
        if a-c<=0:
            e=a
            d=c
        else:
            e=c
            d=a
    else:
        f=c
        if a-b<=0:
            e=a
            d=b
        else:
            e=b
            d=a
print('从大到小为',d,e,f)
        
   
