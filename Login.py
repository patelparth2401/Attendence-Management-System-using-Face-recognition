from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import attendence
import SR
import openpyxl,xlrd
from openpyxl import Workbook
import pathlib
#Functionality Part
def user_Enter(event):
    if uname_Entry.get()=="User Name":
        uname_Entry.delete(0,END)

def pass_Enter(event):
    if pass_Entry.get()=="Password":
        pass_Entry.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    pass_Entry.config(show='*')
    eye_button.config(command=show)
    
def show():
    openeye.config(file='openeye.png')
    pass_Entry.config(show='')
    eye_button.config(command=hide)

def connect():
    db=mysql.connector.connect(host='localhost',
                        database='fr',
                        user='root',
                        password='')
    return db
    
def login():
    if uname_Entry.get()=='' or pass_Entry.get()=='' or menu.get()=="Select User Type":
        messagebox.showerror('Error',"Enter all fields")
    else:
        try:
            db=connect()
            cursor=db.cursor()
        except:
            messagebox.showerror('Error',"Database connectivity issue")
        query="select * from user where username= %s and pass= %s and Type=%s "
        cursor.execute(query,(uname_Entry.get(),pass_Entry.get(),menu.get()))
        if menu.get()== "Admin":  
            if(cursor.fetchone()):
                Login.destroy()        
                SR.Student_registration()
            else:
                print("Invalid user name or password")
        else:
            if(cursor.fetchone()):
                Login.destroy()        
                attendence.attendance()
            else:
                print("Invalid user name or password")
            
        
#root
Login=Tk()
Login.geometry("800x650+50+25")
Login.resizable(False,False)
Login.title('Login Page')
Login.config(bg='white')

background="#06283D"
foreground="#EDEDED"

Name=Label(Login,text="Attendance System",width=44,font=("Microsoft  yahei UI Light",23,"bold"),bg="white",fg=background)
Name.place(y=10)

old=Image.open('MBIT.png')
new=old.resize((100,120))
mbit=ImageTk.PhotoImage(new)
mbit_logo=Label(Login,image=mbit,bg="white")
mbit_logo.place(x=50,y=10)

old_1=Image.open('CVMU.png')
new_1=old_1.resize((100,90))
cvm=ImageTk.PhotoImage(new_1)
cvm_logo=Label(Login,image=cvm,bg="white")
cvm_logo.place(x=650,y=10)

#frame
frame=Frame(Login,bg=background,width=350,height=470)
frame.place(x=250,y=100)
#Logo
heading=Label(frame,text="Login page",font=("Microsoft  yahei UI Light",23,"bold"),bg=background,fg=foreground)
heading.place(x=28,y=10)
#uname
uname_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
uname_Entry.place(x=40,y=100)
uname_Entry.insert(0,"User Name")
uname_Entry.bind('<FocusIn>',user_Enter)

#line frame
line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=125)

#User Type
menu= StringVar(frame)
menu.set("Select User Type")
drop= OptionMenu(frame, menu,"Admin",'Faculty')
drop.place(x=40,y=150)
drop.config(fg="white",bd=1,bg=foreground,font=14,activebackground=background,activeforeground=foreground)

#line frame
line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=200)

#pass
pass_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
pass_Entry.place(x=40,y=220)
pass_Entry.insert(0,"Password")
pass_Entry.bind('<FocusIn>',pass_Enter)

#line frame
line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=245)

openeye=PhotoImage(file="openeye.png")
img_lbl=Label()
eye_button=Button(frame,image=openeye,width=13,height=10,bd=0,
                  bg=background,activebackground=background,cursor='hand2',command=hide)
eye_button.place(x=270,y=225)

login_btn=Button(frame,text='Login',font=('open sans',16,'bold'),
                 fg=background,bg=foreground,width=20,bd=0,
                 activebackground=background,activeforeground=foreground,command=login)
login_btn.place(x=40,y=300)

o_img=Image.open('img1.png')
n_img=o_img.resize((170,100))
img=ImageTk.PhotoImage(n_img)
img1=Label(Login,image=img,bg="white")
img1.place(x=50,y=325)

o1=Image.open('img2.jpg')
n1=o1.resize((150,100))
img_r=ImageTk.PhotoImage(n1)
img2=Label(Login,image=img_r,bg="white")
img2.place(x=650,y=325)
Login.mainloop()
