
from tkinter import messagebox

# a class of objects of users registerd on the app
class Users:
    def __init__(self,username,email,password):
        '''A constuctor method with instance variables of the class Users'''
        self.username = username
        self.email = email
        self.password = password
        
#an athutication class to register and and save users' credentials to a csv file
class Authentication:

    global filename
    filename = 'registered_users.csv'

    def __init__(self):
        self.registered_users_list = []


    def __str__(self):
        return f"{self.username,self.email,self.password}"


    def register_user(self, user):
        '''A method to register users, it takes a user object and checks if the user is not
         already registered.
         It registers the user if it does not exist in the system and renders an error message 
         if it already is already registered
        
        '''
        # self.load_file_data()
        if user.password in [user_[2] for user_ in self.registered_users_list] and user.username in [user_[0] for user_ in self.registered_users_list]:
                return messagebox.showerror("ERROR","User already exists")
        else:
            self.registered_users_list.append((user.username, user.email, user.password))
            self.add_registered_user_to_file()

    def load_file_data(self):

        '''A method that loads data from the csv file 
        and set the data to attributes of an instance of the User class
        
        '''

        self.registered_users_list.clear()
        file = open(filename, "r")
        lines = file.readlines()
        
        for line in lines[1:]:
            line = line.strip()
            line_list = line.split(',')
            user = Users(line_list[0], line_list[1], line_list[2])
            self.register_user(user)


    def add_registered_user_to_file(self):

        '''A method that adds users data to a csv file, the first column of the csv contains
         the column headings, any line after represents the information about each registered user'''

        file = open(filename, "w")
        file.write('{},{},{}\n'.format('username', 'user_email', 'user_password'))
        for user in self.registered_users_list:
            file.write('{},{},{}\n'.format(user[0], user[1], user[2]))

        # self.load_file_data()
                

auth = Authentication()