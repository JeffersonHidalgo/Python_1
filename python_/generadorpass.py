import random 

def generate_password():
    password = ""
    for i in range(8):
        password += random.choice(
            list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
        )
    return password

print(generate_password())