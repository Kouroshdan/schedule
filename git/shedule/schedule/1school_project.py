# project

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

win = Tk()
win.title(' scheduler')
win.geometry('900x490')
win.attributes("-toolwindow", True)
#------------------------

#------------------------------

#------------------------

note_1 = ttk.Notebook(win)
note_1.pack()

fram_pan_add_lessons = Frame(win, width=800, height=600, bg='lightskyblue1')
frame_schedule = Frame(win, width=800, height=600, bg='lightsteelblue3')
note_1.add(fram_pan_add_lessons, text='add')
note_1.add(frame_schedule, text='schedule')

pan_add = PanedWindow(fram_pan_add_lessons, orient='horizontal')
pan_add.pack()
fram_pan_add_lessons = Frame(win, width=800, height=200, bg='lightskyblue1')
fram_pan_add_lessons_2 = Frame(win, width=800, height=400, bg='lightskyblue3')
pan_add.add(fram_pan_add_lessons)
pan_add.add(fram_pan_add_lessons_2)

#------------
# - ----------


def save():

    lesson_name = entry_lessons_name.get()
    teacher_name = entry_teacher_name.get()
    hardness = lessons_hardnes_combo.get()
    if teacher_name and lesson_name and hardness != '':
        try:
            f = open('school_lesson.csv', 'a')
            f.write(lesson_name + ',')
            f.write(teacher_name + ',')
            f.write(hardness)
            f.write('\n')
            f.close()
            messagebox.showinfo(title='Data Saved',
                                message='Data has been saved sucsesfuly')
            entry_lessons_name.delete(0, END)
            entry_teacher_name.delete(0, END)
            lessons_hardnes_combo.delete(0, END)

        except:
            messagebox.showerror(title='Error', message='there is an error')
    else:
        messagebox.showerror(title='enterys not filled',
                             message='please fill all enterys')


def save_2():
    sun = sunday.get()
    mon = monday.get()
    tue = tuesday.get()
    wed = wednesday.get()
    thu = thursday.get()
    fri = friday.get()
    sat = saturday.get()
    day = per_day_combo.get()

    if sun + mon + tue + wed + thu + fri + sat != 0:
        if day != '':
            yes_no = messagebox.askyesno(
                title='data will be deleted',
                message=
                'if you saved any data before it will be deleted if you accept click yes'
            )
            if yes_no:
                try:

                    with open('school_day.csv', 'w') as f:
                        f.write(str(sun + mon + tue + wed + thu + fri + sat))
                        f.write(',')
                        f.write(day)
                        f.write('\n')
                    with open('school_days.csv', 'w') as f:
                        if sun == 1:
                            f.write('sun')
                            f.write(',')
                        if mon == 1:
                            f.write('mon')
                            f.write(',')
                        if tue == 1:
                            f.write('tue')
                            f.write(',')
                        if wed == 1:
                            f.write('wed')
                            f.write(',')
                        if sun == 1:
                            f.write('thu')
                            f.write(',')
                        if fri == 1:
                            f.write('fri')
                            f.write(',')
                        if sat == 1:
                            f.write('sat')
                            f.write(',')

                    messagebox.showinfo(
                        title='data saved',
                        message='Data has been saved successfully')
                except:
                    messagebox.showerror(
                        title='Saving error',
                        message='There was an error while saving')
            else:
                messagebox.showerror(
                    title='yes to save',
                    message='In order to save you need to click yes')
        else:
            messagebox.showerror('Lessons per day',
                                 message='Enter how many lessons per day ')
    else:
        messagebox.showerror('One work day',
                             message='Enter at least one working day')


def b_import():
    lst = []
    button_import.grid_forget()
    with open('school_lesson.csv', 'r') as f:
        school = (f.readlines())

        for item in school:
            word = re.search(r"\w{1,},", item)
            if word:
                lst.append(word.group())
    label_lesson = Label(frame_1, text='\n'.join(lst), font=(2, ))
    label_lesson.grid(pady=20, padx=10)


lst_combo_r = []
lst_check = []
lst_check_1 = []
error = 0


def import_2():
    x = 0
    lst_day = []
    with open('school_days.csv', 'r') as f:
        for line in f:
            days = line.split(',')
            lst_day.append(days)
    for i in lst_day:
        for item in i:
            if item != '':
                label = Label(frame_2, text=item, font=(2, ))
                label.grid(pady=3)
                x += 1

    with open('school_day.csv', 'r') as f:
        num = f.read()
        button_make.grid_forget()
        lst = []

        for i in (num):
            if i != ',' and i != '' and i != '\n':
                lst.append(i)

    lst_lesson = []
    with open('school_lesson.csv') as f:

        lst_1 = int(lst[1])
        for line in f:
            days = line.split(',')
            lst_lesson.append(days)

    # button_import = Button(frame_2, text='check', font=4, command=def_1)
    # button_import.grid(column=3, row=9)

    if int(lst[0]) > 1 or int(lst[0]) == 1:

        if int(lst[1]) > 1 or int(lst[1]) == 1:

            check_1_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_1_1.grid(column=2, row=1, padx=10, pady=5)

    if int(lst[0]) > 1 or int(lst[0]) == 1:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_1_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_1_2.grid(column=3, row=1, padx=10, pady=5)

    if int(lst[0]) > 1 or int(lst[0]) == 1:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_1_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_1_3.grid(column=4, row=1, padx=10, pady=5)

    if int(lst[0]) > 1 or int(lst[0]) == 1:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_1_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_1_4.grid(column=5, row=1, padx=10, pady=5)

    if int(lst[0]) > 1 or int(lst[0]) == 1:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_1_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_1_5.grid(column=6, row=1, padx=10, pady=5)

    if int(lst[0]) > 2 or int(lst[0]) == 2:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_2_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_2_1.grid(column=2, row=2, padx=10, pady=5)

    if int(lst[0]) > 2 or int(lst[0]) == 2:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_2_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_2_2.grid(column=3, row=2, padx=10, pady=5)

    if int(lst[0]) > 2 or int(lst[0]) == 2:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_2_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_2_3.grid(column=4, row=2, padx=10, pady=5)
    if int(lst[0]) > 2 or int(lst[0]) == 2:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_2_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_2_4.grid(column=5, row=2, padx=10, pady=5)

    if int(lst[0]) > 2 or int(lst[0]) == 2:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_2_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_2_5.grid(column=6, row=2, padx=10, pady=5)

    if int(lst[0]) > 3 or int(lst[0]) == 3:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_3_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_3_1.grid(column=2, row=3, padx=10, pady=5)

    if int(lst[0]) > 3 or int(lst[0]) == 3:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_3_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_3_2.grid(column=3, row=3, padx=10, pady=5)

    if int(lst[0]) > 3 or int(lst[0]) == 3:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_3_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_3_3.grid(column=4, row=3, padx=10, pady=5)
    if int(lst[0]) > 3 or int(lst[0]) == 3:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_3_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_3_4.grid(column=5, row=3, padx=10, pady=5)
    if int(lst[0]) > 3 or int(lst[0]) == 3:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_3_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_3_5.grid(column=6, row=3, padx=10, pady=5)

    if int(lst[0]) > 4 or int(lst[0]) == 4:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_4_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_4_1.grid(column=2, row=4, padx=10, pady=5)

    if int(lst[0]) > 4 or int(lst[0]) == 4:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_4_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_4_2.grid(column=3, row=4, padx=10, pady=5)

    if int(lst[0]) > 4 or int(lst[0]) == 4:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_4_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_4_3.grid(column=4, row=4, padx=10, pady=5)

    if int(lst[0]) > 4 or int(lst[0]) == 4:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_4_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_4_4.grid(column=5, row=4, padx=10, pady=5)

    if int(lst[0]) > 4 or int(lst[0]) == 4:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_4_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_4_5.grid(column=6, row=4, padx=10, pady=5)

    if int(lst[0]) > 5 or int(lst[0]) == 5:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_5_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_5_1.grid(column=2, row=5, padx=10, pady=5)

    if int(lst[0]) > 5 or int(lst[0]) == 5:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_5_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_5_2.grid(column=3, row=5, padx=10, pady=5)
    if int(lst[0]) > 5 or int(lst[0]) == 5:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_5_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_5_3.grid(column=4, row=5, padx=10, pady=5)

    if int(lst[0]) > 5 or int(lst[0]) == 5:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_5_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_5_4.grid(column=5, row=5, padx=10, pady=5)

    if int(lst[0]) > 5 or int(lst[0]) == 5:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_5_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_5_5.grid(column=6, row=5, padx=10, pady=5)

    if int(lst[0]) > 6 or int(lst[0]) == 6:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_6_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_6_1.grid(column=2, row=6, padx=10, pady=5)

    if int(lst[0]) > 6 or int(lst[0]) == 6:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_6_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_6_2.grid(column=3, row=6, padx=10, pady=5)

    if int(lst[0]) > 6 or int(lst[0]) == 6:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_6_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_6_3.grid(column=4, row=6, padx=10, pady=5)
    if int(lst[0]) > 6 or int(lst[0]) == 6:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_6_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_6_4.grid(column=5, row=6, padx=10, pady=5)

    if int(lst[0]) > 6 or int(lst[0]) == 6:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_6_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_6_5.grid(column=6, row=6, padx=10, pady=5)

    if int(lst[0]) > 7 or int(lst[0]) == 7:

        if int(lst[1]) > 1 or int(lst[1]) == 1:
            check_7_1 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_7_1.grid(column=2, row=7, padx=10, pady=5)

    if int(lst[0]) > 7 or int(lst[0]) == 7:

        if int(lst[1]) > 2 or int(lst[1]) == 2:
            check_7_2 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_7_2.grid(column=3, row=7, padx=10, pady=5)

    if int(lst[0]) > 7 or int(lst[0]) == 7:

        if int(lst[1]) > 3 or int(lst[1]) == 3:
            check_7_3 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_7_3.grid(column=4, row=7, padx=10, pady=5)

    if int(lst[0]) > 7 or int(lst[0]) == 7:

        if int(lst[1]) > 4 or int(lst[1]) == 4:
            check_7_4 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_7_4.grid(column=5, row=7, padx=10, pady=5)

    if int(lst[0]) > 7 or int(lst[0]) == 7:

        if int(lst[1]) > 5 or int(lst[1]) == 5:
            check_7_5 = ttk.Combobox(frame_2,
                                     font=(1, ),
                                     values=lst_lesson,
                                     width=8)
            check_7_5.grid(column=6, row=7, padx=10, pady=5)

    def def_1():
        error = 0
        lst_day_1 = []
        try:
            a = check_1_1.get()
            lst_day_1.append(a)
        except:
            pass
        try:
            a = check_1_2.get()
            lst_day_1.append(a)
        except:
            pass
        try:
            a = check_1_3.get()
            lst_day_1.append(a)
        except:
            pass
        try:
            a = check_1_4.get()
            lst_day_1.append(a)
        except:
            pass

        try:
            a = check_1_5.get()
            lst_day_1.append(a)
        except:
            pass

        lst_day_2 = []

        try:
            a = check_2_1.get()
            lst_day_2.append(a)
        except:
            pass
        try:
            a = check_2_2.get()
            lst_day_2.append(a)
        except:
            pass
        try:
            a = check_2_3.get()
            lst_day_2.append(a)
        except:
            pass
        try:
            a = check_2_4.get()
            lst_day_2.append(a)
        except:
            pass

        try:
            a = check_2_5.get()
            lst_day_2.append(a)
        except:
            pass
        lst_day_3 = []
        try:
            a = check_3_1.get()
            lst_day_3.append(a)
        except:
            pass
        try:
            a = check_3_2.get()
            lst_day_3.append(a)
        except:
            pass

        try:
            a = check_3_3.get()
            lst_day_3.append(a)
        except:
            pass
        try:
            a = check_3_4.get()
            lst_day_3.append(a)
        except:
            pass
        try:
            a = check_3_5.get()
            lst_day_3.append(a)
        except:
            pass
        lst_day_4 = []
        try:
            a = check_4_1.get()
            lst_day_4.append(a)
        except:
            pass

        try:
            a = check_4_2.get()
            lst_day_4.append(a)
        except:
            pass
        try:
            a = check_4_3.get()
            lst_day_4.append(a)
        except:
            pass
        try:
            a = check_4_4.get()
            lst_day_4.append(a)
        except:
            pass
        try:
            a = check_4_5.get()
            lst_day_4.append(a)
        except:
            pass
        lst_day_5 = []
        try:
            a = check_5_1.get()
            lst_day_5.append(a)
        except:
            pass
        try:
            a = check_5_2.get()
            lst_day_5.append(a)
        except:
            pass
        try:
            a = check_5_3.get()
            lst_day_5.append(a)
        except:
            pass

        try:
            a = check_5_4.get()
            lst_day_5.append(a)
        except:
            pass
        try:
            a = check_5_5.get()
            lst_day_5.append(a)
        except:
            pass
        lst_day_6 = []
        try:
            a = check_6_1.get()
            lst_day_6.append(a)
        except:
            pass
        try:
            a = check_6_2.get()
            lst_day_6.append(a)
        except:
            pass
        try:
            a = check_6_3.get()
            lst_day_6.append(a)
        except:
            pass

        try:
            a = check_6_4.get()
            lst_day_6.append(a)
        except:
            pass

        try:
            a = check_6_5.get()
            lst_day_6.append(a)
        except:
            pass
        lst_day_7 = []
        try:
            a = check_7_1.get()
            lst_day_7.append(a)
        except:
            pass

        try:
            a = check_7_2.get()
            lst_day_7.append(a)
        except:
            pass
        try:
            a = check_7_3.get()
            lst_day_7.append(a)
        except:
            pass
        try:
            a = check_7_4.get()
            lst_day_7.append(a)
        except:
            pass

        try:
            a = check_7_5.get()
            lst_day_7.append(a)
        except:
            pass

        lst_error = []
        lst_check_1 = []
        lst_check = []
        for item in lst_day_1:
            if item != '':
                lst_check.append(item)

        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_1.append(lesson.group())

        dup = {x for x in lst_check_1 if lst_check_1.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        lst_check_2 = []
        lst_check = []

        for item in lst_day_2:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_2.append(lesson.group())

        dup = {x for x in lst_check_2 if lst_check_2.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        lst_check_3 = []
        lst_check = []

        for item in lst_day_3:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_3.append(lesson.group())

        dup = {x for x in lst_check_3 if lst_check_3.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        lst_check_4 = []
        lst_check = []

        for item in lst_day_4:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_4.append(lesson.group())

        dup = {x for x in lst_check_4 if lst_check_4.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        lst_check_5 = []
        lst_check = []

        for item in lst_day_5:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_5.append(lesson.group())

        dup = {x for x in lst_check_5 if lst_check_5.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        lst_check_6 = []
        lst_check = []

        for item in lst_day_6:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_6.append(lesson.group())

        dup = {x for x in lst_check_6 if lst_check_6.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)
        lst_check_1 = []
        lst_check = []

        lst_check_7 = []
        lst_check = []

        for item in lst_day_7:
            if item != '':
                lst_check.append(item)
        for i in lst_check:
            lesson = re.search(r"\w{1,}\s", i)
            if lesson:
                lst_check_7.append(lesson.group())

        dup = {x for x in lst_check_7 if lst_check_7.count(x) > 1}
        if len(dup) != 0:
            lst_error.append(dup)

        for item in lst_error:
            x = 'cant place two ' + str(item) + ' in one day'
            messagebox.showerror(message=x)
            error = 1

        # for i in lst_check:
        #     lesson = re.search(r"\w{1,}\s", i)
        #     lst_check_1.append(lesson.group())

        # dup = {x for x in lst_check_1 if lst_check_1.count(x) > 1}
        # print(dup)
        # x = 'cant place more than two ' + str(dup) + '  in one day'
        # if len(dup) != 0:
        #     messagebox.showerror(message=x)

        lst_les_1 = []
        lst_hard_ness_1 = []
        for item in lst_day_1:
            if item != '':
                lst_les_1.append(item)
        for i in lst_les_1:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_1.append(lesson.group(1))

        lst_les_2 = []
        lst_hard_ness_2 = []
        for item in lst_day_2:
            if item != '':
                lst_les_2.append(item)
        for i in lst_les_2:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_2.append(lesson.group(1))

        lst_les_3 = []
        lst_hard_ness_3 = []
        for item in lst_day_3:
            if item != '':
                lst_les_3.append(item)
        for i in lst_les_3:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_3.append(lesson.group(1))

        lst_les_4 = []
        lst_hard_ness_4 = []
        for item in lst_day_4:
            if item != '':
                lst_les_4.append(item)
        for i in lst_les_4:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_4.append(lesson.group(1))

        lst_les_5 = []
        lst_hard_ness_5 = []
        for item in lst_day_5:
            if item != '':
                lst_les_5.append(item)
        for i in lst_les_5:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_5.append(lesson.group(1))

        lst_les_6 = []
        lst_hard_ness_6 = []
        for item in lst_day_6:
            if item != '':
                lst_les_6.append(item)
        for i in lst_les_6:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_6.append(lesson.group(1))

        lst_les_7 = []
        lst_hard_ness_7 = []
        for item in lst_day_7:
            if item != '':
                lst_les_7.append(item)
        for i in lst_les_7:
            lesson = re.search(r"\{(.*)\n\}", i)
            if lesson:
                lst_hard_ness_7.append(lesson.group(1))

        x = 0
        for item in lst_hard_ness_1:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1

        x = 0
        for item in lst_hard_ness_2:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1
        x = 0
        for item in lst_hard_ness_3:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1

        x = 0
        for item in lst_hard_ness_4:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')

        x = 0
        for item in lst_hard_ness_5:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1

        x = 0
        for item in lst_hard_ness_6:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1

        x = 0
        for item in lst_hard_ness_7:

            if item == 'Hard':
                x += 1
            if x == 2 or x > 2:
                messagebox.showerror(
                    message='cant have two or more hard lessons in one day ')
                error = 1

        if error == 0:
            messagebox.showinfo(title='no errors',
                                message='your schedule has no ')

    button_import = Button(frame_2, text='check', font=(4, ), command=def_1)
    button_import.grid(column=3, row=9)


# - - - - - - -
label_enter_name_lessons = Label(fram_pan_add_lessons,
                                 text='Enter lessons name : ',
                                 font=(2, ))
label_enter_name_lessons.grid(pady=15, padx=8)
entry_lessons_name = Entry(fram_pan_add_lessons, width=15, font=(10, ))
entry_lessons_name.grid(pady=15)

label_enter_teacher_name = Label(
    fram_pan_add_lessons,
    text='Enter teacher name : ',
    font=(2, ),
)
label_enter_teacher_name.grid(pady=15, padx=8)
entry_teacher_name = Entry(fram_pan_add_lessons, width=15, font=(10, ))
entry_teacher_name.grid(pady=15)

label_enter_lessons_hardnes_combo = Label(
    fram_pan_add_lessons,
    text='Enter lessons hardnes : ',
    font=(2, ),
)
label_enter_lessons_hardnes_combo.grid(pady=15, padx=8)
lessons_hardnes_combo = ttk.Combobox(fram_pan_add_lessons,
                                     values=['Hard', 'Medium', 'Easy'],
                                     width=7,
                                     font=(7, ))
lessons_hardnes_combo.grid(pady=15)

b_save = Button(fram_pan_add_lessons,
                text='Save',
                font=(4, ),
                
                compound='right',
                command=save)
b_save.grid(pady=30)

pan_1 = PanedWindow(frame_schedule, orient='vertical')
pan_1.pack()
frame_1 = Frame(win, width=800, height=200, bg='gray70')
frame_2 = Frame(win, width=800, height=400, bg='khaki1')
pan_1.add(frame_1)
pan_1.add(frame_2)

label_days = Label(
    fram_pan_add_lessons_2,
    text='Select working days :',
    font=(2, ),
)

label_days.grid(column=2, row=0, padx=70)

sunday = IntVar()

sunday_check = Checkbutton(fram_pan_add_lessons_2,
                           text="Sunday",
                           variable=sunday,
                           onvalue=1,
                           offvalue=0,
                           font=(2, ))
sunday_check.grid(column=2, row=1, padx=10)

monday = IntVar()

monday_check = Checkbutton(fram_pan_add_lessons_2,
                           text="Monday",
                           variable=monday,
                           onvalue=1,
                           offvalue=0,
                           font=(2, ))
monday_check.grid(column=2, row=2, padx=10)

tuesday = IntVar()

tuesday_check = Checkbutton(fram_pan_add_lessons_2,
                            text="Tuesday",
                            variable=tuesday,
                            onvalue=1,
                            offvalue=0,
                            font=(2, ))
tuesday_check.grid(column=2, row=3, padx=10)

wednesday = IntVar()

wednesday_check = Checkbutton(fram_pan_add_lessons_2,
                              text="wednesday",
                              variable=wednesday,
                              onvalue=1,
                              offvalue=0,
                              font=(2, ))
wednesday_check.grid(column=2, row=4, padx=10)

thursday = IntVar()

thursday_check = Checkbutton(fram_pan_add_lessons_2,
                             text="Thursday",
                             variable=thursday,
                             onvalue=1,
                             offvalue=0,
                             font=(2, ))
thursday_check.grid(column=2, row=5, padx=10)

friday = IntVar()

friday_check = Checkbutton(fram_pan_add_lessons_2,
                           text="Friday",
                           variable=friday,
                           onvalue=1,
                           offvalue=0,
                           font=(2, ))
friday_check.grid(column=2, row=6, padx=10)

saturday = IntVar()

saturday_check = Checkbutton(fram_pan_add_lessons_2,
                             text="Saturday",
                             variable=saturday,
                             onvalue=1,
                             offvalue=0,
                             font=(2, ))
saturday_check.grid(column=2, row=7, padx=10)

label_days = Label(
    fram_pan_add_lessons_2,
    text='How many lessons per day:',
    font=(2, ),
)
label_days.grid(column=3, row=0, padx=50)
per_day_combo = ttk.Combobox(fram_pan_add_lessons_2,
                             values=['1', '2', '3', '4', '5'],
                             width=7,
                             font=(7, ))
per_day_combo.grid(column=3, row=2)


b_save_2 = Button(fram_pan_add_lessons_2,
                  text='Save',
                  font=(4, ),
                  
                  compound='right',
                  command=save_2)
b_save_2.grid(column=3, row=6)
#
# -----------------------------------------------------------
button_import = Button(frame_1,
                       text='Import lessons',
                       font=(4, ),
                       command=b_import)
button_import.grid(padx=40, pady=40)

button_make = Button(frame_2,
                     text='Import schadule',
                     font=(4, ),
                     command=import_2)
button_make.grid(padx=300, pady=150)
# ---------------
win.mainloop()
