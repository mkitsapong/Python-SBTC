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
root.option_add("*Font", "Fixedsys 20")
menus = {"Bmw Z4 (3.9M)":39990000, 
"Honda Accord (1.7M)":1799000,
"Toyota Camry (1.4M)":1455000, 
"Mercedes Benz c300 (2.5M)":2599000, 
"Suzuki Swift (557K)":557000, 
"Nissan Almera (509K)":509000, 
"Ford Mustang (3.6M)":3699000, 
"Ferrari Roma (21M)":21230000,
"Mitsubishi Pajero (1.2M)":1299000, 
"Audi a5 (3.5M)":3599000,
"Maserati Granturismo (14M)":14390000,
"Rolls Royce Cullinan (32M)":32900000}
item_per_row = 3
tv_menu =StringVar()

f1 = Frame (root) 
f1.grid(row=0,column=0,columnspan=2)
f2 = Frame (root) 
f2.grid(row=1, column=1) 
Label(f1,text = "PANIDA NILNON 64301280010",width=50,bg="salmon3").pack(padx=20,pady=20)
Label(f1,text = "Car Shop",width=150,bg="LightPink2").pack(padx=30,pady=30)

for i, k in enumerate(menus.keys()):
    btn = Button(f2, text=k, width=50,bg="dark salmon")
    btn.grid(row=i// item_per_row, column = i % item_per_row)
    btn.bind("<Button-1>", show)
Label(root, text="list", textvariable=tv_menu, fg="maroon4").grid(columnspan=item_per_row)

root.mainloop()