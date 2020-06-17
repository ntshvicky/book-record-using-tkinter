"""
A program which store book information like,
Book name, ISBN, Year, Author
Users can Add,Update,Delete Books information
Users also can search all details or using basic details
"""
from tkinter import *
import backend

def view_command():
    listbox.delete(0,END)
    for row in backend.viewAll():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    for row in backend.viewSearched(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        listbox.insert(END,row)

def insert_command():
    if(title_text.get()!="" and author_text.get()!="" and year_text.get()!="" and isbn_text.get()!=""):
        backend.addBook(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        title_text.set("")
        author_text.set("")
        year_text.set("")
        isbn_text.set("")
        b1.focus()
        view_command()
    else:
        print("No valid data")

def get_selected_row(event):
    try:
        #index=listbox.curselection()//(0,) for first index
        index=listbox.curselection()[0] #0 for first index
        #listbox.get(index) //(1, 'The Book', 'Nitish', '2010', '0000-0001') for selected row
        #return listbox.get(index)[0] #1 for selected row 0 index contains primary key
        global selected_row
        selected_row = listbox.get(index)
        title_text.set(selected_row[1])
        author_text.set(selected_row[2])
        year_text.set(selected_row[3])
        isbn_text.set(selected_row[4])
    except IndexError:
        print("No selected row")



def delete_command():
    try:
        backend.deleteBook(selected_row[0])
        title_text.set("")
        author_text.set("")
        year_text.set("")
        isbn_text.set("")
        b1.focus()
        view_command()
    except NameError:
        print("No row selected for delete operation")

def update_command():
    if(title_text.get()!="" and author_text.get()!="" and year_text.get()!="" and isbn_text.get()!=""):
        backend.updateBook(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(), selected_row[0])
        title_text.set("")
        author_text.set("")
        year_text.set("")
        isbn_text.set("")
        b1.focus()
        view_command()
    else:
        print("No row selected for update operation")

window=Tk()

#create label
ltle = Label(window, text="Title")
ltle.grid(row=0,column=0)

laut = Label(window, text="Author")
laut.grid(row=0,column=2)

lyr = Label(window, text="Year")
lyr.grid(row=1,column=0)

lisbn = Label(window, text="ISBN")
lisbn.grid(row=1,column=2)

#create textbox
title_text=StringVar()
ttle = Entry(window, textvariable=title_text)
ttle.grid(row=0,column=1)

author_text=StringVar()
taut = Entry(window, textvariable=author_text)
taut.grid(row=0,column=3)

year_text=StringVar()
tyr = Entry(window, textvariable=year_text)
tyr.grid(row=1,column=1)

isbn_text=StringVar()
tisbn = Entry(window, textvariable=isbn_text)
tisbn.grid(row=1,column=3)

#Listbox contains book list
listbox=Listbox(window, height=6, width=35)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)
#bind list with function
listbox.bind('<<ListboxSelect>>', get_selected_row)

#scrollbar for listing
sb=Scrollbar(window)
sb.grid(row=2,column=2, rowspan=6)
#merge scrollbar with lisbox
listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

#Create Button for View All, Search Book, Add New, Update, Delete, and Close app
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Book", width=12, command=insert_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

view_command()
window.mainloop()