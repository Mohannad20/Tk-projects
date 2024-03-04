from customtkinter import *
from CTkListbox import *
from tkinter import messagebox

window = CTk()
window.geometry('350x600')
window.title('TODO-Lists')

def add():
    listbox.insert(END, entry.get())
    entry.delete(0,END)

def remove():
    try:
        selected_items = listbox.curselection()
        
        for i in reversed(selected_items):
            listbox.delete(i)
        if not selected_items:
            raise ValueError( "Nothing is selected" )
    except ValueError as e:
        messagebox.showerror(title="Error", message=str(e))

CTkLabel(window,
         text='TODO-Lists',
         font=('Poppins Black', 24),
         bg_color='#330a4c',
         text_color='#eed2ff',
         width=350,
         height=50).grid(row=0,columnspan=3)

listbox = CTkListbox(window,
                width=300,
                multiple_selection=True,
                height=380,
                corner_radius=10,
                border_width=1,
                border_color='#eed2ff',
                fg_color='#330a4c',
                text_color='#eed2ff',
                hover_color='#661499',
                highlight_color='grey')
listbox.grid(row=1, columnspan=3, pady=15)

entry = CTkEntry(window,
                 width=320,
                 height=45,
                 font=("Poppins Bold", 18),
                 corner_radius=20,
                 border_width=1,
                 placeholder_text='add a task',
                 placeholder_text_color='#661499',
                 border_color='#eed2ff',
                 fg_color='#330a4c',
                 text_color='#eed2ff')
entry.grid(row=9,columnspan=3, pady=10)

btn_add = CTkButton(window,
                    text="+ Add item",
                    font=("Poppins Black", 18),
                    fg_color='#330a4c',
                    border_width=0.7,
                    hover_color='#661499',
                    border_color='white',
                    text_color='#eed2ff',
                    corner_radius=40,
                    command=add)
btn_add.grid(row=10,column=1, pady=5)

btn_remove = CTkButton(window,
                       text="- Remove item",
                       font=("Poppins Black", 18),
                       fg_color='#330a4c',
                       border_width=0.7,
                       hover_color='#661499',
                       border_color='white',
                       text_color='#eed2ff',
                       corner_radius=40,
                       command=remove)
btn_remove.grid(row=10,column=2, pady=5)

window.mainloop()