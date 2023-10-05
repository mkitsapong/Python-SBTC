from tkinter import* 
root =Tk() 
root.option_add("*Font", "Fixedsys 25")
f1 = Frame (root, bg="red") 
f1.grid(row=0, column=0, columnspan=2)
f2 = Frame (root, bg="purple")
f2.grid(row=1,column=0) 
f3=Frame (root, bg="pink")
f3.grid(row=1,column=1)
Label(f1, text="Kitsapong", width= 30).pack (padx=15, pady=15) 
for manu in ["apple","papaya","banana","orange"]:
    Button(f2, text=manu).pack(fill=X, padx=15, pady=15) 
for i,n in enumerate("1234567890"):
    Button(f3, text=n).grid(row=i//3,column=i%3, padx=10, pady=10)
root.mainloop()
