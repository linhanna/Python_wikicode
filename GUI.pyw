from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Main import Work, addWork, showMark, showToDo, showWho, index_day, sortTime, timeTable
import Main
from datetime import *


def runGUI():
    def showTimeTable():
        def data():
            FONT_X = ('Arial', 15)
            row_X = 0
            for day in range(Main.DAY_OF_WEEK):
                if day == Main.MON: 
                    Label(frame, text = "Monday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.TUE: 
                    Label(frame, text = "Tueday:",font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.WED:
                    Label(frame, text = "Wednesday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.THU: 
                    Label(frame, text = "Thursday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.FRI: 
                    Label(frame, text = "Friday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.SAT: 
                    Label(frame, text = "Saturday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                elif day == Main.SUN: 
                    Label(frame, text = "Sunday:", font = FONT_X).grid(row = row_X, column = 0, sticky = 'w')
                    row_X += 1
                
                for who in range(len(Main.mark[day])):
                    if Main.mark[day][who] : person = 'Mother'
                    else: person = 'Father'
                    Label(frame, text = Main.toDoList[day][who].toString() + " -> " + person, font = FONT_X).grid(row = row_X, column = 1, sticky = 'w')
                    row_X += 1

        def myfunction(event):
            canvas.configure(scrollregion = canvas.bbox("all"), width = 700, height = 500)
        #--------------------------------------------------------------------------------
        timeTable_window = Tk()
        timeTable_window.title('Time Table')
        timeTable_window.geometry('700x500')


        canvas = Canvas(timeTable_window)
        frame = Frame(canvas)
        myscrollbar=Scrollbar(timeTable_window, orient = "vertical", command = canvas.yview)
        canvas.configure(yscrollcommand = myscrollbar.set)

        myscrollbar.pack(side = "right", fill = "y")
        canvas.pack(side = "left")
        canvas.create_window((0,0),window = frame, anchor = 'nw')
        frame.bind("<Configure>", myfunction)
        data()
        timeTable_window.mainloop()


    def enter():
        day_list = days_entry.get().split(',')
        work = work_entry.get()
        time_list = time_entry.get().split(':')
        hour = int(time_list[0])
        min = int(time_list[1])
        Work(work, time(hour, min)).show()
        for day in day_list:
            addWork(Main.toDoList, index_day(day), Work(work, time(hour, min)))
    
    def divide():
        sortTime(Main.toDoList)
        Main.mark = timeTable(Main.toDoList)
        showMark(Main.mark)
        showWho(Main.toDoList, Main.mark)
        showTimeTable()

    def delete():
        Main.toDoList = [[],[],[],[],[],[],[]]
        Main.mark = [[],[],[],[],[],[],[]]
        showToDo(Main.toDoList)
        print(Main.mark)
        print('Deleted successfully!')
    root = Tk()
    root.title("Time Table")

    FONT = ('Arial', 20)
    BG_COLOR = '#219ebc'

    root.config(bg = BG_COLOR)

    label_TimeTable = Label(root, text = "Time Table", font = FONT )
    label_TimeTable.grid(row = 0, column = 2, padx = 10, pady = 10)
    label_day = Label(root, text = "Day", font = FONT, background = '#219ebc')
    label_day.grid(row = 1, column = 0, padx = 10, pady = 10)
    label_work = Label(root, text = "Work", font = FONT, background = '#219ebc')
    label_work.grid(row = 1, column = 2, padx = 10, pady = 10)
    label_time = Label(root, text = "Time", font = FONT, background = '#219ebc')
    label_time.grid(row = 1, column = 5, padx = 10, pady = 10)

    days_entry = Entry(root, font = FONT, width = 15)
    days_entry.grid(row=2, column=0, padx=10, pady=10)
    work_entry = Entry(root, font = FONT, width = 15)
    work_entry.grid(row=2, column=2, padx=10, pady=10)
    time_entry = Entry(root, font = FONT, width = 15)
    time_entry.grid(row=2, column=5, padx=10, pady=10)


    enter_button = Button(root, 
        text='Enter', 
        bg='#e9c46a',
        font = ('Arial', 15),
        command = enter
    )
    enter_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    divide_button = Button(root, 
        text='Devide', 
        bg='#e9c46a',
        font = ('Arial', 15),
        width = 20,
        command = divide
    )
    divide_button.grid(row=4, column=0, padx=10, pady=10)

    delete_button = Button(root, 
        text='Delete', 
        bg='#e9c46a',
        font = ('Arial', 15),
        width = 20,
        command = delete
    )
    delete_button.grid(row=4, column=5, padx=10, pady=10)

    root.mainloop()

def notice(mess):
    top = Tk() 
    top.geometry("100x100")      
    messagebox.showinfo("Reminder", mess)  
    top.destroy()