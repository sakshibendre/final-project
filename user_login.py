from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import student
from face_recognition import Face_Recognition

#from register import Register
import mysql.connector
''' --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport'''
import os

class user_Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\final project\final project\SOURCE\images\login_bg.jpeg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"C:\final project\final project\SOURCE\images\login_profile.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="light green",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        '''loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)'''


        # Creating Button Forget
        Forgotbtn=Button(frame1,text="Forgot Password",command=self.forget_pwd,font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        Forgotbtn.place(x=120,y=370,width=100,height=20)


        #  THis function is for open register window
        '''def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)'''


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="user" and self.txtpwd.get()=="user"):
            messagebox.showinfo("Successfully","Welcome to Attendance Management System sUsing Facial Recognition")
            open_min=messagebox.askyesno("YesNo","User Window")
            if open_min>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
        
                # Creating Button New Password
                loginbtn=Button(self.root,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC",href="home.py")
        #loginbtn.place(x=70,y=300,width=270,height=35)

    def forget_pwd(self):
        '''if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:'''
        self.root2=Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("400x400+610+170")
        l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
        l.place(x=0,y=10,relwidth=1)
        # -------------------fields-------------------
        #label1 
        ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=70,y=80)

        #Combo Box1
        self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=70,y=110,width=270)


        #label2 
        sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=70,y=150)

        #entry2 
        self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=70,y=180,width=270)

        #label2 
        new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        new_pwd.place(x=70,y=220)

        #entry2 
        self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.new_pwd.place(x=70,y=250,width=270)

        # Creating Button New Password
        loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=70,y=300,width=270,height=35)

# =====================main program Face deteion system====================
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Home Page")

        #first image
        img=Image.open(r"C:\final project\final project\SOURCE\images\college3.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        #second image
        img1=Image.open(r"C:\final project\final project\SOURCE\images\college2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)

        #Third image
        img2=Image.open(r"C:\final project\final project\SOURCE\images\college1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)

        #bg image
        img3=Image.open(r"C:\final project\final project\SOURCE\images\home_bg.jpeg")
        img3=img3.resize((40000,1000),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\final project\final project\SOURCE\images\student_details.jpeg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_pannels,cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)


        #detect button
        img5=Image.open(r"C:\final project\final project\SOURCE\images\face_detection.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command = self.f_recog,cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendance button
        img6=Image.open(r"C:\final project\final project\SOURCE\images\attendance.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help button
        img7=Image.open(r"C:\final project\final project\SOURCE\images\help_desk.jpeg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40)

        
        #Train data button
        img8=Image.open(r"C:\final project\final project\SOURCE\images\train_data.jpeg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photo button
        img9=Image.open(r"C:\final project\final project\SOURCE\images\photos.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer button
        img10=Image.open(r"C:\final project\final project\SOURCE\images\developer.jpeg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit button
        img11=Image.open(r"C:\final project\final project\SOURCE\images\exit.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2", font=("times new roman",25,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def f_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


if __name__ == "__main__":
    root=Tk()
    app=user_Login(root)
    root.mainloop()