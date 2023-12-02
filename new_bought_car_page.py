from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mainpage, manage_database, database

class BoughtCarPage:
    def __init__(self, selected_car=""):
        self.root = Tk()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Add Cars")
        self.width_of_window = 1000
        self.height_of_window = 600
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(False, False)
        
        self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)

        # Here we are getting the data from the parameter regarding
        # the selected car from the display car file
        self.selectedCar = selected_car

        if self.selectedCar:
            self.root.title("carObar -- Update Brand New Cars")
        else:
            self.root.title("carObar -- Buy Brand New Cars")
        

    def new_bought_car_page_widgets(self):

    ###---------------------------------/////// Brand New CAR DETAILS //////------------------------------###

        self.brand_new_frame = Frame(self.root, width=1000,height=1000, bg= "white")
        self.brand_new_frame.place(x=0,y=0)

        self.heading = ttk.Label(self.brand_new_frame, text='Brand New Cars', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 35, 'normal'))
        self.heading.place(x=350, y=0)

        self.title1 = ttk.Label(self.brand_new_frame, text=' Enter Car Details ', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 19, 'normal'))
        self.title1.place(x=400, y=110)

        self.car_brand = ttk.Label(self.brand_new_frame,text="Car Brand", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=90, y=190,width=180, height=30)

        self.car_brand_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_brand_entry.place(x =220,y =190,width =180,height=30)


        self.car_model = ttk.Label(self.brand_new_frame,text="Car Model", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_model.place(x=90,y=260,width=250, height=30)

        self.car_model_entry= ttk.Entry(self.brand_new_frame, font =20)
        self.car_model_entry.place(x =220,y =260,width =180,height=30)

        self.car_mileage = ttk.Label(self.brand_new_frame,text="Car Mileage",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_mileage.place(x=570,y=260,width=180, height=30)

        self.car_mileage_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_mileage_entry.place(x =720,y =260,width =180,height=30) 


        self.car_price = ttk.Label(self.brand_new_frame,text="Car Price",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_price.place(x=90,y=330,width=180, height=30)

        self.car_price_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_price_entry.place(x =220,y =330,width =180,height=30) 


        # -------------/////////  COMBOBOX //////////----------------#

        self.car_var = ttk.Label(self.brand_new_frame,text="Car Variant", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_var.place(x=570, y=190, width=180, height=30)

        variant =["Petrol","Diesel","Electric","Hybrid"]
        self.car_var_cb = ttk.Combobox(self.brand_new_frame, values=variant)
        self.car_var_cb.place(x=720, y=190, width=180, height=30)
        self.car_var_cb["state"]='readonly'
        self.car_var_cb.set("Select Variant")

        if self.selectedCar:

            self.s = ttk.Style()
            self.s.configure('my.TButton', font=('Bahnschrift SemiBold SemiConden', 18, 'bold'), background='white', foreground='#57A1F8')

            self.submit = ttk.Button(self.root, text='Submit', style= "my.TButton", command= self.get_updated_new_car_data)
            self.submit.place(x=450,y=520)

            result = dict(self.selectedCar).get("values")
            print("result")    


            self.car_brand_entry.insert(0,result[1])
            self.car_model_entry.insert(0,result[2])
            self.car_var_cb.set(result[3])
            self.car_mileage_entry.insert(0,result[4])
            self.car_price_entry.insert(0,result[5])

        else:
            self.s = ttk.Style()
            self.s.configure('my.TButton', font=('Bahnschrift SemiBold SemiConden', 18, 'bold'), background='white', foreground='#57A1F8')
            
            self.submit = ttk.Button(self.root, text='Submit', style= "my.TButton", command= self.get_updated_new_car_data)
            self.submit.place(x=420,y=520)

        self.root.mainloop()
        
        #------------------------------//////// GETTING CAR DATA ///////----------------------------###

    def get_new_car_data(self):

        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="Select Variant":
            messagebox.showwarning("Alert!","Please select variant")

        elif self.car_mileage_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter car mileage")

        elif self.car_price_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter car price")

        else:
            carBrand =  self.car_brand_entry.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            carMileage = self.car_mileage_entry.get()
            carPrice = self.car_price_entry.get()
            
            a = ("New", carBrand,carModel, carVariant,carMileage,carPrice)

            ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

            result = database.add_brand_new_cars(a)
            if result:
                    messagebox.showinfo("Message","Car details added successfully")
                    self.new_bought_car_page_widgets()
                    
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")


    def get_updated_new_car_data(self):
        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="Select Variant":
            messagebox.showwarning("Alert!","Please select variant")

        elif self.car_mileage_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter car mileage")

        elif self.car_price_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter car price")

        else:
            carBrand =  self.car_brand_entry.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            carMileage=self.car_mileage_entry.get()
            carPrice = self.car_price_entry.get()
            

            u = ("New", carBrand, carModel, carVariant,carMileage,carPrice, dict(self.selectedCar).get("text"))

            ###----------------------//////// CONNECTING WITH DATABASE ///////---------------------------###

            result = database.update_new_cars(u)
            if result:
                    messagebox.showinfo("Message","Car details updated successfully")
                    self.root.destroy()
                    bnc = manage_database.DisplayCars()
                    bnc.display_brand_new_cars()
                    bnc.button_frame()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")

    def open_home_page(self):
        self.root.destroy()
        n = mainpage.HomePage()
        n.homepage_widgets()

if __name__=="__main__":
    s=BoughtCarPage()
    s.new_bought_car_page_widgets()
    