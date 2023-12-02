from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import database, login_admin

class UpdatePass:
    

    def __init__(self):
        self.root = Toplevel()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Update Password")
        self.width_of_window = 900
        self.height_of_window = 450
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.configure(bg ='#fff')
        self.root.title("carObar -- Create New Password")
        self.root.resizable(width =False, height= False)
    

    def update_passw_frame(self):
        self.image_path = Image.open('images/mainpage/main.png').resize((350,300))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.imgTk, width=350, height=300,bg='white')
        self.image_label.place(x=50, y=80)
        

        self.frame = Frame(self.root,width=350,height=450,bg='white')
        self.frame.place(x=480,y=70)

        self.heading = Label(self.frame,text ='Update Password' , fg='#57a1f8',bg = 'white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.heading.place(x=80,y=5)

        #------------------------------- ///// USERNAME ENTRY ///// -----------------------------##
    
        def on_enter(e):
            self.Username.delete(0,'end')

        def on_leave(name):
            name == self.Username.get()
            if name=='':
                self.user.insert(0,'Username')
                
        self.Username = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.Username.place(x=30,y=80)
        self.Username.insert(0,'Username')
        self.Username.bind('<FocusIn>', on_enter)
        self.Username.bind('<FocusOut>', on_leave)

        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=107)

        #------------------------------- ///// OLD PASSWORD ENTRY ///// -----------------------------##

        def on_enter(e):
            self.old_password.delete(0,'end')

        def on_leave(name):
            name == self.old_password.get()
            if name=='':
                self.old_password.insert(0,'Old Password')

        self.old_password = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.old_password.place(x=30,y=150)
        self.old_password.insert(0,'Old Password')
        self.old_password.bind('<FocusIn>', on_enter)
        self.old_password.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=177)


        #------------------------------- ///// NEW PASSWORD ENTRY ///// -----------------------------##

        def on_enter(e):
            self.new_password.delete(0,'end')

        def on_leave(name):
            name == self.Username.get()
            if name=='':
                self.new_password.insert(0,'New Password')

        self.new_password = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.new_password.place(x=30,y=220)
        self.new_password.insert(0,'New Password')
        self.new_password.bind('<FocusIn>', on_enter)
        self.new_password.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=247)

        #--------------------------------- //// "CREATE" BUTTON ////-----------------------------------
            
        self.b1 = Button(self.frame,width =39,pady=7,text="Create",bg='#57a1f8',fg='white',border=0,command=self.updated_password).place(x=35,y=280)
        


        self.root.mainloop()

    def updated_password(self):
        if self.Username.get() == "":
            messagebox.showwarning("Alert!","Please enter the Username ")
        elif self.old_password.get()=="":
            messagebox.showwarning("Alert!","Please enter the Old Password")


        elif self.new_password.get() =="":
            messagebox.showwarning("Alert!","Please enter the new password again")
        else:
            username = self.Username.get()
            oldpassword = self.old_password.get()
            newPassword = self.new_password.get()
            previous_data = (
                username,
                oldpassword
            )
            updated_data = (
                newPassword,
                username
            )
            
            result = database.update_passwords(previous_data,updated_data)
            if result:
                messagebox.showinfo("Message"," Password updated")
                self.root.destroy()

                        
            else:
                messagebox.showerror("Alert!", "something went wrong")
            

if __name__ == "__main__":

    t = UpdatePass()
    t.update_passw_frame()

# auto-py-to-exe