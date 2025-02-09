from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

def name_Enter(event):
    if name_Entry.get()=="Name":
        name_Entry.delete(0,END)

def pass_Enter(event):
    if pass_Entry.get()=="Password":
        pass_Entry.delete(0,END)
        
def email_Enter(event):
    if email_Entry.get()=="Email":
        email_Entry.delete(0,END)

def user_Enter(event):
    if uname_Entry.get()=="User Name":
        uname_Entry.delete(0,END)
        
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

def register():
    if (uname_Entry.get()=='' 
        or pass_Entry.get()==''or menu.get()=="Department" or name_Entry.get()=='' or email_Entry.get()==''):
        messagebox.showerror('Error',"Enter all fields")
    else:
        print(uname_Entry.get(),pass_Entry.get(),name_Entry.get(),email_Entry.get(),menu.get())
        try:
            db=connect()
            cursor=db.cursor()
        except:
            messagebox.showerror('Error',"Database connectivity issue")
        query='insert into user (Name,email,Dept,username,pass,Type) values(%s,%s,%s,%s,%s,"Faculty")'
        cursor.execute(query,(name_Entry.get(),email_Entry.get(),menu.get(),uname_Entry.get(),pass_Entry.get()))
        db.commit()
        messagebox.showinfo("Suscces","Registered successfully")
        
        
Register=Tk()
Register.geometry("800x650+50+25")
Register.resizable(False,False)
Register.title('Registration Page')
Register.config(bg='white')

background="#06283D"
foreground="#EDEDED"

Name=Label(Register,text="Attendance System",width=44,font=("Microsoft  yahei UI Light",23,"bold"),bg="#06283D",fg=foreground)
Name.place(y=10)

old=Image.open('MBIT.png')
new=old.resize((100,120))
mbit=ImageTk.PhotoImage(new)
mbit_logo=Label(Register,image=mbit,bg="white")
mbit_logo.place(x=50,y=10)

old_1=Image.open('CVMU.png')
new_1=old_1.resize((100,90))
cvm=ImageTk.PhotoImage(new_1)
cvm_logo=Label(Register,image=cvm,bg="white")
cvm_logo.place(x=650,y=10)

#frame
frame=Frame(Register,bg=background,width=350,height=470)
frame.place(x=250,y=100)
#Logo
heading=Label(frame,text="Faculty Registration",font=("Microsoft  yahei UI Light",23,"bold"),bg=background,fg=foreground)
heading.place(x=28,y=10)
#uname
name_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
name_Entry.place(x=40,y=100)
name_Entry.insert(0,"Name")
name_Entry.bind('<FocusIn>',name_Enter)

#line frame
line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=125)

email_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
email_Entry.place(x=40,y=140)
email_Entry.insert(0,"Email")
email_Entry.bind('<FocusIn>',email_Enter)

line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=165)
#User Type
menu= StringVar(frame)
menu.set("Department")
drop= OptionMenu(frame, menu,"IT",'CE','ASH')
drop.place(x=40,y=180)
drop.config(fg="white",bd=1,bg=foreground,font=14,activebackground=background,activeforeground=foreground)

uname_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
uname_Entry.place(x=40,y=225)
uname_Entry.insert(0,"User Name")
uname_Entry.bind('<FocusIn>',user_Enter)

line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=250)

pass_Entry=Entry(frame,width=30,font=("Microsoft  yahei UI Light",14,"bold"),bd=0,fg=foreground,bg=background)
pass_Entry.place(x=40,y=270)
pass_Entry.insert(0,"Password")
pass_Entry.bind('<FocusIn>',pass_Enter)

line=Frame(frame,width=250,height=2,bg=foreground)
line.place(x=40,y=295)

openeye=PhotoImage(file="openeye.png")
img_lbl=Label()
eye_button=Button(frame,image=openeye,width=13,height=10,bd=0,
                  bg=background,activebackground=background,cursor='hand2',command=hide)
eye_button.place(x=270,y=275)

login_btn=Button(frame,text='Register',font=('open sans',16,'bold'),
                 fg=background,bg=foreground,width=20,bd=0,
                 activebackground=background,activeforeground=foreground,command=register)
login_btn.place(x=40,y=350)

o_img=Image.open('img1.png')
n_img=o_img.resize((170,100))
img=ImageTk.PhotoImage(n_img)
img1=Label(Register,image=img,bg="white")
img1.place(x=50,y=325)

o1=Image.open('img2.jpg')
n1=o1.resize((150,100))
img_r=ImageTk.PhotoImage(n1)
img2=Label(Register,image=img_r,bg="white")
img2.place(x=650,y=325)

Register.mainloop()
