##simple program which get data of cars form user with GUI and save it on csv file.
from csv import *
from tkinter import *
from tkinter import messagebox


window=Tk()
window.title("Cars data entry")
main_lst=[]

def Add():
    lst=[name.get(),year.get(),km.get(),phoneNumber.get(),place.get()
        ,price.get(),hand.get()]
    main_lst.append(lst)
    messagebox.showinfo("Information","The data has been added successfully")

def Save():
    with open("data_entry.csv","w") as file:
        Writer=writer(file)
        Writer.writerow(["Car Name","Year","KM","Phone number","Place","Price","Hand"])
        Writer.writerows(main_lst)
        messagebox.showinfo("Information","Saved successfully")

def Clear():
    name.delete(0,END)
    year.delete(0,END)
    km.delete(0,END)
    phoneNumber.delete(0, END)
    place.delete(0,END)
    price.delete(0,END)
    hand.delete(0,END)

label1=Label(window,text="Car Name: ",padx=20,pady=10)
label2=Label(window,text="Year: ",padx=20,pady=10)
label3=Label(window,text="KM: ",padx=20,pady=10)
label4=Label(window,text="Phone number: ",padx=20,pady=10)
label5=Label(window,text="Place: ",padx=20,pady=10)
label6=Label(window,text="Price: ",padx=20,pady=10)
label7=Label(window,text="Hand: ",padx=20,pady=10)
name=Entry(window,width=30,borderwidth=5)
year=Entry(window,width=30,borderwidth=5)
km=Entry(window,width=30,borderwidth=5)
phoneNumber=Entry(window,width=30,borderwidth=5)
place=Entry(window,width=30,borderwidth=5)
price=Entry(window,width=30,borderwidth=5)
hand=Entry(window,width=30,borderwidth=5)
save=Button(window,text="Save",padx=20,pady=10,command=Save)
add=Button(window,text="Add",padx=20,pady=10,command=Add)
clear=Button(window,text="Clear",padx=18,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)
label6.grid(row=5,column=0)
label7.grid(row=6,column=0)
name.grid(row=0,column=1)
year.grid(row=1,column=1)
km.grid(row=2,column=1)
phoneNumber.grid(row=3,column=1)
place.grid(row=4,column=1)
price.grid(row=5,column=1)
hand.grid(row=6,column=1)
save.grid(row=8,column=0,columnspan=2)
add.grid(row=7,column=0,columnspan=2)
clear.grid(row=9,column=0,columnspan=2)
Exit.grid(row=10,column=0,columnspan=2)

window.mainloop()
