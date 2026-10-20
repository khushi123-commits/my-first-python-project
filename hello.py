import tkinter as tk
def calculate():
    print("calculator")
window=tk.Tk()
window.title("my calculator")
window.geometry("300x400")

display=tk.Entry(window,
font=("airtel",20),
justify="right"
)
display.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky="ew")

def click(number):
    if number=="=":
        calculate()
    else:    
     display.insert(tk.END,number)
def clear():
    display.delete (0,tk.END)
def calculate():
  try:
        result=eval(display.get())
        display.delete(0,tk.END)
        display.insert(0,result)
  except:
     display.delete(0,tk.END)
display.insert(0,"error")

#number button
Button=[("7",1,0),("8",1,1),("9",1,2),("/",1,3),
        ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
        ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
        ("0",4,0),(".",4,1),("=",4,2),("+",4,3)]

for text, row,column in Button:
    tk.Button(
        window,
        text=text,
        command=lambda x=text: click(x),
        width=5,
        height=2
    ).grid(row=row, column=column)        
tk.Button(
  window , text="Clear",
command=clear).grid(row=4,column=0,columnspan=4)

window.mainloop()



