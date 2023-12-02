from tkinter import *
from tkinter import ttk, messagebox
import database, new_bought_car_page, car_services_page, sell_car_page, mainpage

class DisplayCars:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Manage Database")
        self.width_of_window = 1200
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        # self.root.resizable(False,False)
        self.root.title("carObar -- Manage Database")

        self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   BUTTON FRAME   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    

    def button_frame(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20, y=10, width=1160, height=120)

        self.database1 = ttk.Button(self.f,width=32, text='Manage Brand-new Cars Bought',command=self.display_brand_new_cars)
        self.database1.place(x=30, y=25)

        self.database2 = ttk.Button(self.f, width=32, text='Manage Second-hand Cars Bought', command = self.display_secondhand_cars_bought)
        self.database2.place(x=30, y=70)

        self.database3 = ttk.Button(self.f, width=24, text='Manage In Stock Cars',command = self.display_in_stock_cars)
        self.database3.place(x=290, y=25)

        self.database4 = ttk.Button(self.f, width=24, text='Manage Cars Sold', command= self.display_sold_cars)
        self.database4.place(x=290, y=70)

        self.database5 = ttk.Button(self.f, width=24, text='Manage Car Services', command=self.display_car_services)
        self.database5.place(x=500, y=25)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     BRAND NEW CARS TREEVIEW      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_brand_new_cars(self):

        
        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=535)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I"))

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", width=80, anchor=CENTER)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", width=120, anchor=CENTER)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", width=120, anchor=CENTER)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", width=120, anchor=CENTER)

        self.tree_view.heading("#5",text="MILEAGE")
        self.tree_view.column("#5", width=150, anchor=CENTER)

        self.tree_view.heading("#6",text="PRICE")
        self.tree_view.column("#6", width=100, anchor=CENTER)

        self.tree_view.heading("#7",text="DELETE")
        self.tree_view.column("#7", width=100, anchor=CENTER)

        self.tree_view.heading("#8",text="UPDATE")
        self.tree_view.column("#8", width=100, anchor=CENTER)

        self.tree_view.heading("#9",text="ADD IN STOCK")
        self.tree_view.column("#9", width=150, anchor=CENTER)
        

        for i in database.get_brand_new_cars():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5],i[6], "Delete", "Update","Add In Stock"))
        self.tree_view.bind("<Double-Button-1>", self.perform_action1)  

        vertical_scrollbar = ttk.Scrollbar(self.f, orient=VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=1128, y=21, height=498)

        horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.place(x=16, y=501, width=1115)
        
        self.tree_view.place(x=15,y=20,width=1130,height=500)

    def perform_action1(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#7":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_brand_new_cars(d)
                if result:
                    messagebox.showinfo("Message","Car data deleted successfully")
                    self.root.destroy()
                    v = DisplayCars()
                    v.display_brand_new_cars()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#8":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = new_bought_car_page.BoughtCarPage(self.tree_view.item(r))
                self.root.destroy()
                s.new_bought_car_page_widgets()

        elif column_id == "#9":
            new_car_data = self.tree_view.item(r)
            print("New Car Data - ", new_car_data)

            car_details = new_car_data.get("values")
            print("Car Details - ", car_details)

            add_in_stock_result = database.add_in_stock(
                (
                    car_details[0],
                    car_details[1],
                    car_details[2],
                    car_details[3],
                    car_details[4],
                    "0 KM",
                    "XXXX",
                    "N/A",
                    car_details[5],
                    "NO"
                )
            )

            if add_in_stock_result:
                messagebox.showinfo("Meesage","Car added in the stock")
            else:
                messagebox.showwarning("Alert!","Something went wrong")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      SECOND-HAND CARS BOUGHT      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_secondhand_cars_bought(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=535)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I","J","K","L","M","N"), selectmode= EXTENDED)

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", anchor=CENTER,width=80)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", anchor=CENTER,width=120)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", anchor=CENTER,width=120)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", anchor=CENTER,width=120)

        self.tree_view.heading("#5",text="KMS DRIVEN")
        self.tree_view.column("#5", anchor=CENTER,width=160)

        self.tree_view.heading("#6",text="REGISTRATION YEAR")
        self.tree_view.column("#6", anchor=CENTER,width=150)

        self.tree_view.heading("#7",text="OWNERSHIP")
        self.tree_view.column("#7", anchor=CENTER,width=120)

        self.tree_view.heading("#8",text="SELLER NAME")
        self.tree_view.column("#8", anchor=CENTER,width=100)

        self.tree_view.heading("#9",text="SELLER CONTACT")
        self.tree_view.column("#9", anchor=CENTER,width=120)

        self.tree_view.heading("#10",text="SELLER ADDRESS")
        self.tree_view.column("#10", anchor=CENTER,width=200)

        self.tree_view.heading("#11",text="PRICE")
        self.tree_view.column("#11", anchor=CENTER,width=100)

        self.tree_view.heading("#12",text="DELETE")
        self.tree_view.column("#12", anchor=CENTER,width=100)

        self.tree_view.heading("#13",text="UPDATE")
        self.tree_view.column("#13", anchor=CENTER,width=110)

        self.tree_view.heading("#14",text="ADD IN STOCK")
        self.tree_view.column("#14", anchor=CENTER,width=150)
        

        for i in database.get_car_and_seller_details():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9],i[10],i[11], "Delete", "Update","Add In Stock"))
        self.tree_view.bind("<Double-Button-1>", self.perform_actions2)    

        vertical_scrollbar = ttk.Scrollbar(self.f, orient=VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=1128, y=21, height=498)

        horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.place(x=16, y=501, width=1115)
        
        self.tree_view.place(x=15,y=20,width=1130,height=500)

    def perform_actions2(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#12":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_car_and_seller_details(d)
                if result:
                    messagebox.showinfo("Message","Car data deleted successfully")
                    self.root.destroy()
                    v = DisplayCars()
                    v.display_secondhand_cars_bought()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#13":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = sell_car_page.SellCarPage(self.tree_view.item(r))
                self.root.destroy()
                s.sellcar_page_widgets()
        elif column_id == "#14":
            second_hand_car_detials = self.tree_view.item(r)

            scar_details = second_hand_car_detials.get("values")
            print("Second Hand Car Details - ", scar_details)

            second_hand_car_add_result = database.add_second_hand_car_in_stock(
                (
                    scar_details[0],
                    scar_details[1],
                    scar_details[2],
                    scar_details[3],
                    "N/A",
                    scar_details[4],
                    scar_details[5],
                    scar_details[6],
                    scar_details[10],
                    "NO"
                )
            )

            if second_hand_car_add_result:
                messagebox.showinfo("Message","Car added in the stock")
            else:
                messagebox.showwarning("Alert!","Something went wrong")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    IN STOCK CARS TREEVIEW    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_in_stock_cars(self):
        
        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=535)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I","J","K"))

        self.tree_view.heading("#0", text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", width=80, anchor=CENTER)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", width=120, anchor=CENTER)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", width=120, anchor=CENTER)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", width=120, anchor=CENTER)

        self.tree_view.heading("#5",text="MILEAGE")
        self.tree_view.column("#5", width=150, anchor=CENTER)

        self.tree_view.heading("#6",text="KMS DRIVEN")
        self.tree_view.column("#6", width=160, anchor=CENTER)

        self.tree_view.heading("#7",text="REGISTRATION YEAR")
        self.tree_view.column("#7", width=150, anchor=CENTER)

        self.tree_view.heading("#8",text="OWNERSHIP")
        self.tree_view.column("#8", width=120, anchor=CENTER)

        self.tree_view.heading("#9",text="PRICE")
        self.tree_view.column("#9", width=100, anchor=CENTER)

        self.tree_view.heading("#10",text="CAR SOLD STATUS")
        self.tree_view.column("#10", width=100, anchor=CENTER)
        
        self.tree_view.heading("#11",text="SOLD CAR")
        self.tree_view.column("#11", width=100, anchor=CENTER)

        for i in database.manage_cars_stock():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], "Sold Car"))
        self.tree_view.bind("<Double-Button-1>", self.perform_action3)    

        vertical_scrollbar = ttk.Scrollbar(self.f, orient=VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=1128, y=21, height=498)

        horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.place(x=16, y=501, width=1115)
        
        self.tree_view.place(x=15,y=20,width=1130,height=500)

    def perform_action3(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#11":
            confirmation = messagebox.askyesno("Alert!","Do you really want to sell this car?")
            if confirmation:
                result = database.sold_car(
                    (
                        "YES",
                        d[0]
                        )
                    )
                if result:
                    messagebox.showinfo("Message","Car sold successfully")
                    self.root.quit()
                    v = DisplayCars()
                    v.display_in_stock_cars()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    SOLD CARS TREEVIEW    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_sold_cars(self):
        
        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=535)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I","J"))

        self.tree_view.heading("#0", text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", width=80, anchor=CENTER)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", width=120, anchor=CENTER)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", width=120, anchor=CENTER)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", width=120, anchor=CENTER)

        self.tree_view.heading("#5",text="MILEAGE")
        self.tree_view.column("#5", width=150, anchor=CENTER)

        self.tree_view.heading("#6",text="KMS DRIVEN")
        self.tree_view.column("#6", width=140, anchor=CENTER)

        self.tree_view.heading("#7",text="REGISTRATION YEAR")
        self.tree_view.column("#7", width=150, anchor=CENTER)

        self.tree_view.heading("#8",text="OWNERSHIP")
        self.tree_view.column("#8", width=120, anchor=CENTER)

        self.tree_view.heading("#9",text="PRICE")
        self.tree_view.column("#9", width=100, anchor=CENTER)

        self.tree_view.heading("#10",text="CAR SOLD STATUS")
        self.tree_view.column("#10", width=160, anchor=CENTER)

        for i in database.show_all_sold_cars_details():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        # self.tree_view.bind("<Double-Button-1>", self.perform_action4)    

        vertical_scrollbar = ttk.Scrollbar(self.f, orient=VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=1128, y=21, height=498)

        horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.place(x=16, y=501, width=1115)
        
        self.tree_view.place(x=15,y=20,width=1130,height=500)

    # def perform_action4(self, e):
    #     # Focus Row 
    #     r = self.tree_view.focus()
    #     print(r)

    #     # Get the column id
    #     column_id = self.tree_view.identify_column(e.x)
    #     print("Column ID - ", column_id)

    #     # Get the data from the row according to the focused row
    #     d = self.tree_view.item(r)
    #     print("Focused Row - ", d)

    #     car_id = d.get("text")
    #     print("Car ID - ", car_id)
    #     d = (car_id,)

    #     if column_id == "#11":
    #         confirmation = messagebox.askyesno("Alert!","Do you really want to sell this car?")
    #         if confirmation:
    #             result = database.sold_car(
    #                 (
    #                     "YES",
    #                     d[0]
    #                     )
    #                 )
    #             if result:
    #                 messagebox.showinfo("Message","Car sold successfully")
    #                 self.root.quit()
    #                 v = DisplayCars()
    #                 v.display_in_stock_cars()
    #                 v.button_frame()
                    
    #             else:
    #                 messagebox.showwarning("Alert!","Something went wrong")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      CAR SERVICES          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_car_services(self):
        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=535)

        self.tree_view = ttk.Treeview(self.f, columns= ("A","B","C","D","E","F","G"))

        self.tree_view.heading("#0", text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1", text="SERVICE TYPE")
        self.tree_view.column("#1", width= 140, anchor=CENTER)

        self.tree_view.heading("#2", text="SERVICE TIME")
        self.tree_view.column("#2", width= 170, anchor=CENTER)

        self.tree_view.heading("#3",text= "SERVICE DATE")
        self.tree_view.column("#3", width= 150, anchor=CENTER)

        self.tree_view.heading("#4",text= "CUSTOMER NAME")
        self.tree_view.column("#4", width= 180, anchor=CENTER)

        self.tree_view.heading("#5",text= "CUSTOMER CONTACT")
        self.tree_view.column("#5", width= 160, anchor=CENTER)

        self.tree_view.heading("#6",text= "DELETE")
        self.tree_view.column("#6", width= 120, anchor=CENTER)

        self.tree_view.heading("#7",text= "UPDATE")
        self.tree_view.column("#7", width= 120, anchor=CENTER)


        for i in database.get_car_services_details():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Delete","Update"))

        self.tree_view.bind("<Double-Button-1>", self.perform_action5)

        vertical_scrollbar = ttk.Scrollbar(self.f, orient=VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(x=1127, y=21, height=498)

        horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.place(x=16, y=501, width=1115)
        
        self.tree_view.place(x=15,y=20,width=1130,height=500)

    def perform_action5(self,e):
        
        #Focus Row
        r = self.tree_view.focus()
        print(r)

        #Get column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        #Get the data from the row acording to the focused row

        d = self.tree_view.item(r)
        print("Focused Row - ",d)


        service_id = d.get("text")
        print("Service Id - ",service_id)
        d =(service_id,)


        if column_id =="#6":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete")
            if confirmation:
                result = database.delete_car_services_data(d)
                if result:
                    messagebox.showinfo("Message","Sevices data deleted successfully")
                    self.display_car_services()
                    
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")
        
        elif column_id == "#7":
            a = car_services_page.CarServicePage(self.tree_view.item(r))
            self.root.destroy()
            a.car_services_page_widgets()    
            

    def open_home_page(self):
        self.root.destroy()
        n = mainpage.HomePage()
        n.homepage_widgets()
        n.open_sidebar()
        n.open_dashboard() 

if __name__=="__main__":
    v = DisplayCars()
    v.button_frame()
    v.root.mainloop()