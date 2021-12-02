import os
import tkinter as tk
import tksheet
from tkinter.constants import END
from db import Database
from tkinter import StringVar, Toplevel, messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from auth import *

class MainLogic(tk.Frame):

    def __init__(self,master):
        super().__init__(master)
        master.geometry("400x350")
        master.configure(bg = "#10C5A7")
        self.main_screen()
        global saved_user_details
        saved_user_details = {}
        
    
    def main_screen(self):
        # Create widgets for main page here
        self.master.title("LANDING PAGE")

        self.main_caption = tk.Label(self.master, text = "WELCOME TO NOTES APP", 
        font=('Consolas', 20), bg = "#10C5A7", fg = "white")
        self.main_caption.place( x = 50, y = 0)
        self.main_reg_btn = tk.Button(self.master, text = "LOGIN",bg = "#10C5A7",fg="white", command = self.login_view)
        self.main_reg_btn.place(x = 130, y = 60,width = 120, height = 40)
        self.main_log_btn = tk.Button(self.master, text = "REGISTER",bg = "#10C5A7", fg="white", command = self.register_view)
        self.main_log_btn.place(x = 130, y = 130,width = 120, height = 40)

    
    def connect_database(self):
        global db
        db = Database("notesapp.db")
    
    # WINDOW FOR NOTES APP VIEW
    def notes_view(self):
        self.notes_view = Toplevel(root)
        self.notes_view.geometry("900x850")
        self.notes_view.configure(bg = "#10C5A7")
        self.connect_database()
        self.notes_view.title("NOTES APP VIEW")
        self.notes_view_widgets()
        self.display_data()

        global note_values
        note_values = 0

        # Load image icon and display
        self.load = Image.open(os.path.abspath("notes_icon.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = tk.Label(self.notes_view, image = self.render,height = 59,bg = "#10C5A7")
        self.img.place(x = 570, y = 10)

    def register_view(self):
        self.register_view_screen = Toplevel(root)
        self.register_view_screen.geometry("400x350")
        self.register_view_screen.configure(bg = "#10C5A7")
        self.connect_database()
        self.register_view_screen.title("REGISTER PAGE")
        self.register_view_widgets()

    # WIDGETS FOR REGISTER VIEW

    def register_view_widgets(self):
        # Create widgets for login page here
        self.master.title("REGISTER PAGE")
        self.main_caption = tk.Label(self.register_view_screen, text = "REGISTER NEW ACCOUNT", 
        font = ('Consolas', 20), bg = "#10C5A7", fg = "white")
        self.main_caption.place( x = 50, y = 0)

        # Initializing the textvaraibles for register
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        # Username Label
        self.reg_username_label = tk.Label(self.register_view_screen, text = "Username: ", bg = "#10C5A7",font = ('Helvetica', 15))
        self.reg_username_label.place(x = 130 , y = 40 )
        # Username Entry box
        self.reg_username = tk.Entry(self.register_view_screen, textvariable = self.username)
        self.reg_username.place(x = 130 , y = 80, height = 25)
        # Email Label
        self.reg_email_label = tk.Label(self.register_view_screen, text = "Email: ",bg = "#10C5A7",font = ('Helvetica', 15))
        self.reg_email_label.place(x = 130, y = 110 )
        # Email Entry box
        self.reg_email = tk.Entry(self.register_view_screen, textvariable = self.email)
        self.reg_email.place(x = 130, y = 150, height = 25)
        # Password Label
        self.password_label = tk.Label(self.register_view_screen, text = "Password: ", bg = "#10C5A7",font = ('Helvetica', 15))
        self.password_label.place(x = 130 , y = 190 )
        # Password Entry box
        self.reg_password = tk.Entry(self.register_view_screen, textvariable = self.password, show="*")
        self.reg_password.place(x = 130 , y = 230, height = 25)
        # Registration button
        self.main_reg_btn = tk.Button(self.register_view_screen, text = "REGISTER", bg = "#10C5A7", fg="white", command = self.add_user)
        self.main_reg_btn.place(x = 130, y = 270,width = 120, height = 40)
    
        
    # Window for login page                                                                                                
    def login_view(self):
        self.login_view_screen = Toplevel(root)
        self.login_view_screen.geometry("400x350")
        self.login_view_screen.configure(bg = "#10C5A7")
        self.connect_database()
        self.login_view_screen.title("LOGIN PAGE")
        # auth.add_registered_user_to_file()
        self.login_view_widgets()


    def login_view_widgets(self):
        # Create widgets for REGISTER page here
        self.master.title("LOGIN ACCOUNT")

        # Initializing text variables
        self.login_username = StringVar()
        self.login_password = StringVar()


        # Caption
        self.main_caption = tk.Label(self.login_view_screen, text = "SIGN IN", 
        font=('Consolas', 20), bg = "#10C5A7", fg = "white")
        self.main_caption.place( x = 140, y = 0)
        # Login email label and entry
        self.username_label = tk.Label(self.login_view_screen, text = "Username: ", bg = "#10C5A7",font=('Helvetica', 15))
        self.username_label.place(x = 130 , y = 40 )
        self.login_username_entry = tk.Entry(self.login_view_screen, textvariable = self.login_username)
        self.login_username_entry.place(x = 130 , y = 80, height = 25)
        # Login password label and entry 
        self.password_label = tk.Label(self.login_view_screen, text = "Password: ", bg = "#10C5A7",font=('Helvetica', 15))
        self.password_label.place(x = 130 , y = 110 )
        self.login_password_entry = tk.Entry(self.login_view_screen, textvariable = self.login_password, show="*")
        self.login_password_entry.place(x = 130 , y = 150, height = 25)
        # Login Button
        self.main_log_btn = tk.Button(self.login_view_screen, text = "LOGIN", bg = "#10C5A7", fg="white", command = self.verify_login)
        self.main_log_btn.place(x = 130, y = 190,width = 120, height = 40)


    # Getting registration details and registering user
    def add_user(self):
        email_info = self.email.get()
        username_info = self.username.get()
        password_info = self.password.get()
        if email_info == "" or username_info == "" or password_info == "":
            return messagebox.showerror("Required fields", "Please fill all entries")
        else:
            global new_user
            new_user = Users(username_info, email_info, password_info)
            # saved_user_details[username_info] = password_info

            
            auth.load_file_data()
            auth.register_user(new_user)

            self.reg_username.delete(0, END)
            self.reg_password.delete(0, END)
            self.reg_email.delete(0, END)
            self.login_view()
            self.register_view_screen.destroy()

    # Methods to verify login details
    def load_data_from_registered_users(self):
        f = open('registered_users.csv', 'r')
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            line_array = line.split(',')
            saved_user_details[line_array[0]] = line_array[2]


    def verify_login(self):
        login_username_info = self.login_username.get()
        password_info = self.login_password.get()

        print(saved_user_details)
        self.load_data_from_registered_users()
        # Checking if username and email matches 
        if login_username_info in saved_user_details and saved_user_details[login_username_info] == password_info:
                self.notes_view()
                print('Successfully Logged In')
        else:
                messagebox.showerror("Authentication failed",
                "Invalid username or email")

        # Delete contents of text-fields
        self.login_username_entry.delete(0, END)
        self.login_password_entry.delete(0, END)
        
        self.login_view_screen.destroy()


    # WIDGETS FOR NOTES APP VIEW
    def notes_view_widgets(self):
            
            # Caption
            self.main_caption = tk.Label(self.notes_view,fg="#0D2E28",bg="#10C5A7", text='Collaborative Notes App', font = ('Comic Sans MC', 25,"italic"))
            self.main_caption.place(x = 200, y = 15)

            # Title
            self.title = tk.StringVar()
            self.title_caption = tk.Label(
            self.notes_view, fg="#0D2E28",bg="#10C5A7", text='Title  of Note', font = ('bold', 14), pady=20)
            self.title_caption.place(x = 300, y = 50)
            self.title_entry = tk.Entry(self.notes_view, textvariable = self.title,font=('bold', 14))
            self.title_entry.place(x = 190, y = 110, width=400,height = 30)

            # Description
            self.description= tk.StringVar()
            self.description_label = tk.Label(
                self.notes_view,fg="#0D2E28",bg="#10C5A7", text='Note Description (50 words max)', font = ('bold', 14))
            self.description_label.place(x = 250, y = 160)
            self.description_entry = tk.Entry(
                self.notes_view, textvariable = self.description,font = ('bold', 11))
            self.description_entry.place(x = 190, y = 200,width=400, height=90)

            # Buttons
            self.add_btn = tk.Button(
                self.notes_view, text="Add Note", width=12, command=self.add_note)
            self.add_btn.place(x = 150, y = 350)

            self.delete_btn = tk.Button(
                self.notes_view, text="Edit Note", width=12, command=self.update_note)
            self.delete_btn.place(x=290,y=350)

            self.update_btn = tk.Button(
                self.notes_view, text="Delete Note", width=12, command=self.delete_note)
            self.update_btn.place(x=420,y=350)

            self.reset_btn = tk.Button(
                self.notes_view, text="Reset", width=12, command=self.clear_notes)
            self.reset_btn.place(x=560,y=350)

            # Adding the Table for displaying table
            global tree

            tree = ttk.Treeview(self.notes_view, column=("c1", "c2", "c3"), show='headings')


            tree.column("#1", anchor=tk.CENTER, width = 50)

            tree.heading("#1", text="S/N")

            tree.column("#2", anchor=tk.CENTER, width = 250)

            tree.heading("#2", text="TITLE")

            tree.column("#3", anchor=tk.CENTER, width = 450)

            tree.heading("#3", text="DESCRIPTION")

            tree.place(x = 80, y = 460)

            tree.tag_configure("oddrow",background="lightblue")


            # Binding select
            tree.bind("<Double-1>", self.select_note)

            # Instruction
            self.instruction = tk.Label(self.notes_view,fg="#0D2E28",bg="#10C5A7", text='* Double-click to edit or delete note *', font=('Comic Sans MC', 14,"italic"))
            self.instruction.place(x = 250, y = 420)


    def display_data(self):
            # Loop through notes
            for row in db.fetch_data():
                # Display notes
                tree.insert("",tk.END, values = row)

    def add_note(self):
            if self.title.get() == '' or self.description.get() == '':
                return messagebox.showinfo("Required Fields", "Please include all fields")
                
            else:
                # Insert into Database
                db.insert_data(self.title.get(), self.description.get())

                # Clear list
                tree.delete(0, tk.END)
                
                tree.insert(parent = "", index = "end",text = "",values=(self.title.get(),self.description.get()), tags=("oddrow"))

                self.clear_notes()
               
    def update_note(self):
            self.selected_item = tree.focus()
            # Save new data
            global note_values
            note_values = tree.item(self.selected_item,text = "" , values = (self.title.get(), self.description.get()))
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            # Update new data in database
            db.update_data(note_values[0], self.title.get(), self.description.get())
            # Display data on table
            self.display_data()

    def delete_note(self):
            # Delete note from treeview
            x = tree.selection()[0]
            tree.delete(x)
            # Delete note from database
            db.delete_data(x[0])
            self.clear_notes()
            self.display_data()
            return  messagebox.showinfo("SUCCESS","Deleted Note")

    def clear_notes(self):
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        
    def select_note(self,action):
        try:
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

            self.selected_item = tree.focus()
            note_values = tree.item(self.selected_item,"values")
            print(note_values)
            # Add to entry boxes
            self.title_entry.insert(0, note_values[1])

            self.description_entry.insert(0, note_values[2])

        except:
            return messagebox.showerror("No Item was selected")
            
    
root = tk.Tk()

app = MainLogic(master=root)
app.load_data_from_registered_users()

if __name__ == "__main__":
    app.mainloop()


