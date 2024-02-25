from customtkinter import *
from tkinter import ttk,messagebox, filedialog
from tkinter import * 
from fpdf import FPDF
import csv
import json
import sqlite3

w = CTk()
w.geometry('1150x530')
w.title('Patienten Management')
set_appearance_mode('dark')
CTkLabel(master=w, width=1150, height=40, text='Patientenmanagement bei Dr.Jinazi', fg_color='black',
         font=('calibri', 25, 'bold')).place(x=0, y=0)

conn = sqlite3.connect('patient_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        matricule TEXT,
        nom TEXT,
        prenom TEXT,
        age INTEGER,
        adresse TEXT,
        telephone TEXT,
        remarque TEXT
    )
''')
conn.commit()
# conn.close()

# import data
def import_data():
    file_path = filedialog.askopenfilename(filetypes=[('SQLite Database Files', '*.db')])
    if file_path:
        conn_import = sqlite3.connect(file_path)
        cursor_import = conn_import.cursor()

        cursor_import.execute('SELECT * FROM patients')
        data = cursor_import.fetchall()

        for row in data:
            tree.insert('', 'end', values=row)
        messagebox.showinfo("Erfolgreich", "Daten erfolgreich importiert!")
        conn_import.close()

# export data to a csv file
def export_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Id', 'Vorname', 'Nachname', 'Alter', 'Adresse', 'Telephon', 'Hinweis'])
            for child in tree.get_children():
                data = tree.item(child, 'values')
                csvwriter.writerow(data)
        messagebox.showinfo("Erfolgreich", "Datenexport nach CSV erfolgreich!")

# export data to a text file
def export_to_txt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as txtfile:
            for child in tree.get_children():
                data = tree.item(child, 'values')
                txtfile.write('\t'.join(map(str, data)) + '\n')
        messagebox.showinfo("Erfolgreich", "Datenexport nach TXT erfolgreich!")


# export data to a pdf file
def export_to_pdf():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF Files', '*.pdf')])
    if file_path:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(family="Arial", size=10)

        # conn = sqlite3.connect('patient_data.db')
        # cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        patienten = cursor.fetchall()

    for patient in patienten:
            pdf.cell(200, 10, txt=f"ID: {patient[0]}, Vorname: {patient[1]}, Nachname: {patient[2]}, "
                                  f"Alter: {patient[3]}, Adresse: {patient[4]}, Telephon: {patient[5]}, "
                                  f"Hinweis: {patient[6]}", ln=True)
    pdf.output(file_path)
    messagebox.showinfo('Erfolgreich', "Datenexport nach PDF erfolgreich!")

# export data to a json file
def export_to_json():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[('JSON Files', '*.json')])
    if file_path:
        data_list = []
        for child in tree.get_children():
            data_list.append(tree.item(child, 'values'))

        with open(file_path, 'w') as jsonfile:
            json.dump(data_list, jsonfile)
        messagebox.showinfo("Erfolgreich", "Datenexport nach JSON erfolgreich!")


############################# save button #############################
def save():
    matricule = matriculeEntry.get()
    nom = nomEntry.get()
    prenom = prenomEntry.get()
    age = ageEntry.get()
    adresse = adresseEntry.get()
    telephone = telephoneEntry.get()
    remarque = remarqueEntry.get()

    cursor.execute('''
            INSERT INTO patients (matricule, nom, prenom, age, adresse, telephone, remarque)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (matricule, nom, prenom, age, adresse, telephone, remarque))
    conn.commit()
    
    tree.insert('', 'end', values=[matricule, nom, prenom, age, adresse, telephone, remarque])
    messagebox.showinfo("Erfolgreich", "Daten erfolgreich gespeichert!!")

    matriculeEntry.delete(0, 'end')
    nomEntry.delete(0, 'end')
    prenomEntry.delete(0, 'end')
    ageEntry.delete(0, 'end')
    adresseEntry.delete(0, 'end')
    telephoneEntry.delete(0, 'end')
    remarqueEntry.delete(0, 'end')

############################# delete button #############################
def delete():
    selectedPatients = reversed(tree.selection())
    for patient in selectedPatients:
        selected_patient_id = tree.item(patient, 'values')[0]
        cursor.execute('DELETE FROM patients WHERE matricule = ?', (selected_patient_id,))
        conn.commit()

        tree.delete(patient)

############################# edit button #############################
def edit():
    selectedPatient = tree.selection()
    if selectedPatient:
        matricule = matriculeEntry.get()
        nom = nomEntry.get()
        prenom = prenomEntry.get()
        age = ageEntry.get()
        adresse = adresseEntry.get()
        telephone = telephoneEntry.get()
        remarque = remarqueEntry.get()

        try:
            # Use placeholders in the SQL query to avoid SQL injection
            cursor.execute('''
                UPDATE patients
                SET nom=?, prenom=?, age=?, adresse=?, telephone=?, remarque=?
                WHERE matricule=?
            ''', (nom, prenom, age, adresse, telephone, remarque, matricule))

            conn.commit()

            # Update the values in the treeview for the selected patient
            tree.item(selectedPatient, values=[matricule, nom, prenom, age, adresse, telephone, remarque])

            messagebox.showinfo('Erfolgreich', 'Änderungen erfolgreich in der Datenbank gespeichert!')

        except sqlite3.Error as e:
            # Handle any potential database errors
            messagebox.showerror("Error", f"Database error: {str(e)}")

def on_treeview_select(event):
    selected_item = tree.selection()
    
    if selected_item:
        # Get the values of the selected patient
        values = tree.item(selected_item, 'values')
        
        # Populate entry widgets with the selected patient's information
        matriculeEntry.delete(0, 'end')
        matriculeEntry.insert(0, values[0])

        nomEntry.delete(0, 'end')
        nomEntry.insert(0, values[1])

        prenomEntry.delete(0, 'end')
        prenomEntry.insert(0, values[2])

        ageEntry.delete(0, 'end')
        ageEntry.insert(0, values[3])

        adresseEntry.delete(0, 'end')
        adresseEntry.insert(0, values[4])

        telephoneEntry.delete(0, 'end')
        telephoneEntry.insert(0, values[5])

        remarqueEntry.delete(0, 'end')
        remarqueEntry.insert(0, values[6])



############################# frame1 #############################
frame1= CTkFrame(w,width=350,height=400)
frame1.place(x=35,y=70)

############################# labels and inputs #############################
CTkLabel(master=frame1,text='Patient Id :', ).place(x=10,y=10)
matriculeEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
matriculeEntry.place(x=160,y=10)

CTkLabel(master=frame1,text='Patient Vorname :', ).place(x=10,y=50)
nomEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
nomEntry.place(x=160,y=50)

CTkLabel(master=frame1,text='Patient Nachname :', ).place(x=10,y=90)
prenomEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
prenomEntry.place(x=160,y=90)

CTkLabel(master=frame1,text='Patient Alter :', ).place(x=10,y=130)
ageEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
ageEntry.place(x=160,y=130)

CTkLabel(master=frame1,text='Patient Adresse :', ).place(x=10,y=170)
adresseEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
adresseEntry.place(x=160,y=170)

CTkLabel(master=frame1,text='Patient Telephon :', ).place(x=10,y=210)
telephoneEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
telephoneEntry.place(x=160,y=210)

CTkLabel(master=frame1,text='Hinweis :', ).place(x=10,y=250)
remarqueEntry = CTkEntry(master=frame1,width=180,fg_color='black',font=('calibri',15),border_width=1,corner_radius=5)
remarqueEntry.place(x=160,y=250)

############################# buttons #############################
enregistrerbtn = CTkButton(master=frame1, width=140, fg_color='grey', text_color='black', font=('calibri',18,'bold'), text='Save ', command=save)
enregistrerbtn.place(x=25,y=315)
modifierbtn = CTkButton(master=frame1, width=140, fg_color='grey', text_color='black', font=('calibri',18,'bold'), text='Edit ',command=edit)
modifierbtn.place(x=185,y=315)
supprimerbtn = CTkButton(master=frame1, width=140, fg_color='grey', text_color='black', font=('calibri',18,'bold'), text='Delete ', command=delete)
supprimerbtn.place(x=100,y=360)

############################# menu bar #############################
menubar = Menu(master=w)
# File Menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Import Data", command=import_data)
file_menu.add_command(label="Export to PDF", command=export_to_pdf)
file_menu.add_command(label="Export to CSV", command=export_to_csv)
file_menu.add_command(label="Export to TXT", command=export_to_txt)
file_menu.add_command(label="Export to JSON", command=export_to_json)


############################# frame 2 #############################
frame2= CTkFrame(master=w,width=720,height=380)
frame2.place(x=405,y=70)

CTkLabel(master=frame2,corner_radius=5,width=720,height=40, text='Patienten Liste',fg_color='black',font=('calibri',20,'bold')).place(x=0,y=0)

############################# tree view #############################
columns = ("Id", "Vorname", "Nachname", "Alter", "Adresse", "telephon", "Hinweis")
tree = ttk.Treeview(master=frame2, columns=columns, show="headings")

style = ttk.Style(w)
style.theme_use("clam")
style.configure("Treeview", background="black", fieldbackground="black", foreground="white")
style.configure("Treeview.Heading", font=('calibri',15))
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100,anchor=CENTER)
    
tree.place(x=5, y=60)
tree.config(height=20)
tree.bind("<<TreeviewSelect>>", on_treeview_select)

w.config(menu=menubar)
w.mainloop()