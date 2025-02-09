from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import openpyxl as ox
import pandas as pd
    
def attendance():
    
    root=Tk()
    root.title("Attendance data")
    root.geometry("1000x500+50+50")
    
    Name=Label(root,text="Class vise attendance report",font=("Microsoft  yahei UI Light",23,"bold"),bg="#06283D",fg="#EDEDED")
    Name.pack(pady=40)
    def open():
        filename=filedialog.askopenfilename(title="Open a file",
                                            filetype=(("xlxs files",".xlsx"),("All files","*."),("csv files",".csv")))
        if filename:
            try:
                filename =r"{}".format(filename)
                df=pd.read_excel(filename)
            except:
                messagebox.showerror("Error","you cant access this file")
            tree.delete()
        
            tree['column']= list(df.columns)
            tree['show']="headings"
            for col in tree['columns']:
                tree.heading(col, text=col)
        
            df_rows=df.to_numpy().tolist()
            for row in df_rows:
                tree.insert("", "end", values=row)


    frame=Frame(root)
    frame.pack(pady=25)

    tree=ttk.Treeview(frame)
    tree.pack()
    
    button=Button(root,text='open',width=60,height=2,font=30,fg="#EDEDED",bg="#06283D",command=open)
    button.pack()


    root.mainloop()