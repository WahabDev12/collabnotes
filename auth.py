import csv

class Authentication:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
        self.load_file_data("auth_data.csv")

    def load_file_data(self,filename):
        pass
                

    def __str__(self):
        return f"{self.username,self.email,self.password}"


    def register_user(self):
        username_data = self.username  # Use tkinter's get method afterwards
        email_data = self.username

    def login_user(self):
        pass