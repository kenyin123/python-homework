chi=[]
math=[]
i=0
while i<10:#(1)
    print('请输入第',i+1,'名同学的语文成绩')
    a=float(input())
    chi.append(a)
    print('请输入第',i+1,'名同学的数学成绩')
    b=float(input())
    math.append(b)
    i=i+1

sum1=sum(chi)#(2)
sum2=sum(math)
ave1=sum1/10
ave2=sum2/10
print('这10名学生语文平均分为',ave1,'数学平均分为',ave2)

j=0#(3)
grade=[]
while j<10:
    grade.append(chi[j]+math[j])
    j=j+1
maxgrade=max(grade)
mingrade=min(grade)
maxstu=grade.index(maxgrade)+1
minstu=grade.index(mingrade)+1
print('最高分的学生学号为',maxstu,'，其成绩为',maxgrade)
print('最低分的学生学号为',minstu,'，其成绩为',mingrade)

k=0#(4)
while k<10:
    if (chi[k])<60 and (math[k])<60:
        print('学号为',k+1,'的同学两门课都不及格，他的各科成绩为：语文',chi[k],'数学',math[k])
    k=k+1

l=0#(5)
while l<10:
    if grade[l]>180:
        print('学号为',l+1,'的同学两门课平均分超过90，他的各科成绩为：语文',chi[l],'数学',math[l])
    l=l+1
