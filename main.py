import re

classtime=['', '', '第一節<br>8:10~9:00', ' 第二節<br>9:10~10:00', ' 第三節<br>10:10~11:00', ' 第四節<br>11:10~12:00', '中午<br>12:00~13:20', ' 第五節<br>13:20~14:10', ' 第六節<br>14:20~15:10', ' 第七節<br>15:20~16:10', ' 第八節<br>16:20~17:10', ' 第九節<br>17:20~18:10']
week=['一','二','三','四','五']
classlist=[]

for i in range(len(classtime)):
    classlist.append([])
    for j in range(6):
        classlist[i].append([])
        if i<=len(classtime):
            classlist[i][0]=classtime[i]
for i in range(6):
    if i>0:
        classlist[0][i]=week[i-1]
    classlist[1][i]=':------------:'

with open('a.txt','r',encoding='utf-8') as f:
    f.readline()
    for i in f:
        data=i.split()
        classname,teacher,classnum=data[3],data[7],data[8]
        day_time=re.findall(r'\w/\d',i)
        for j in day_time:
            day,t=j.split('/')
            t=int(t)
            if t>4:t+=1
            match day:
                case '一':
                    classlist[t+1][1]=f'{classname}<br>{teacher}<br>{classnum}'
                case '二':
                    classlist[t+1][2]=f'{classname}<br>{teacher}<br>{classnum}'
                case '三':
                    classlist[t+1][3]=f'{classname}<br>{teacher}<br>{classnum}'
                case '四':
                    classlist[t+1][4]=f'{classname}<br>{teacher}<br>{classnum}'
                case '五':
                    classlist[t+1][5]=f'{classname}<br>{teacher}<br>{classnum}'

with open('out.md','w',encoding='utf-8') as f:
    for i in classlist:
        f.write('|')
        for j in i:
            if j!=[]:f.write(j+"|")
            else:f.write(''+"|")
        f.write('\n')
