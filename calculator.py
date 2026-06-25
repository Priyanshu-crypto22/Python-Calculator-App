import tkinter as tk
import math,keyboard

window=tk.Tk()

window.title("Calculator")
window.geometry('290x385')

entry=tk.Entry(window,width=13,font=('Arial',30),justify='right',takefocus=False)
command=''
memory=-1
flag=False

def add():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='add'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='add'
        entry.delete(0,tk.END)

def mul():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='mul'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='mul'
        entry.delete(0,tk.END)

def sub():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='sub'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='sub'
        entry.delete(0,tk.END)

def div():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='div'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='div'
        entry.delete(0,tk.END)

def sq():
    global flag
    if not entry.get() or entry.get()=='ERROR':
        return
    x=float(entry.get())
    entry.delete(0,tk.END)
    x*=x
    entry.insert(0,x)
    flag=True

def clear_all():
    global memory,command,flag
    command=''
    memory=-1
    entry.delete(0,tk.END)
    flag=False

def square_root():
    global command,memory,flag
    if not entry.get() or entry.get()=='ERROR':
        return
    x=float(entry.get())
    if x<0:
        entry.delete(0,tk.END)
        entry.insert(0,"ERROR")
        memory=-1
        command=''
        flag=True
        return
    x=math.sqrt(x)
    entry.delete(0,tk.END)
    entry.insert(0,x)
    flag=True

def modulus():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='mod'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='mod'
        entry.delete(0,tk.END)

def power():
    global memory,command,flag
    if memory!=-1:
        equals()
        command='power'
        flag=True
    else:
        if not entry.get() or entry.get()=='ERROR':
            return
        memory=float(entry.get())
        command='power'
        entry.delete(0,tk.END)

def inverse():
    global command,memory,flag
    if not entry.get() or entry.get()=='ERROR':
        return
    x=float(entry.get())
    if x==0:
        entry.delete(0,tk.END)
        entry.insert(0,'ERROR')
        memory=-1
        command=''
        flag=True
    else:
        x=1/x
        entry.delete(0,tk.END)
        entry.insert(0,x)
        flag=True

def insert_digit(x):
    global flag
    if flag:
        entry.delete(0,tk.END)
        flag=False
    entry.insert(tk.END,x)

def backspace():
    if not entry.get():
        return
    elif entry.get()=='ERROR':
        entry.delete(0,tk.END)
    else:
        entry.delete(len(entry.get())-1)

def equals():
    global memory,command,flag
    if not entry.get() or entry.get()=='ERROR':
        return
    n2=float(entry.get())
    if command=='add':
        temp=memory+n2
    elif command=='mul':
        temp=memory*n2
    elif command=='sub':
        temp=memory-n2
    elif command=='div':
        if n2==0:
            entry.delete(0,tk.END)
            entry.insert(0,'ERROR')
            memory=-1
            command=''
            flag=True
            return
        else:
            temp=memory/n2
    elif command=='mod':
        if n2==0:
            entry.delete(0,tk.END)
            entry.insert(0,'ERROR')
            memory=-1
            command=''
            flag=True
            return
        else:
            temp=memory%n2
    elif command=='power':
        temp=math.pow(memory,n2)
    else:
        return
    flag=True
    memory=-1
    entry.delete(0,tk.END)
    entry.insert(0,temp)

def insert_point():
    global flag
    if flag:
        entry.delete(0,tk.END)
        flag=False
    if not entry.get() or entry.get()=='ERROR':
        entry.insert(0,'0.')
    elif '.' not in entry.get():
        entry.insert(tk.END,'.')

def clear_e():
    global flag
    flag=False
    if entry.get():
        entry.delete(0,tk.END)

def key_press(event):
    key=event.keysym
    if key in '0123456789':
        insert_digit(key)
    elif key == 'plus':
        add()
    elif key == 'minus':
        sub()
    elif key == 'asterisk':
        mul()
    elif key == 'slash':
        div()
    elif key == 'percent':
        modulus()
    elif key == 'Return':
        equals()
    elif key == 'period':
        insert_point()
    elif key == 'BackSpace':
        backspace()
    elif key == 'Escape':
        clear_all()
    




addition=tk.Button(text='add',height=3,width=9,command=add,foreground='white',background='black')
subtraction=tk.Button(text='subtract',height=3,width=9,command=sub,foreground='white',background='black')
mult=tk.Button(text='multiply',height=3,width=9,command=mul,foreground='white',background='black')
divide=tk.Button(text='divide',height=3,width=9,command=div,foreground='white',background='black')
equal=tk.Button(text='equal',height=3,width=9,command=equals,foreground='white',background='black')
clear=tk.Button(text='CE',height=3,width=9,command=clear_e,foreground='white',background='black')
back=tk.Button(text='Back',height=3,width=9,command=backspace ,foreground='white',background='black')
square=tk.Button(text='square',height=3,width=9,command=sq,foreground='white',background='black')
c_all=tk.Button(text='C',height=3,width=9,command=clear_all,foreground='white',background='black')
sq_root=tk.Button(text='Root',height=3,width=9,command=square_root,foreground='white',background='black')
mod=tk.Button(text='%',height=3,width=9,command=modulus,foreground='white',background='black')
inv=tk.Button(text='1/x',height=3,width=9,command=inverse,foreground='white',background='black')
exp=tk.Button(text='power',height=3,width=9,command=power,foreground='white',background='black')
point=tk.Button(text='.',height=3,width=9,command=insert_point,foreground='white',background='black')
zero=tk.Button(text='0',height=3,width=9,command= lambda x=0: insert_digit(x),foreground='white',background='black')

entry.grid(row=0,column=0,columnspan=4)


for i in range(1,10):
    button=tk.Button(text=i,height=3,width=9,command=lambda x=i : insert_digit(x),foreground='white',background='black')
    r=(i+8)//3
    c=(i-1)%3
    button.grid(row=r,column=c,)


addition.grid(row=5,column=3)
subtraction.grid(row=4,column=3)
mult.grid(row=3,column=3)
divide.grid(row=2,column=3)
equal.grid(row=6,column=3)
clear.grid(row=1,column=1)
back.grid(row=1,column=3)
sq_root.grid(row=2,column=2)
c_all.grid(row=1,column=2)
exp.grid(row=6,column=0)
inv.grid(row=2,column=0)
mod.grid(row=1,column=0)
square.grid(row=2,column=1)
zero.grid(row=6,column=1)
point.grid(row=6,column=2)



window.bind('<Key>',key_press)
window.mainloop()