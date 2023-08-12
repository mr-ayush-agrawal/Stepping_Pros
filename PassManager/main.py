from cryptography.fernet import Fernet

def wKey():
    '''
    This is for generating a key to encryt and store it in a file
    '''
    key = Fernet.generate_key()
    # Storing the key in a file
    with open('PassManager/key.key', 'wb') as Key_File:
        Key_File.write(key)

def load_key():
    '''
    This would return the Key for encrypting and decrypting
    and return the key
    '''

    file = open('PassManager/key.key', 'rb')
    key = file.read()
    file.close()
    return key

def view():
    with open("PassManager/PassWords.txt", 'r') as file :
        for line in file.readlines():
            AP = line.split(' |$| ')
            print(f"Account : {AP[0]}  -> Password : {fer.decrypt(AP[1].encode()).decode()}")

def Add():
    Account = input('Enter the Account : ')
    pswd = input('Enter the Password : ' )

    with open("PassManager/PassWords.txt", 'a') as file :
        file.write(Account + " |$| " + fer.encrypt(pswd.encode()).decode() + '\n')
        # |$| ->  is delimeter for seprating the Acc and pswd
        # encode is to convert str -> byte string
        # decode byte string -> string

mstr = input ("Enter the master password :")
menu = '''
1. View Passwords
2. Add Passord
Enter Your Choice
'''

# Converting stirng to byte string as Fernet accepts the byte string for encrypting
key = load_key() + bytes(mstr, 'UTF-8')
fer = Fernet(key)
print(fer)

if __name__ == '__main__':
    while True:
        ch = input(menu)
        if ch == '1' :
            view()
        elif ch == '2' :
            Add()
        else :
            print("Exiting the Program")
            break
