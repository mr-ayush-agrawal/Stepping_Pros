mstr = input ("Enter the master password :")
menu = '''
1. View Passwords
2. Add Passord
Enter Your Choice
'''






def view():
    with open("PassWords.txt", 'r') as file :
        for line in file.readlines():
            AP = line.split(' |$| ')
            print(f"Account : {AP[0]}  -> Password : {AP[1]}")

def Add():
    Account = input('Enter the Account : ')
    pswd = input('Enter the Password : ' )

    with open("PassWords.txt", 'a') as file :
        file.write(Account + " |$| " + pswd + '\n')
        # |$| ->  is delimeter for seprating the Acc and pswd


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
