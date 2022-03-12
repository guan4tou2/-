import re,sys

classtime = ['', '', '第一節<br>8:10~9:00', ' 第二節<br>9:10~10:00', ' 第三節<br>10:10~11:00', ' 第四節<br>11:10~12:00', '中午',
             ' 第五節<br>13:20~14:10', ' 第六節<br>14:20~15:10', ' 第七節<br>15:20~16:10', ' 第八節<br>16:20~17:10', ' 第九節<br>17:20~18:10']
week = ['一', '二', '三', '四', '五']
classlist = []
color = ['#bda642', '#4542f5', '#ff00ff']  # '必修' '選修' '通識'
filedata=""

regex = r"\d+\s+\d{4}\s+\w*\s(\D*)\n(\w{2})\s+\d\.0\s+\d\s+(\w{3,})\s+(\w{3}\d{4})\s+\(\S*\s+\)\s+(.*)"

if len(sys.argv) == 2:
    fileName = sys.argv[1]
    if not bool(re.search(r'\w*.txt', fileName)):
        print("副檔名須為txt")
        sys.exit()
    for i in range(len(classtime)):
        classlist.append([])
        for j in range(6):
            classlist[i].append([])
            if i <= len(classtime):
                classlist[i][0] = classtime[i]
    for i in range(6):
        if i > 0:
            classlist[0][i] = week[i-1]
        classlist[1][i] = ':------------:'

    with open(fileName, 'r', encoding='utf-8') as f:
        filedata=f.read()

    fileData=re.findall(regex, filedata)
    
    for data in fileData:
        classname, teacher, classnum = data[0], data[2], data[3]
        types = 0 if data[1]=='必修' else 1 if data[1]=='選修' else 2
        day_time = re.findall(r'\w/\d', data[4])
        for j in day_time:
            day, t = j.split('/')
            t = int(t)
            if t > 4:
                t += 1
            classlist[t+1][week.index(
                day)+1] = f'<font color={color[types]}>{classname}<br>{teacher}<br>{classnum}</font>'
            
    with open('out.md', 'w', encoding='utf-8') as f:
        for i in classlist:
            f.write('|')
            for j in i:
                if j != []:
                    f.write(j+"|")
                else:
                    f.write(''+"|")
            f.write('\n')
    print("已完成，請查看out.md")
else:
    print("請輸入檔名")
