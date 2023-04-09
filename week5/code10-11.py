from tkinter import *

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "marshmallow.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 4):
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i], height = 500, width = 500)
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 2):
    for k in range(0, 2):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 500
    xPos = 0
    yPos += 500

window.mainloop()