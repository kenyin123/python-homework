n=int(input('请输入一个正整数'))
a=1
b=1
c=0
i=0
print(a,'\n',b)
while i<n-2:
    c=b
    b=a+b
    a=c
    print(b)
    i=i+1
    
