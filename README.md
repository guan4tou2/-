# school-timetable-generator
課表生成器

! python環境須為python10

1. 將main.py下載
2. 將nfu ecare內的選課結果複製後以下面格式儲存成txt檔案
```
順序	當期課號	修課班級	科目名稱	選別	學分	時數	授課老師	教室	上課星期/節次(*表衝堂)
1	0667	四技三進階英文	進階英文(二) 資工甲班	必修	2.0	2	顏廷芳	AIA0101 (電腦語言教室_資訊大樓 )	四/5 四/6
2 .........
3 ...
.
.
```
3. 檔案存放於同一目錄底下後，`python main.py file.txt`
4. 將輸出檔案out.md以markdown格式打開
5. 即可將課表截圖保存
