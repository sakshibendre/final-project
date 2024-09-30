from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        
#=============== bg image ==================#
        self.bg=ImageTk.PhotoImage(file=r"D:\Codings\FINAL YEAR PROJECT\SOURCE\images\walt.jpg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
#=============== side img ==================#
        self.bg1=ImageTk.PhotoImage(file=r"D:\Codings\FINAL YEAR PROJECT\SOURCE\images\left.jpg")
        
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
#=============== main frame ==================#
        

        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)
        
#=============== label and entry ==================#      
        fname=Label(frame, text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame, text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
#============row2
        
        contact=Label(frame, text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        
        email=Label(frame, text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        
#===============row3
        security_Q=Label(frame, text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your College name","Favourite Color")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        
        security_A=Label(frame, text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
#==============row4
        
        
        pswd=Label(frame, text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame, text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        
#============check button
        checkbtn=Checkbutton(frame,text="I agree the terms and conditions",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
#============button

        btn=Button(frame,text="Register",font=("times new roman",15,"bold"),bg="lightgreen")
        btn.place(x=50,y=430,width=100,height=50)
        
        btnlog=Button(frame,text="Login",font=("times new roman",15,"bold"),bg="lightgreen")
        btnlog.place(x=370,y=430,width=100,height=50)


if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
        
