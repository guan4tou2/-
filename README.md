# NFU課表生成器

1. 將main.py下載
2. 修改color內的hex色碼可更改課程種類的顏色
3. 將nfu ecare內的選課結果表格複製後儲存成txt檔案
4. 檔案存放於同一目錄底下後，`python main.py file.txt`
5. 將輸出檔案out.md以markdown格式打開
6. 即可將課表截圖保存

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

# NFU共同課表生成器
1. 將common.py下載
2. 修改color內的hex色碼可更改課程種類的顏色，可添加或刪減grades與color的內容
3. 將使用main.py做出的課表檔案改名為`姓名_年級.md`的格式，年級為大幾or碩幾
4. 檔案存放於同一目錄底下後，`python common.py 姓名_年級.md 姓名_年級.md`，輸入檔案可輸入多個
5. 若已有輸出檔案可改為`python common.py out.md 姓名_年級.md`
6. 將輸出檔案out.md以markdown格式打開
7. 即可將課表截圖保存
