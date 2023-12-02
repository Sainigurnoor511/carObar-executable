from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import buy_car_page, sell_car_page, new_bought_car_page, car_services_page, manage_database, update_password, invoice_generator


class HomePage:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title('carObar')
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(width =False, height= False)
        self.root.overrideredirect(1)


    #######################################       HOMEPAGE       ##################################################
    
    def homepage_widgets(self):
        # Main Frame
        self.mainframe = Frame(self.root, width=1000, height=700, background="white")
        self.mainframe.place(x=0, y=0)

        self.image_path = Image.open('images/background.jpg').resize((1000,564))
        self.image = ImageTk.PhotoImage(self.image_path)
        self.background_pic = ttk.Label(self.mainframe, image=self.image)
        self.background_pic.place(x=-2, y=136)

        self.heading = ttk.Label(self.mainframe, text='Welcome Administrator !', foreground='#1C1C1C', background="white", font=('Bahnschrift SemiCondensed', 35, 'normal'))
        self.heading.place(x=280, y=30)

        self.image_path = Image.open('images/mainpage/sidebar.png').resize((45,45))
        self.sidebar_image = ImageTk.PhotoImage(self.image_path)
        self.sidebar_button = Button(self.mainframe, image= self.sidebar_image, border=0, background="white", command= self.open_sidebar)
        self.sidebar_button.place(x=10,y=35)


        self.image_path = Image.open('images/mainpage/user.png').resize((45,45))
        self.user_image = ImageTk.PhotoImage(self.image_path)
        self.user_label = Label(self.mainframe, image=self.user_image, background= "white")
        self.user_label.place(x=940, y=35)

        self.context_menu = Menu(self.mainframe, tearoff=0)
        self.context_menu.add_command(label="Update Password", command=self.menu_action)

        # Bind the context menu to the label widget
        self.user_label.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self,event):
            self.context_menu.post(event.x_root, event.y_root)

    def menu_action(self):
            up = update_password.UpdatePass()
            up.update_passw_frame()

        
    #######################################     SIDEBAR MENU     ##################################################

    def open_sidebar(self):
        # Sidebar/Menubar for accessing different windows
        self.sidebar_frame = Frame(self.root, height=700, width=200, background= 'black')
        self.sidebar_frame.place(x=0, y=0)

        self.heading = ttk.Label(self.sidebar_frame, text='carObar', foreground='white',background="black", font=('Magneto', 23, 'normal'))
        self.heading.place(x=40, y=30)

        self.image_path = Image.open('images/mainpage/back.png').resize((20,20))
        self.back_image = ImageTk.PhotoImage(self.image_path)
        self.back_button = Button(self.sidebar_frame, image= self.back_image, border=0,borderwidth=0, background="black",command= self.close_sidebar)
        self.back_button.place(x=10,y=42)

        self.image_path = Image.open('images/mainpage/dashboard.png').resize((150,30))
        self.dashboard_image = ImageTk.PhotoImage(self.image_path)
        self.dashboard_button = Button(self.sidebar_frame, image= self.dashboard_image, border=0, background="black", command= self.open_dashboard)
        self.dashboard_button.place(x=25,y=150)

        self.image_path = Image.open('images/mainpage/buycar.png').resize((150,30))
        self.buycar_image = ImageTk.PhotoImage(self.image_path)
        self.buycar_button = Button(self.sidebar_frame, image= self.buycar_image, border=0, background="black", command= self.open_buycar)
        self.buycar_button.place(x=25,y=200)

        self.image_path = Image.open('images/mainpage/sellcar.png').resize((150,30))
        self.sellcar_image = ImageTk.PhotoImage(self.image_path)
        self.sellcar_button = Button(self.sidebar_frame, image= self.sellcar_image, border=0, background="black", command= self.open_sellcar)
        self.sellcar_button.place(x=25,y=250)

        self.image_path = Image.open('images/mainpage/services.png').resize((150,30))
        self.services_image = ImageTk.PhotoImage(self.image_path)
        self.services_button = Button(self.sidebar_frame, image= self.services_image, border=0, background="black", command= self.open_car_services)
        self.services_button.place(x=26,y=300)

        self.image_path = Image.open('images\mainpage\exit.png').resize((80,35))
        self.exit_image = ImageTk.PhotoImage(self.image_path)
        self.exit_button = Button(self.sidebar_frame, image= self.exit_image, border=0, background="black", command=self.exit_button)
        self.exit_button.place(x=33,y=350)


    def close_sidebar(self):
        self.sidebar_frame.destroy()


    ##################################     SIDEBAR MENU ITEMS     #################################################
    
    def open_dashboard(self):
        self.dashboard_frame = Frame(self.root, width=1000, height=700, background="white")
        self.dashboard_frame.place(x=0, y=100)
        self.close_sidebar()
        # self.open_sidebar()
        

        self.image_path = Image.open('images/mainpage/sidebar.png').resize((40,40))
        self.sidebar_image = ImageTk.PhotoImage(self.image_path)
        self.sidebar_button = Button(self.mainframe, image= self.sidebar_image, border=0, background="white", command= self.open_sidebar)
        self.sidebar_button.place(x=10,y=35)

        self.image_path = Image.open('images/mainpage/dashboard_buttons.png')
        self.dashboard_buttons_image = ImageTk.PhotoImage(self.image_path)
        self.dashboard_buttons = ttk.Label(self.dashboard_frame,image=self.dashboard_buttons_image, background="white")
        self.dashboard_buttons.place(x=10,y=50)

        self.image_path = Image.open('images/mainpage/graph.png').resize((478,400))
        self.graph_img = ImageTk.PhotoImage(self.image_path)
        self.graph_image = ttk.Label(self.dashboard_frame,image=self.graph_img, background="white")
        self.graph_image.place(x=520,y=195)

        self.dashboard_buttons_label1 = ttk.Label(self.dashboard_frame,text= "₹ 2.5 cr", foreground='#01FB09', background="white", font=('Montserrat Medium', 16, 'bold'))
        self.dashboard_buttons_label1.place(x=42,y=80)

        self.dashboard_buttons_label2 = ttk.Label(self.dashboard_frame,text= "926", foreground='#FE0101', background="white", font=('Montserrat Medium', 16, 'bold'))
        self.dashboard_buttons_label2.place(x=325,y=80)

        self.dashboard_buttons_label2_5 = ttk.Label(self.dashboard_frame,text= "👁", foreground='#FE0101', background="white", font=('Montserrat Medium', 18, 'normal'))
        self.dashboard_buttons_label2_5.place(x=290,y=78)

        self.dashboard_buttons_label3 = ttk.Label(self.dashboard_frame,text= "10", foreground='#FFCF00', background="white", font=('Montserrat Medium', 25, 'bold'))
        self.dashboard_buttons_label3.place(x=546,y=70)

        self.dashboard_buttons_label4 = ttk.Label(self.dashboard_frame,text= "10", foreground='#0079C6', background="white", font=('Montserrat Medium', 25, 'bold'))
        self.dashboard_buttons_label4.place(x=799,y=70)


        self.s = ttk.Style()
        self.s.configure('my.TButton', font=('Montserrat', 22, 'bold'), width= 18, background='white', foreground='#57A1F8')


        self.new_bought_car_button = ttk.Button(self.root, text='Add New Cars', style= "my.TButton", command= self.open_new_bought_car)
        self.new_bought_car_button.place(x=60,y=340)


        self.manage_database_button = ttk.Button(self.root, text='Manage Database', style= "my.TButton", command= self.open_manage_database)
        self.manage_database_button.place(x=60,y=400)


        self.generate_invoice_button = ttk.Button(self.root, text='Generate Invoice', style= "my.TButton", command= self.open_invoice_generator)
        self.generate_invoice_button.place(x=60,y=460)



        # self.image_path = Image.open('images/mainpage/manage_database.png').resize((300, 50))
        # self.manage_database_image = ImageTk.PhotoImage(self.image_path)
        # self.manage_database_button = Button(self.dashboard_frame, image= self.manage_database_image, background= "white", border=0, command= self.open_manage_database)
        # self.manage_database_button.place(x=40,y=200)

        # self.image_path = Image.open('images/mainpage/add_brandnew_cars.png').resize((305, 45))
        # self.new_bought_car_image = ImageTk.PhotoImage(self.image_path)
        # self.new_bought_car_button = Button(self.dashboard_frame, image= self.new_bought_car_image,background= "white", border=0, command= self.open_new_bought_car)
        # self.new_bought_car_button.place(x=37,y=273)

        # self.image_path = Image.open('images/mainpage/generate_invoice.png').resize((301, 52))
        # self.generate_invoice_image = ImageTk.PhotoImage(self.image_path)
        # self.generate_invoice_button = Button(self.dashboard_frame, image= self.generate_invoice_image, background= "white",  border=0, command= self.open_invoice_generator)
        # self.generate_invoice_button.place(x=40,y=340)

    def open_buycar(self):
        self.root.destroy()
        bc = buy_car_page.BuyCarPage()
        
    def open_sellcar(self):
        self.root.destroy()
        sc = sell_car_page.SellCarPage()
        sc.sellcar_page_widgets()

    def open_car_services(self):
        # self.root.destroy()
        cs = car_services_page.CarServicePage()
        cs.car_services_page_widgets()

    def open_manage_database(self):
        self.root.destroy()
        db = manage_database.DisplayCars()
        db.button_frame()

    def open_new_bought_car(self):
        self.root.destroy()
        nb = new_bought_car_page.BoughtCarPage()
        nb.new_bought_car_page_widgets()

    def open_invoice_generator(self):
        ig = invoice_generator.InvoiceGenerator()
        ig.widgets()
        

    def exit_button(self):
        self.root.destroy()

if __name__ == '__main__':
    hm = HomePage()
    hm.homepage_widgets()
    hm.root.mainloop()