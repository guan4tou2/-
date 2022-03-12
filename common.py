import re,sys

grades = ['大三', '大四', '碩一']  # '大一', '大二',, '碩二'
color = ['#bda642', '#4542f5', '#ff00ff']  # '大三' '大四' '碩一'

filedata=[]

regex = r"<font color=#\w*>\D*<br>\w*<br>\w{3}\d{4}</font>"

if len(sys.argv) >= 2:
    for nowindex,fileName in enumerate(sys.argv[1:]):
        if not bool(re.search(r'\w*.md', fileName)):
            print("副檔名須為md")
            sys.exit()
        
        with open(fileName, 'r', encoding='utf-8') as f:
            filedata.append(f.read())
            if bool(re.search(r'^<.*</font>', filedata[nowindex])):
                filedata[nowindex] = re.sub(r'^<.*>', '', filedata[nowindex])
        if not bool(re.search(r'out.md', fileName)):
            studentName, grade = re.search(
                r'(\w+)_(\w{2})\.md', fileName).groups()
            filedata[nowindex] = re.sub(regex, f'<font color={color[grades.index(grade)]}>{studentName}<br></font>', filedata[nowindex])

        filedata[nowindex] = re.split(r'\|', filedata[nowindex])
        
    Data=filedata[0]
    for i in filedata[1:]:
        for j in range(len(Data)):
            if not bool(re.search(i[j], Data[j])):
                Data[j] += i[j]

    with open('out.md', 'w', encoding='utf-8') as f:
        for i in grades:
            f.write(f'<font color={color[grades.index(i)]}>{i}</font> ')
        f.write('\n')
        for i in Data[:-1]:
            if i != '':
                f.write(i+"|")
            else:
                f.write(''+"|")

    print("已完成，請查看out.md")
else:
    print("請輸入檔名")
