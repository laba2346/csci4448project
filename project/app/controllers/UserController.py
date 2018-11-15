from app import login
from ..models.Employee import *

@login.user_loader
def load_user(user_id):
    return find_user(user_id)


def find_user(user_id):
    user_file = open("user_file.txt", 'r')
    for line in user_file:
        fields = line.split(',')
        line_user_id = fields[0]
        name = fields[1]
        username = fields[2]
        password = fields[3]
        print(line_user_id)
        if user_id == line_user_id:
            return Employee(name, username, password, str(user_id))
    return None

def find_user_username(desired_username):
    user_file = open("user_file.txt")
    for line in user_file:
        fields = line.split(',')
        user_id = fields[0]
        name = fields[1]
        username = fields[2]
        password = fields[3]
        print(password)
        if username == desired_username:
            return Employee(name, username, password, str(user_id))
    return None
