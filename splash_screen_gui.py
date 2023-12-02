from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import mainpage, login_admin

w=Tk()
w.iconbitmap("resources/myIcon.ico")

#Using piece of code from old splash screen
width_of_window = 643
height_of_window = 400
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
# w.attributes("-alpha", 0.95)
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    la = login_admin.Login()
    la.login_frame()
    

Frame(w, width=643, height=400, bg='white').place(x=0,y=0)
# label1=Label(w, text='carObar', fg='#2F60D8', bg='#272727')
# label1.configure(font=("Harlow Solid Italic", 40, "bold"))
# label1.place(x=115,y=70)

image_path = Image.open('resources/Picture1.png')
imgTk = ImageTk.PhotoImage(image_path)
image_label = Label(w, image=imgTk)
image_label.place(x=0, y=0)

label2=Label(w, text= "LOADING.....", fg='black', bg='white') #decorate it 
label2.configure(font=("ADLaM Display", 16, "bold"))
label2.place(x=10,y=360)

#making animation
image_a=ImageTk.PhotoImage(Image.open('images\splashscreen\c1.png'))
image_b=ImageTk.PhotoImage(Image.open('images\splashscreen\c2.png'))


for i in range(2): #4loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=280, y=370)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=370)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=320, y=370)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=340, y=370)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=370)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=300, y=370)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=320, y=370)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=340, y=370)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=370)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=370)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=320, y=370)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=340, y=370)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=370)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=300, y=370)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=320, y=370)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=340, y=370)
    w.update_idletasks()
    time.sleep(0.4)

w.destroy()
new_win()
w.mainloop()