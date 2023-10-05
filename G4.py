from tkinter import*
from datetime import datetime
group_1_cnt =0 
group_2_cnt =0 
total_cnt =0 
total2_cnt =0 
def record_transaction(t_total):
    with open("scoree.csv", mode='a', newline='', encoding='UTF-8') as f:
        score = t_total[t_total]
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{t_total},{score}, {dt}\n')

def show(e):
    menu_item = e.widget.cget("text")
    tv_menu.set(f"Them = {t_total}, score = {t_total[t_total]}")
    record_transaction(t_total)

def group_1_click(): 
    global group_1_cnt 
    global total_cnt 
    group_1_cnt+=1
    total_cnt+=1 
    t_group_1.set(group_1_cnt )
    t_total.set(f'total={total_cnt}') 

def group_2_click(): 
    global group_2_cnt 
    global total2_cnt 
    group_2_cnt+=1 
    total2_cnt+=1 
    t_group_2.set(group_2_cnt )
    t_total2.set(f'total={total2_cnt}') 

root = Tk() 
root.option_add("*Font", "Fixedsys 30") 

t_group_1 = IntVar()
t_group_2 = IntVar() 
t_total = StringVar() 
t_total2 = StringVar() 
tv_menu =StringVar()

Button (root, text="TEAM Blue", bg="blue", width="10", command=group_1_click).grid(row=0,column=0) 
Button (root, text="TEAM RED", bg="red",width="10", command=group_2_click).grid(row=0,column=1) 
Label(root, textvariable=t_group_1, bg="pink").grid(row=1, column=0, sticky="news") 
Label(root, textvariable=t_group_2, bg="red").grid(row=1,column=1, sticky="news") 
Label(root, textvariable=t_total,bg="yellow").grid(row=2, column=0,sticky="news") 
Label(root, textvariable=t_total2,bg="yellow").grid(row=2, column=1,sticky="news") 
Label(root, text=total_cnt, textvariable=tv_menu, fg="Red").grid(columnspan=2)
root.mainloop()