from tkinter import *
group_1_cnt = 0
group_2_cnt = 0
group_3_cnt = 0 
group_4_cnt = 0 
total_cnt = 0

def group_1_click():
    global group_1_cnt
    global total_cnt
    group_1_cnt += 1
    total_cnt += 1
    t_G1.set(group_1_cnt)
    t_total.set(f'total = {total_cnt}')

def group_2_click():
    global group_2_cnt
    global total_cnt
    group_2_cnt += 1
    total_cnt -= 1
    t_G2.set(group_2_cnt)
    t_total.set(f'total = {total_cnt}')

def group_3_click():
    global group_3_cnt
    global total_cnt
    group_3_cnt += 1
    total_cnt *= 2
    t_G3.set(group_3_cnt)
    t_total.set(f'total = {total_cnt}')

def group_4_click():
    global group_4_cnt
    global total_cnt
    group_4_cnt += 1
    total_cnt /= 2
    t_G4.set(group_4_cnt)
    t_total.set(f'total = {total_cnt}') 

root = Tk()
root.option_add("*Font", "Fixedsys 25")

t_G1 = IntVar()
t_G2 = IntVar()
t_G3 = IntVar()
t_G4 = IntVar()
t_total = StringVar()

Button(root, text="+ 1", bg="AntiqueWhite1", width=12,
       command=group_1_click).grid(row=0,column=0,ipady=10,ipadx=10)
Button(root, text="- 1", bg="AntiqueWhite1", width=12,
       command=group_2_click).grid(row=0,column=1,ipady=10,ipadx=10)
Button(root, text="* 2", bg="AntiqueWhite1", width=12,
       command=group_3_click).grid(row=0,column=2,ipady=10,ipadx=10)
Button(root, text="/ 2", bg="AntiqueWhite1", width=12, 
       command=group_4_click).grid(row=0,column=3,ipady=10,ipadx=10)   

Label(root, textvariable=t_G1, bg="SeaGreen1").grid(row=1, column=0, sticky="news")
Label(root, textvariable=t_G2, bg="SeaGreen1").grid(row=1, column=1, sticky="news")
Label(root, textvariable=t_G3, bg="SeaGreen1").grid(row=1, column=2, sticky="news")
Label(root, textvariable=t_G4, bg="SeaGreen1").grid(row=1, column=3, sticky="news")
Label(root, textvariable=t_total, bg="cadet blue").grid(row=2, columnspan=10, sticky="news")
root.mainloop()