a=float(input('请输入工资:'))
b=a-4500
if b<=0:
    c=0
else:
    if b<=1500:
        c=b*0.03
    else:
        if b<=4500:
            c=b*0.1-105
        else:
            if b<=9000:
                c=b*0.2-555
            else:
                if b<=35000:
                    c=b*0.25-1005
                else:
                    if b<=55000:
                        c=b*0.3-2755
                    else:
                        if b<=80000:
                            c=b*0.35-5505
                        else:
                            c=b*0.45-13505
print('应交个人所得税:',c)
