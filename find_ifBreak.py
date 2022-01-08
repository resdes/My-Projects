from datetime import datetime
from tkinter import *
from time import sleep
root=Tk()
breaksSE=[[540,555],[595,605],[695,705],[745,785],[825,835],[875,890],[930,940]]#The break's starts and ends in a list within in a list
breaks=[540, 595, 695, 745, 825, 875, 930,1299]#List of ust the break's starts
breaksE=[555, 605, 705, 785, 835, 890, 940,1390]
def func():
    now = int(datetime.now().strftime("%H"))*60+int(datetime.now().strftime("%M"))
    for i in range (len(breaksSE)-1):
        if breaksSE[i][0]<now and breaksSE[i][1]>now:
            isBreak=True
        else:
            isBreak=False
    if isBreak==False:
        reak=min((i for i in breaks if i > now),default="EMPTY")
        if reak=="EMPTY":
            dreak=min(i for i in breaksE if i > now)
            dFark=dreak-now
            return("Derse "+str(dFark)+" dakika var.")
        else:
            fark=reak-now
            return("Teneffüse "+str(fark)+" dakika var")
def func2():
    v.set(func())
v = StringVar()
v.set("default")
lbl=Label(root, textvariable=v, font=("Arial", 26))
lbl.place(x=0, y=80)
photo = PhotoImage(file = "bell.png")
root.iconphoto(False, photo)
root.title('BİLSEM Teneffüs')
root.geometry("300x200+20+20")
func2()
root.mainloop()





