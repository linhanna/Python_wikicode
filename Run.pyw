from datetime import time
from time import sleep
from GUI import *
import Main
from tkinter import messagebox

runGUI()

while (True):
    hour = datetime.now().hour
    min = datetime.now().minute
    day = datetime.now().weekday()
    if  len(Main.toDoList[day]) == 0:
        sleep((24 - hour)*60*60 +(60 - min)*60)
    else :
        works_list = Main.toDoList[day]
        for i in range(len(works_list)):
            work = works_list[i]
            if time(hour, min) > work.getTime():
                continue
            else:
                t = datetime.now().time()
                while not(t.hour == work.getTime().hour and t.minute == work.getTime().minute):
                    sleep(30)
                    t = datetime.now().time()
                mess = work.toString() + (' -> Mother' if Main.mark[day][i] else ' -> Father')
                notice(mess)
            
