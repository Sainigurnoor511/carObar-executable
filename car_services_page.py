from tkinter import *
from tkinter import Tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import database, mainpage, manage_database


class CarServicePage:

    def __init__(self,selected_Service=""):
        self.root = Toplevel()
        self.root.iconbitmap("resources/myIcon.ico")
        self.root.title("carObar -- Car Services")
        self.selectedService = selected_Service
        self.width_of_window = 900
        self.height_of_window = 450
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        
        self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)

        self.root.resizable(width=False, height=False)

        
        if self.selectedService:
            self.root.title("carObar -- Update Services")
        else:
            self.root.title("CarObar -- Services")  
                

    def car_services_page_widgets(self):
        
        self.frame = Frame(self.root, width=1000, height=700, background="white")
        self.frame.place(x=0, y=0)

        if self.selectedService: 
            self.heading = ttk.Label(self.frame, text=' Update Services', foreground='#57A1F8', font=('Harlow Solid Italic', 30, 'normal'))
            self.heading.place(x=350, y=5)
        else:
            self.heading = ttk.Label(self.frame, text='Services',background="white", foreground='#57A1F8', font=('Harlow Solid Italic', 40, 'normal'))
            self.heading.place(x=400, y=5)

        self.heading = ttk.Label(self.frame, text='* closed on Sunday', foreground='red')
        self.heading.place(x=705, y=175)

        #!_________________________________________________________________________________________________________


        self.customer_name = ttk.Label(self.frame,text='Customer Name', width=27,background="white", foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.customer_name.place(x=80, y=210)

        self.customer_name_entry = ttk.Entry(self.frame)
        self.customer_name_entry.place(x=80,y=250,width=200)

        self.customer_contact = ttk.Label(self.frame,text='Customer Contact', width=27,background="white", foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.customer_contact.place(x=398, y=210)

        self.customer_contact_entry = ttk.Entry(self.frame)
        self.customer_contact_entry.place(x=398,y=250,width=200)
        

        #!_________________________________________________________________________________________________________

        self.services_label = ttk.Label(self.frame,text='Select Service', width=27,background="white", foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.services_label.place(x=80, y=110)

        self.services_cb = ttk.Combobox(self.root, width=27)
        self.services_cb['values'] = (  ' Car Wash', 
                                        ' Repair', 
                                        ' Full Car Service')
        self.services_cb['state'] = 'readonly'
        self.services_cb.set("Select Service")
        self.services_cb.place(x=80, y=140)

        #!_________________________________________________________________________________________________________

        self.time_label = ttk.Label(self.frame,text='Select Time', width=27,background="white", foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.time_label.place(x=398, y=110)

        self.time_cb = ttk.Combobox(self.root, width=27)
        self.time_cb['values'] = ( '9:00 am - 11:00 am', 
                                    '11:00 am - 1:00 pm', 
                                    '1:00 pm - 3:00 pm',
                                    '3:00 pm - 5:00 pm')
        self.time_cb['state'] = 'readonly'
        self.time_cb.set("Select Time")
        self.time_cb.place(x=398, y=140)

        #!_________________________________________________________________________________________________________

        self.date_label = ttk.Label(self.frame,text='Select date',background="white", width=27, foreground='#57A1F8',font=('Harlow Solid Italic', 16, 'normal'))
        self.date_label.place(x=705, y=110)

        self.d = DateEntry(self.root)
        self.d.place(x=705,y=140)
        
        if self.selectedService:
            
            self.up = Button(self.root,width=12,text='Update',bg="#57A1F8",fg="white",command= self.get_services_update)
            self.up.place(x=420,y=350)

            result = dict(self.selectedService).get("values")
            print("Services detials - ", result)
            
            self.services_cb.set(result[0])
            self.time_cb.set(result[1])
            self.d.set_date(result[2])
            self.customer_name_entry.insert(0,result[3])
            self.customer_contact_entry.insert(0,result[4])

            

        else:    
            # self.book = Button(self.root,width=12,text='Book',bg="#57A1F8",fg="white",command= self.get_services_data)
            # self.book.place(x=420,y=350)

            self.s = ttk.Style()
            self.s.configure('my.TButton', font=('Bahnschrift SemiBold SemiConden', 16, 'bold'), background='white', foreground='#57A1F8')
            self.submit = ttk.Button(self.root, text='Book', style= "my.TButton", command= self.get_services_data)
            self.submit.place(x=420,y=355)
        
        #!_________________________________________________________________________________________________________

    def get_services_data(self):
        
        if self.services_cb.get() == "Select Service":
            messagebox.showwarning("Alert!","Please select the service")

        elif self.time_cb.get() == "Select Time" :
            messagebox.showwarning("Alert!","Please select time slot")

        elif self.d.get() == "":
            messagebox.showwarning("Alert!","Please Select the date") 

        elif self.customer_contact_entry.get()=="":
            messagebox.showwarning("Alert!","please enter the customer contact")     

        elif self.customer_name_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter the customer name")

        else:
            service =  self.services_cb.get()
            time = self.time_cb.get()
            Date_entry =  self.d.get()
            customerName = self.customer_name_entry.get()
            customerContact = self.customer_contact_entry.get()

            a = (service,time,Date_entry,customerName,customerContact)
        
            result = database.add_car_services_details(a)
            if result:
                    messagebox.showinfo("Message","Car Service detail added successfully")
                    self.root.destroy()
                    self.car_services_page_widgets()

                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")

    #!_________________________________________________________________________________________________________


    def get_services_update(self):
        
        if self.services_cb.get() == "Select Service":
            messagebox.showwarning("Alert!","Please select the service")

        elif self.time_cb.get() == "Select Time" :
            messagebox.showwarning("Alert!","Please select time slot")

        elif self.d.get() == "":
            messagebox.showwarning("Alert!","Please Select the date") 

        elif self.customer_contact_entry.get()=="":
            messagebox.showwarning("Alert!","please enter the customer contact")     

        elif self.customer_name_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter the customer name")

        else:
            service =  self.services_cb.get()
            time = self.time_cb.get()
            Date_entry =  self.d.get()
            customerName = self.customer_name_entry.get()
            customerContact = self.customer_contact_entry.get()

            b = (service,time,Date_entry,customerName,customerContact,dict(self.selectedService).get("text"))
        
            result = database.update_car_services_details(b)
            if result:
                    messagebox.showinfo("Message","Car Service detail updated successfully")
                    self.root.destroy()
                    v = manage_database.DisplayCars()
                    v.display_car_services()
                    v.button_frame()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")
    
    def open_home_page(self):
        self.root.destroy()


if __name__ == "__main__":
    cs = CarServicePage()
    cs.car_services_page_widgets()
    cs.root.mainloop()