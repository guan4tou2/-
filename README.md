# NFU-school-timetable-generator
NFU課表生成器

1. 將main.py下載
2. 將nfu ecare內的選課結果表格複製後儲存成txt檔案
3. 檔案存放於同一目錄底下後，`python main.py file.txt`
4. 將輸出檔案out.md以markdown格式打開
5. 即可將課表截圖保存

表格內容
```
順序
NO	當期課號
Course Code	修課班級
Class	科目名稱
Subject Name	選別
Selection	學分
Credit	時數
Hour	授課老師
Teacher	教室
Classroom	上課星期/節次(*表衝堂)
ClassWeek/Period(*Indicating Class Conflict)
....
.....
....
```
