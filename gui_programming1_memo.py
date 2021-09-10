from tkinter import *
import os
from io import open

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+300")

# 파일 이름
File_name = "mynote.txt"

# 함수 구현
def open_file():
    if os.path.isfile(File_name):
        with open(File_name,"r") as f:
            txt.delete("1.0",END)
            txt.insert(END,f.read())

def save_file():
    with open(File_name,"w") as f:
        f.write(txt.get("1.0" , END))

# 파일 메뉴 구현

menu = Menu(root)

menu_file = Menu(menu ,tearoff=0)
menu_file.add_command(label="열기" , command=open_file)
menu_file.add_command(label="저장" , command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기" , command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식 ,보기 , 도움말
menu.add_cascade(label="편집")
menu.add_cascade(label="편집")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

#스크롤 바 생성
scl = Scrollbar(root)
scl.pack(side="right" , fill="y")

# 텍스트 생성

txt = Text(root , yscrollcommand=scl.set)
txt.pack(side="left",fill="both" , expand=TRUE)

# 스크롤로 텍스트 감싸주기
scl.config(command=txt.yview)

root.mainloop()