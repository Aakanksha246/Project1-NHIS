import tkinter as tk 
from tkinter import ttk
def button_click (value):
    current_text = entry.get()
    if value == "=":
        try:
            result = eval (current_text)
            entry.delete ( 0,tk.END)
            entry.insert (0,str(result))
        except Exception:
            entry.delete (0,tk.END)
            entry.insert (0,"Error")
    elif value =="C":
        entry.delete (0,tk.END)
    elif value=="delete":
        entry.delete(len(current_text)-1,tk.END)
    else:
        entry.insert (tk.END,value)
root =tk.Tk()
root.title (" Advanced Calculator") 
root.geometry("280x350")
root.configure(bg="#f0f0f0")
entry = tk.Entry(root,width=20,font=("Arial",18),borderwidth=3,relief="solid")
entry.grid(row=0,column=0,columnspan=4,padx=3,pady=3)
Buttons =["7","8","9","/",
          "4","5","6","*",
          "1","2","3","-",
          "C","0","=","+",
          ".","delete"
          ]
btn_fg ="#f0f0f0"
btn_hover_bg ="powder blue"
def on_enter(e):
    e.widget['background']=btn_hover_bg
def on_leave(e):
    e.widget['background']=btn_fg
for i, Button in enumerate (Buttons):
    row = (i//4) + 1
    col = i % 4
    btn = tk.Button(root,text=Button,width=5,height=2,font=("Arial",10),command=lambda value= Button:button_click(value))
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
footer_label = tk.Label(root,text="My First Project",font=("Arial",10),bg="#f0f0f0",fg="#888888")
footer_label.grid(row=6,column=0,columnspan=4,pady=10)
root.mainloop()    

