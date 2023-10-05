from tkinter import*
from datetime import datetime

def record_transaction(menu_item):
    with open("Carshop.csv", mode='a', newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{menu_item},{price}, {dt}\n')

def show(e):
    menu_item = e.widget.cget("text")
    tv_menu.set(f"Car = {menu_item}, price = {menus[menu_item]} Baht")
    record_transaction(menu_item)

root = Tk()
root.option_add("*Font", "consoles 20")
menus = {"โกโก้":35, 
"ชามะนาว":40,
"ชานม":35, 
"ชาเขียว":25, 
"ชามะนาวโซดา":50, }
item_per_row = 2
tv_menu =StringVar()

f1 = Frame (root) 
f1.grid(row=0,column=0,columnspan=2)
f2 = Frame (root) 
f2.grid(row=1, column=1) 
Label(f1,text = "Kitsapong Maunkwan",width=59,bg="khaki").pack(padx=16,pady=16)

for i, k in enumerate(menus.keys()):
    btn = Button(f2, text=k, width=30,bg="#D26D2A")
    btn.grid(row=i// item_per_row, column = i % item_per_row)
    btn.bind("<Button-1>", show)
Label(root, text="list", textvariable=tv_menu, fg="red",bg="lawngreen",width=60).grid(columnspan=item_per_row)

root.mainloop()