from tkinter import *
from tkinter import messagebox
import win_10

drivelist = win_10.driveFetch()

def getSelectedRow(event):
    index=list1.curselection()[0]
    selected = list1.get(index)
    win_10.selectedValue(selected)


def command_servStart():
    msg = win_10.servStart()
    messagebox.showinfo('info',msg)

def command_servStop():
    msg = win_10.servStop()
    messagebox.showinfo('info',msg)  

def command_search():
    list1.delete(0,END)
    search = search_text.get()
    drivepath = droplist.get()
    if not search:
        messagebox.showinfo('error','input something in the search box')
    else:
        for row in win_10.search(search,drivepath + ":\\"):
            list1.insert(END,row)

window = Tk()
#window.geometry('750x250')
window.wm_title("Windows 10 100% Disk Solution")
window.configure(background="#746ca9")
#window.columnconfigure(0, weight=1)
#window.rowconfigure(0, weight=1)

label1 = Label(window,text="This Program will help you to activate and eacivate the window services which causes 100% disk utilization", fg="white",bg="#372982")
label1.grid(row=0,column=00,columnspan = 30)
"""label2= Label(window,text=" deacivate the window services which causes")
label2.grid(row=1,column=0)
label3=Label(window,text="100% disk utilization")
label3.grid(row=2,column=0)"""
label4 = Label(window,text = "Search for a file Name", fg="white",bg="#372982")
label4.grid(row = 3,column = 0)
label5 = Label(window,text="Drive", fg="white",bg="#372982")
label5.grid(row = 3, column = 2)

search_text = StringVar()
entry1=Entry(window,textvariable = search_text)
entry1.grid(row=3,column=1)

droplist = StringVar(window)
droplist.set(drivelist[0])
dropdown = OptionMenu(window,droplist,*drivelist)
dropdown.grid(row = 3,column = 3)


list1 = Listbox(window,height=10, width=100)
list1.grid(row=5, column = 0, columnspan = 20)
sb1=Scrollbar(window)
sb1.grid(row=5,column = 21, sticky='ns')
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',getSelectedRow)

startbutton = Button(window,text="Start Services", width=16, command=command_servStart, fg="white",bg="#372982")
startbutton.grid(row=0,column=31)
stopbutton = Button(window,text="Stop Services", width=16, command=command_servStop, fg="white",bg="#372982")
stopbutton.grid(row=1,column=31)
searchbutton= Button(window,text="Search",width = 16, command=command_search, fg="white",bg="#372982")
searchbutton.grid(row=3, column=31)

window.mainloop()
