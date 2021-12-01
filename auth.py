import csv

class Users:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
        


class Authentication:


    filename = 'registered_users.csv'

    def __init__(self):
        self.registered_users_list = []


    def __str__(self):
        return f"{self.username,self.email,self.password}"


    def register_user(self, user):
        
        if user.password in [user_[2] for user_ in self.registered_users_list]:
                return False

        self.registered_users_list.append((user.username, user.email, user.password))


    def load_file_data(self):
        self.registered_users_list.clear()
        file = open(Authentication.filename, "r")
        lines=file.readlines()
        
        for line in lines:
            line = line.strip()
            line_list = line.split(',')
            print(line_list)
            user = Users(line_list[0], line_list[1], line_list[2])
            self.register_user(user)
       

        file.close()        

    def add_registered_user_to_file(self):
        file = open(Authentication.filename, "w")
        for user in self.registered_users_list:
            file.write('{},{},{}\n'.format(user[0], user[1], user[2]))

        file.close()
                



auth = Authentication()