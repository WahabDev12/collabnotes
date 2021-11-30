import tkinter as tk
from db import Database
from tkinter import PhotoImage, Toplevel, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import os
from PIL import Image,ImageTk

class MainLogic(tk.Frame):

    def __init__(self,master):
        super().__init__(master)
        master.geometry("400x350")
        master.configure(bg = "#10C5A7")
        self.main_screen()


    
    def main_screen(self):
        # Create widgets for main page here
        self.master.title("LANDING PAGE")

        self.main_caption = tk.Label(self.master, text = "WELCOME TO NOTES APP", 
        font=('Consolas', 20), bg = "#10C5A7", fg = "white")
        self.main_caption.place( x = 50, y = 0)
        self.main_reg_btn = tk.Button(self.master, text = "REGISTER",bg = "#10C5A7",fg="white")
        self.main_reg_btn.place(x = 130, y = 60,width = 120, height = 40)
        self.main_log_btn = tk.Button(self.master, text = "LOGIN",bg = "#10C5A7", fg="white", command = self.login_view)
        self.main_log_btn.place(x = 130, y = 130,width = 120, height = 40)


    
    def connect_database(self):
        global db
        db = Database("notesapp.db")
    
    # WINDOW FOR NOTES APP VIEW
    def notes_view(self):
        self.notes_view = Toplevel(root)
        self.notes_view.geometry("800x850")
        self.notes_view.configure(bg = "#10C5A7")
        self.connect_database()
        self.notes_view.title("NOTES APP VIEW")
        self.notes_view_widgets()
        self.display_data()

        self.selected_note = 0

        # Load image icon and display
        self.load = Image.open(os.path.abspath("notes_icon.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = tk.Label(self.notes_view, image=self.render,height = 59,bg = "#10C5A7")
        self.img.place(x = 570, y = 10)

    def login_view(self):
        self.login_view = Toplevel(root)
        self.login_view.geometry("400x350")
        self.login_view.configure(bg = "#10C5A7")
        self.connect_database()
        self.login_view.title("LOGIN PAGE")
        self.login_view_widgets()

    # WIDGETS FOR LOGIN VIEW

    def login_view_widgets(self):
        # Create widgets for login page here
        self.master.title("LANDING PAGE")

        self.main_caption = tk.Label(self.login_view, text = "LOGIN", 
        font=('Consolas', 20), bg = "#10C5A7", fg = "white")
        self.main_caption.place( x = 50, y = 0)
        self.username_label = tk.Label(self.login_view, text = "Username : ")
        self.username_label.place(x = 130 , y = 120 )
        self.login_username = tk.Entry(self.login_view)
        self.login_username.place(x = 130 , y = 140)
        self.main_log_btn = tk.Button(self.login_view, text = "LOGIN",bg = "#10C5A7", fg="white", command = self.notes_view)
        self.main_log_btn.place(x = 130, y = 160,width = 120, height = 40)

    # WIDGETS FOR NOTES APP VIEW
    def notes_view_widgets(self):
            
            # Caption
            self.main_caption = tk.Label(self.notes_view,fg="#0D2E28",bg="#10C5A7", text='Collaborative Notes App', font=('Comic Sans MC', 25,"italic"))
            self.main_caption.place(x = 200, y = 15)

            # Title
            self.title = tk.StringVar()
            self.title_caption = tk.Label(
                self.notes_view, fg="#0D2E28",bg="#10C5A7", text='Title of Note', font=('bold', 14), pady=20)
            self.title_caption.place(x = 300, y = 50)
            self.title_entry = tk.Entry(self.notes_view, textvariable=self.title,font=('bold', 14))
            self.title_entry.place(x = 190, y = 110, width=400,height = 30)

            # Description
            self.description= tk.StringVar()
            self.description_label = tk.Label(
                self.notes_view,fg="#0D2E28",bg="#10C5A7", text='Note Description (150 words max)', font=('bold', 14))
            self.description_label.place(x = 250, y = 160)
            self.description_entry = tk.Entry(
                self.notes_view, textvariable=self.description,font=('bold', 11))
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

            self.exit_btn = tk.Button(
                self.notes_view, text="Reset", width=12, command=self.clear_notes)
            self.exit_btn.place(x=560,y=350)


            # List of Notes Table
            self.notes_list = tk.Listbox(self.notes_view,bg = "#293230",fg="white", height=10, width=100, border=0,borderwidth=0, highlightthickness=0, font = "Times 10")
            self.notes_list.place(x = 100, y = 460)

            # Create scrollbar
            self.scrollbar = tk.Scrollbar(self.notes_view,orient="vertical")
            self.scrollbar.place(x = 685, y = 460)

            # Set scrollbar to notes
            self.notes_list.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.configure(command=self.notes_list.yview)

            # Bind select
            self.notes_list.bind('<<ListboxSelect>>', self.select_note)

            # Instruction
            self.instruction = tk.Label(self.notes_view,fg="#0D2E28",bg="#10C5A7", text='* Select a note to edit or delete *', font=('Comic Sans MC', 15,"italic"))
            self.instruction.place(x = 230, y = 420)


    def display_data(self):
            self.notes_list.delete(0, tk.END)
            # Loop through notes
            for row in db.fetch_data():
                # Display notes
                self.notes_list.insert(tk.END, row)

    def add_note(self):
            if self.title.get() == '' or self.description.get() == '':
                return messagebox.showinfo("Required Fields", "Please include all fields")
                
            else:
                # Insert into Database
                db.insert_data(self.title.get(), self.description.get())

                # Clear list
                self.notes_list.delete(0, tk.END)

                # Insert into list
                self.notes_list.insert(tk.END, (self.title.get(), self.description.get(
                )))

                self.clear_notes()
                self.display_data()

               
    def update_note(self):
            db.update_data(self.selected_note[0], self.title.get(), self.description.get())
            self.display_data()
            return messagebox.showinfo("SUCCESS","Updated Note")

    def delete_note(self):
            db.delete_data(self.selected_note[0])
            self.clear_notes()
            self.display_data()
            return  messagebox.showinfo("SUCCESS","Deleted Note")

    def clear_notes(self):
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        
    def select_note(self,action):
            try:
                index = self.notes_list.curselection()[0]
                self.selected_note = self.notes_list.get(index)
                # Add text to entries
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(tk.END, self.selected_note[1])
                self.description_entry.delete(0, tk.END)
                self.description_entry.insert(tk.END, self.selected_note[2])

            except:
                messagebox.showerror(
                    "No Item was selected")
                return
            
    
root = tk.Tk()

app = MainLogic(master=root)

if __name__ == "__main__":
    app.mainloop()


