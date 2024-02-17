from cryptography.fernet import Fernet 

'''
def add_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as k:
        k.write(key)
'''

def load_key():
    with open('key.key', 'rb') as enc:
        key = enc.read()
        return key

def add_login():
    site = input("Enter a login site: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    token = fer.encrypt(password.encode())

    with open('password_manager.txt', 'a') as f:
        f.write(site + '|' + username + '|' + token.decode() + "\n")

def view_login():
    with open('password_manager.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            site, username, password = data.split(sep = '|')
            decrypt = fer.decrypt(password.encode())
            print("\n", "site name:", site, "\n", "username:", username, "\n", "password:", decrypt.decode(), "\n")

def modify_login():
    site = input("Enter site login you want to modiy")

master_pass = 'mypass'
key = load_key() + master_pass.encode()
fer = Fernet(key)

cnt = 0
while cnt < 3:
    pwd = input("Master pasword: ")
    
    if pwd == master_pass:
        break
    else:
        cnt += 1
        print(f"You have {3 - cnt} remaining tries")

mode = input("What would you like to do.. Add a new login or view existing ones (add, view)? ").lower()
if mode == "view":
    view_login()
elif mode == "add":
    add_login()
else:
    quit()


    

        





