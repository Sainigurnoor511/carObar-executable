from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import update_password
import database, mainpage

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Login Screen")
        self.width_of_window = 900
        self.height_of_window = 450
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.configure(bg ='#fff')
        self.root.title("carObar -- Login Page")
        self.root.resizable(width =False, height= False)
        self.root.bind('<Return>', self.log_in)
        

    def login_frame(self):
        self.image_path = Image.open('images/mainpage/main5.png').resize((350,300))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.imgTk, width=350, height=300,bg='white')
        self.image_label.place(x=50, y=80)
        

        self.frame = Frame(self.root,width=350,height=350,bg='white')
        self.frame.place(x=480,y=70)

        self.heading = Label(self.frame,text ='Log in' , fg='#57a1f8',bg = 'white',font=('Microsoft YaHei UI Light',18,'bold'))
        self.heading.place(x=130,y=5)
        #------------------------------------------------------------
    
        def on_enter(e):
            self.user.delete(0,'end')

        def on_leave(name):
            name == self.user.get()
            if name=='':
                self.user.insert(0,'Username')

        def go_to_next_element(event):
            event.widget.tk_focusNext().focus()
                
        self.user = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30,y=80)
        self.user.insert(0,'Username')
        self.user.bind('<Return>', go_to_next_element)
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=107)

        #---------------------------------------------------------

        def on_enter(e):
            self.passwd.delete(0,'end')

        def on_leave(name):
            name == self.user.get()
            if name=='':
                self.passwd.insert(0,'Password')

        def go_to_next_element(event):
            event.widget.tk_focusNext().focus()

        self.passwd = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11),show="*")
        self.passwd.place(x=30,y=150)
        self.passwd.insert(0,'Password')
        self.user.bind('<Return>', go_to_next_element)
        self.passwd.bind('<FocusIn>', on_enter)
        self.passwd.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=177)

        #------------------------------------------------------------

        self.b1 = Button(self.frame,width =39,pady=7,text="Sign in",bg='#57a1f8',fg='white',border=0, command=self.log_in).place(x=35,y=204)
        

        # self.sign_up = Button(self.frame,width=20,text='Forgot password?', border=0,bg='white',cursor='hand1',fg='#57a1f8')#,command=self. open_update_password_window
        # self.sign_up.place(x=195,y=250)


        self.root.mainloop()

    def log_in(self):
            
            if self.user.get() == "": 
                messagebox.showwarning("Alert!","Please enter the username")

            elif self.passwd.get() =="":
                messagebox.showwarning("Alert!","Please enter the password")

            else:
            
                Username = self.user.get()
                password = self.passwd.get()

                a = (Username,password)

                result = database.register_data(a)    
                if result:
                            
                        # messagebox.showinfo("Message"," Logged in")
                        self.root.destroy()
                        np = mainpage.HomePage()
                        np.homepage_widgets()
                        
                else:

                    messagebox.showerror("Alert!", "Incorrect username & password")

        
        

    # def open_update_password_window(self):
    
    #     self.root.destroy()
    #     up = update_password.UpdatePass()
    #     up.update_passw_frame()


if __name__ == "__main__":
    t = Login()
    t.login_frame()