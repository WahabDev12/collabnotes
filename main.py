import tkinter as tk
from db import Database
from tkinter import Button, PhotoImage, Toplevel, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import os
from PIL import Image,ImageTk

class MainLogic():

    # def __init__(self):
    #     self.notes_list = []
        
        # super().__init__(master)
        # root.geometry("800x650")
        # root.configure(bg = "#10C5A7")
        # self.create_widgets_screen()
        # self.connect_database()

        # self.selected_note = 0

        # # Load image icon and display
        # self.load = Image.open(os.path.abspath("notes_icon.png"))
        # self.render = ImageTk.PhotoImage(self.load)
        # self.img = tk.Label(self.master, image=self.render,height = 59,bg = "#10C5A7")
        # self.img.place(x =570, y = 10)

    
    def connect_database(self):
        global db
        db = Database("notesapp.db")

    def create_widgets(self):
        
        create_widgets_screen = Toplevel(root)
        create_widgets_screen.geometry("800x650")
        create_widgets_screen.configure(bg = "#10C5A7")
        create_widgets_screen()
        self.connect_database()
        
        
        self.selected_note = 0

        # Load image icon and display
        self.load = Image.open(os.path.abspath("notes_icon.png"))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = tk.Label(self.create_widgets_screen, image=self.render,height = 59,bg = "#10C5A7")
        self.img.place(x =570, y = 10)
        # Caption
        self.main_caption = tk.Label(self.create_widgets_screen,fg="#0D2E28",bg="#10C5A7", text='Collaborative Notes App', font=('Comic Sans MC', 25,"italic"))
        self.main_caption.place(x = 200, y = 15)

        # Title
        self.title = tk.StringVar()
        self.title_caption = tk.Label(
            self.create_widgets_screen, fg="#0D2E28",bg="#10C5A7", text='Title of Note', font=('bold', 14), pady=20)
        self.title_caption.place(x = 300, y = 50)
        self.title_entry = tk.Entry(self.create_widgets_screen, textvariable=self.title,font=('bold', 14))
        self.title_entry.place(x = 190, y = 110, width=400,height = 30)

        # Description
        self.description= tk.StringVar()
        self.description_label = tk.Label(
            self.create_widgets_screen,fg="#0D2E28",bg="#10C5A7", text='Note Description (150 words max)', font=('bold', 14))
        self.description_label.place(x = 250, y = 160)
        self.description_entry = tk.Entry(
            self.create_widgets_screen, textvariable=self.description,font=('bold', 11))
        self.description_entry.place(x = 190, y = 200,width=400, height=90)

        # Buttons
        self.add_btn = tk.Button(
            self.create_widgets_screen, text="Add Note", width=12, command=self.add_note)
        self.add_btn.place(x = 150, y = 350)

        self.delete_btn = tk.Button(
            self.create_widgets_screen, text="Edit Note", width=12, command=self.update_note)
        self.delete_btn.place(x=290,y=350)

        self.update_btn = tk.Button(
            self.create_widgets_screen, text="Delete Note", width=12, command=self.delete_note)
        self.update_btn.place(x=420,y=350)

        self.exit_btn = tk.Button(
            self.create_widgets_screen, text="Reset", width=12, command=self.clear_notes)
        self.exit_btn.place(x=560,y=350)


        # List of Notes Table
        self.notes_list = tk.Listbox(self.create_widgets_screen,bg = "#293230",fg="white", height=10, width=100, border=0,borderwidth=0, highlightthickness=0, font = "Times 10")
        self.notes_list.place(x = 100, y = 460)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.create_widgets_screenr,orient="vertical")
        self.scrollbar.place(x = 685, y = 460)

        # Set scrollbar to notes
        self.notes_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.notes_list.yview)

        # Bind select
        self.notes_list.bind('<<ListboxSelect>>', self.select_note)

        # Instruction
        self.instruction = tk.Label(self.create_widgets_screen,fg="#0D2E28",bg="#10C5A7", text='* Select a note to edit or delete *', font=('Comic Sans MC', 15,"italic"))
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

            messagebox.showinfo("SUCESS","Added new note")
            return 


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



    def main_screen(self):
        global root
        root = tk.Tk()
        
        root.configure(bg='blue')
        root.geometry("500x600")
        root.title('LANDING PAGE')

        login_btn = tk.Button(text='Login', height='2', width='30', command = login)
        login_btn.pack()
        register_btn = tk.Button(text='Login', height='2', width='30', command = register)
        register_btn.pack()
        
       


    
# root = tk.Tk()
# root.title("ONLINE COLLABO NOTES")

app = MainLogic()
app.display_data()


if __name__ == "__main__":
   app.mainloop()


