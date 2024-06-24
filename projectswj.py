import tkinter as tk
import tkinter.font
window=tkinter.Tk()
window.title("서울 아파트 가격 구하기")
window.geometry("1000x1000+100+100")

def jrg_click():
    label2.config(text="선택한 지역:종로구")
def jg_click():
    label2.config(text="선택한 지역:중구")
def ysg_click():
    label2.config(text="선택한 지역:용산구")
def sdg_click():
    label2.config(text="선택한 지역:성동구")
def ddmg_click():
    label2.config(text="선택한 지역:동대문구")
def jlg_click():
    label2.config(text="선택한 지역:중랑구")
def sbg_click():
    label2.config(text="선택한 지역:성북구")
def gbg_click():
    label2.config(text="선택한 지역:강북구")
def dbg_click():
    label2.config(text="선택한 지역:도봉구")
def nwg_click():
    label2.config(text="선택한 지역:노원구")
def epg_click():
    label2.config(text="선택한 지역:은평구")
def sdmg_click():
    label2.config(text="선택한 지역:서대문구")
def mpg_click():
    label2.config(text="선택한 지역:마포구")
def ycg_click():
    label2.config(text="선택한 지역:양천구")
def gsg_click():
    label2.config(text="선택한 지역:강서구")
def grg_click():
    label2.config(text="선택한 지역:구로구")
def gcg_click():
    label2.config(text="선택한 지역:금천구")
def ydpg_click():
    label2.config(text="선택한 지역:영등포구")
def djg_click():
    label2.config(text="선택한 지역:동작구")
def gag_click():
    label2.config(text="선택한 지역:관악구")
def scg_click():
    label2.config(text="선택한 지역:서초구")
def gng_click():
    label2.config(text="선택한 지역:강남구")
def spg_click():
    label2.config(text="선택한 지역:송파구")
def gdg_click():
    label2.config(text="선택한 지역:강동구")
def gjg_click():
    label2.config(text="선택한 지역:광진구")

title_font= tkinter.font.Font(family='맑은 고딕',size=20)
title=tkinter.Label(window,text='서울 아파트 가격 구하기',font=title_font)
title.place(x=340,y=0)

label2=tkinter.Label(window,text="선택한 지역:")


label3=tkinter.Label(window,text="원하는 평수를 입력하세요.",bg="white")
label3.place(x=450 ,y=140)

ent=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=8)
ent.place(x=600,y=130)

ent1=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=25)
ent1.place(x=500,y=200)

ent2=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=8)
ent2.place(x=600,y=130)



label4=tkinter.Label(window,text="가격 :")
label4.place(x=450,y=210)


jrg=tkinter.Button(window,width=9,height=2,text="종로구",overrelief="solid", command=jrg_click)
jrg.place(x=30,y=50)
jrg_price=int(2917)

jg=tkinter.Button(window,width=9,height=2,text="중구",overrelief="solid",command=jg_click)
jg.place(x=110,y=50)
jg_price=int(4561)

ysg=tkinter.Button(window,width=9,height=2,text="용산구",overrelief="solid",command=ysg_click)
ysg.place(x=190,y=50)
ysg_price=int(6006)

sdg=tkinter.Button(window,width=9,height=2,text="성동구",overrelief="solid",command=sdg_click)
sdg.place(x=270,y=50)
sdg_price=int(5356)

ddmg=tkinter.Button(window,width=9,height=2,text="동대문구",overrelief="solid",command=ddmg_click)
ddmg.place(x=350,y=50)
ddmg_price=int(3871)

jlg=tkinter.Button(window,width=9,height=2,text="중랑구",overrelief="solid",command=jlg_click)
jlg.place(x=30,y=100)
jlg_price=int(3155)

sbg=tkinter.Button(window,width=9,height=2,text="성북구",overrelief="solid",command=sbg_click)
sbg.place(x=110,y=100)
sbg_price=int(3716)

gbg=tkinter.Button(window,width=9,height=2,text="강북구",overrelief="solid",command=gbg_click)
gbg.place(x=190,y=100)
gbg_price=int(3158)

dbg=tkinter.Button(window,width=9,height=2,text="도봉구",overrelief="solid",command=dbg_click)
dbg.place(x=270,y=100)
dbg_price=int(3270)

nwg=tkinter.Button(window,width=9,height=2,text="노원구",overrelief="solid",command=nwg_click)
nwg.place(x=350,y=100)
nwg_price=int(3722)

epg=tkinter.Button(window,width=9,height=2,text="은평구",overrelief="solid",command=epg_click)
epg.place(x=30,y=150)
epg_price=int(3254)

sdmg=tkinter.Button(window,width=9,height=2,text="서대문구",overrelief="solid",command=sdmg_click)
sdmg.place(x=110,y=150)
sdmg_price=int(3759)

mpg=tkinter.Button(window,width=9,height=2,text="마포구",overrelief="solid",command=mpg_click)
mpg.place(x=190,y=150)
mpg_price=int(5079)

ycg=tkinter.Button(window,width=9,height=2,text="양천구",overrelief="solid",command=ycg_click)
ycg.place(x=270,y=150)
ycg_price=int(4963)

gsg=tkinter.Button(window,width=9,height=2,text="강서구",overrelief="solid",command=gsg_click)
gsg.place(x=350,y=150)
gsg_price=int(4145)

grg=tkinter.Button(window,width=9,height=2,text="구로구",overrelief="solid",command=grg_click)
grg.place(x=30,y=200)
grg_price=int(3594)

gcg=tkinter.Button(window,width=9,height=2,text="금천구",overrelief="solid",command=gcg_click)
gcg.place(x=110,y=200)
gcg_price=int(2917)

ydpg=tkinter.Button(window,width=9,height=2,text="영등포구",overrelief="solid",command=ydpg_click)
ydpg.place(x=190,y=200)
ydpg_price=int(4871)

djg=tkinter.Button(window,width=9,height=2,text="동작구",overrelief="solid",command=djg_click)
djg.place(x=270,y=200)
djg_price=int(4811)

gag=tkinter.Button(window,width=9,height=2,text="관악구",overrelief="solid",command=gag_click)
gag.place(x=350,y=200)
gag_price=int(3584)

scg=tkinter.Button(window,width=9,height=2,text="서초구",overrelief="solid",command=scg_click)
scg.place(x=30,y=250)
scg_price=int(7772)

gng=tkinter.Button(window,width=9,height=2,text="강남구",overrelief="solid",command=gng_click)
gng.place(x=110,y=250)
gng_price=int(8432)

spg=tkinter.Button(window,width=9,height=2,text="송파구",overrelief="solid",command=spg_click)
spg.place(x=190,y=250)
spg_price=int(6161)

gdg=tkinter.Button(window,width=9,height=2,text="강동구",overrelief="solid",command=gdg_click)
gdg.place(x=270,y=250)
gdg_price=int(4686)

gjg=tkinter.Button(window,width=9,height=2,text="광진구",overrelief="solid",command=gjg_click)
gjg.place(x=350,y=250)
gjg_price=int(5095)






image1=tkinter.PhotoImage(file='seoul.png')
label1=tkinter.Label(window, image=image1)
label1.place(x=25,y=300)
label2.place(x=580,y=90)
window.mainloop()
