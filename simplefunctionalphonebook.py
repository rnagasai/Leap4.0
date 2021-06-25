from tkinter import *

pb=Tk()
pb.geometry('400x400')
pb.title("Phone Book")

D=dict()

def add1():
    if e1.get() and e2.get():
        n=e1.get()
        p=e2.get()
        D[n]=p
        e1.delete(0,END)
        e2.delete(0,END)
        update_pb()

def view1():
    e1.delete(0,END)
    e2.delete(0,END)
    ans=select.curselection()
    n=list(map(select.get,ans))
    e1.insert(END,n)
    p=D[e1.get()]
    e2.insert(END,p)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)

def del1():
    ans = select.curselection()
    n = list((map(select.get, ans)))
    del D[n[0]]
    update_pb()

def update_pb():
    select.delete(0,END)
    for k in D.keys():
        select.insert(END,k)

f1=Frame(pb)
f1.pack()

f2=Frame(pb)
f2.pack()

l1=Label(f1,text="Name",fg='blue')
l1.pack(side='left',pady=20)
e1=Entry(f1,width=30,fg='blue')
e1.pack(pady=20)

l2=Label(f2,text="Phone No.",fg='blue')
l2.pack(side='left')
e2=Entry(f2,width=30,fg='blue')
e2.pack()


b1 = Button(pb,text="Add Contact",fg='white',bg='blue',command=add1)
b2 = Button(pb,text="View Contact",fg='white',bg='blue',command=view1)
b3 = Button(pb,text="Delete Contact",fg='white',bg='blue',command=del1)
b4 = Button(pb,text="Clear Fields",fg='white',bg='blue',command=clear)
b1.place(x=10,y=100)
b2.place(x=110,y=100)
b3.place(x=210,y=100)
b4.place(x=310,y=100)

ls=Label(text='''List of Contacts
Select one of them 
to view or delete''',fg='blue')
ls.place(x=20,y=200)

select = Listbox(pb, height=12,width=30)
select.place(x=150,y=150)



pb.mainloop()