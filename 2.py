a=input('请输入字符：')
j=0
while(j<len(a)):
    if not (a[j].isalpha()):
        print('输入有误！请重新输入！')
        j=0
        a=input()
    else:
        j=j+1
        
list =[]
for i in range(len(a)):
    num=ord(a[i])+3
    if num<=122:
        new_num=num
    else:
        new_num=num-26
    new_str = chr(new_num)
    list.append(new_str)
    b = ''.join(list)
print('密码为：',b)
