from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mainpage, manage_database, database

class SellCarPage:
    def __init__(self, selected_car=""):
        self.root = Tk()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Sell Car")
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(width =False, height= False)

        self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)

        # Here we are getting the data from the parameter regarding
        # the selected car from the display car file
        self.selectedCar = selected_car

        if self.selectedCar:
            self.root.title("carObar -- Update Used Car")
        else:
            self.root.title("carObar -- Sell Car")
        

    def sellcar_page_widgets(self):

    ###---------------------------------/////// SELL CAR DETAILS //////------------------------------###

        self.sellcar_frame = Frame(self.root, width=1000,height=1000, bg= "white")
        self.sellcar_frame.place(x=0,y=0)

        self.heading = ttk.Label(self.sellcar_frame, text='Sell car', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 35, 'normal'))
        self.heading.place(x=420, y=0)

        self.title1 = ttk.Label(self.sellcar_frame, text='----- Enter Car Details -----', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 19, 'normal'))
        self.title1.place(x=370, y=90)

        self.car_brand = ttk.Label(self.sellcar_frame,text="Car Brand", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=90, y=160,width=180, height=30)

        self.car_brand_entry = ttk.Entry(self.sellcar_frame, font =20 )
        self.car_brand_entry.place(x =220,y =160,width =180,height=30)


        self.car_model = ttk.Label(self.sellcar_frame,text="Car Model", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_model.place(x=90,y=230,width=250, height=30)

        self.car_model_entry= ttk.Entry(self.sellcar_frame, font =20)
        self.car_model_entry.place(x =220,y =230,width =180,height=30)

        # -------------/////////  COMBOBOXES //////////----------------#

        self.car_reg = ttk.Label(self.sellcar_frame,text="Registration Year", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_reg.place(x=520,y=160,width =250,height=30)

        year =[2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990]
        self.car_reg_cb = ttk.Combobox(self.sellcar_frame, values=year)
        self.car_reg_cb.place(x=720, y=160, width=180, height=30)
        self.car_reg_cb["state"]='readonly'
        self.car_reg_cb.set("Select Year")


        self.car_var = ttk.Label(self.sellcar_frame,text="Car Variant", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_var.place(x=570, y=230, width=180, height=30)

        variant =["Petrol","Diesel","Electric","Hybrid"]
        self.car_var_cb = ttk.Combobox(self.sellcar_frame, values=variant)
        self.car_var_cb.place(x=720, y=230, width=180, height=30)
        self.car_var_cb["state"]='readonly'
        self.car_var_cb.set("Select Variant")


        self.car_ownership = ttk.Label(self.sellcar_frame,text="Car Owner", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_ownership.place(x=90,y=300,width=180,height=30)

        ownership =["1st owner","2nd owner","3rd owner","4th owner","5th owner"]
        self.car_ownership_cb = ttk.Combobox(self.sellcar_frame, values=ownership)
        self.car_ownership_cb.place(x =220,y =300,width =180,height=30)
        self.car_ownership_cb["state"]='readonly'
        self.car_ownership_cb.set("Select Ownership")


        self.km_driven = ttk.Label(self.sellcar_frame,text="Km Driven", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.km_driven.place(x=580,y=300,width =180,height=30)

        odometer =["0 km - 10,000 km","10,000 km - 20,000 km","20,000 km - 30,000 km","30,000 km - 40,000 km","40,000 km - 50,000 km","50,000 km - 60,000 km","60,000 km - 70,000 km","70,000 km - 80,000 km","80,000 km - 90,000 km","90,000 km - 1,00,000 km","1,00,000 km - 1,10,000 km"]
        self.km_driven_cb = ttk.Combobox(self.sellcar_frame, values=odometer)
        self.km_driven_cb.place(x =720,y =300,width =180,height=30)
        self.km_driven_cb["state"]='readonly'
        self.km_driven_cb.set("odometer")

      #####---------------------------///// SELLER DETAILS  //////--------------------------------------------#####

        self.title2_label = Label(self.sellcar_frame, text="----- Enter Seller Details -----",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 19, 'normal'))
        self.title2_label.place(x=360,y=380)


        self.seller_name = ttk.Label(self.sellcar_frame,text="Seller Name",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.seller_name.place(x=70,y=460,width=180, height=30)

        self.seller_name_entry = ttk.Entry(self.sellcar_frame, font =20 )
        self.seller_name_entry.place(x =220,y =460,width =180,height=30) 


        self.seller_address = ttk.Label(self.sellcar_frame,text="Seller Address",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.seller_address.place(x=50,y=540,width=180, height=30)

        self.seller_address_entry = ttk.Entry(self.sellcar_frame, font =20 )
        self.seller_address_entry.place(x =220,y =540,width =180,height=30) 


        self.seller_mobile = ttk.Label(self.sellcar_frame,text="Seller Contact No.",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.seller_mobile.place(x=520,y=460,width=180, height=30)

        self.seller_mobile_entry = ttk.Entry(self.sellcar_frame, font =20 )
        self.seller_mobile_entry.place(x =720,y =460,width =180,height=30)

        self.car_price = ttk.Label(self.sellcar_frame,text="Car Price",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_price.place(x=520,y=540,width=180, height=30)

        self.car_price_entry = ttk.Entry(self.sellcar_frame, font =20 )
        self.car_price_entry.place(x =720,y =540,width =180,height=30)

        if self.selectedCar:

            self.submit = Button(self.root,text='update',width=8,font=('Harlow Solid Italic', 12, 'bold'),bg="blue",fg="white",border=2,command= self.get_updated_sell_car_data)
            self.submit.place(x=450,y=635)

            result = dict(self.selectedCar).get("values")

            self.car_brand_entry.insert(0,result[1])
            self.car_model_entry.insert(0, result[2])
            self.car_var_cb.set(result[3])
            self.km_driven_cb.set(result[4])
            self.car_reg_cb.set(result[5])
            self.car_ownership_cb.set(result[6])
            
            self.seller_name_entry.insert(0, result[7])
            self.seller_mobile_entry.insert(0, result[8])
            self.seller_address_entry.insert(0, result[9])
            self.car_price_entry.insert(0, result[10])
            
        
        else:

            self.s = ttk.Style()
            self.s.configure('my.TButton', font=('Bahnschrift SemiBold SemiConden', 18, 'bold'), background='white', foreground='#57A1F8')
            self.submit = ttk.Button(self.root, text='Submit', style= "my.TButton", command= self.get_sell_car_data)
            self.submit.place(x=420,y=635)

        self.root.mainloop()
        
        #------------------------------//////// GETTING CAR DATA ///////----------------------------###

    def get_sell_car_data(self):

        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")

        elif self.car_reg_cb.get() =="Select Year":
            messagebox.showwarning("Alert!","Please select registration year")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="Select Variant":
            messagebox.showwarning("Alert!","Please select variant")
            
        elif self.car_ownership_cb.get() =="Select Ownership":
            messagebox.showwarning("Alert!","Please select car ownership")

        elif self.km_driven_cb.get() =="odometer":
            messagebox.showwarning("Alert!","Please select km driven")

        elif self.seller_name_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller name")

        elif self.seller_mobile_entry.get()=="":
            messagebox.showwarning("Alert!","Please enetr seller's contact number")

        elif self.seller_address_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller's address")

        elif self.car_price_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter car price")

        

        else:
            carBrand =  self.car_brand_entry.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            kmDriven= self.km_driven_cb.get()
            registrationYear = self.car_reg_cb.get()
            carOwnership = self.car_ownership_cb.get()
            sellerName = self.seller_name_entry.get()
            sellerContact=self.seller_mobile_entry.get()
            sellerAddress = self.seller_address_entry.get()
            carPrice =  self.car_price_entry.get()

            a = ("Used", carBrand,carModel, carVariant,kmDriven,registrationYear,carOwnership,sellerName, sellerContact,sellerAddress,carPrice)
            print(a)

            ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

            result = database.add_car_and_seller_details(a)
            if result:
                    messagebox.showinfo("Message","Car & Seller details added successfully")
                    self.sellcar_page_widgets()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")


    
    def get_updated_sell_car_data(self):

        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")

        elif self.car_reg_cb.get() =="Select Year":
            messagebox.showwarning("Alert!","Please select registration year")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="Select Variant":
            messagebox.showwarning("Alert!","Please select variant")
            
        elif self.car_ownership_cb.get() =="Select Ownership":
            messagebox.showwarning("Alert!","Please select car ownership")

        elif self.km_driven_cb.get() =="odometer":
            messagebox.showwarning("Alert!","Please select km driven")

        elif self.seller_name_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller name")

        elif self.seller_mobile_entry.get()=="":
            messagebox.showwarning("Alert!","Please enetr seller's contact number")

        elif self.seller_address_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller's address")

        elif self.car_price_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter car price")    

        else:
            carBrand =  self.car_brand_entry.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            kmDriven= self.km_driven_cb.get()
            carOwnership = self.car_ownership_cb.get()
            registrationYear = self.car_reg_cb.get()
            sellerName = self.seller_name_entry.get()
            sellerContact=self.seller_mobile_entry.get()
            sellerAddress = self.seller_address_entry.get()
            carPrice =  self.car_price_entry.get()


            u = ("Used", carBrand,carModel, carVariant,kmDriven,registrationYear,carOwnership,sellerName, sellerContact,sellerAddress,carPrice, dict(self.selectedCar).get("text"))

            print("Updated Sell car data - ", u)

            ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

            result = database.update_car_and_seller_details(u)
            if result:
                    messagebox.showinfo("Message","Car & Seller details updated successfully")
                    self.root.destroy()
                    suc = manage_database.DisplayCars()
                    suc.display_secondhand_cars_bought()
                    suc.button_frame()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")

    def open_home_page(self):
        self.root.destroy()
        n = mainpage.HomePage()
        n.homepage_widgets()

if __name__=="__main__":
    s = SellCarPage()
    s.sellcar_page_widgets()