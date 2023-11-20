# Random Password geneator -> generates a ranom password with 
# Caps letter, Small letter, digit, Special char

import random
import string

def generate():
    pass_len = int(input('Required len of the password (min = 8, max= 16)  '))
    special_chars = '!@#$%^&*()'
    password = []
    password.append(random.choice(string.ascii_letters).upper())
    password.append(random.choice(string.ascii_letters).lower())
    password.append(random.choice(special_chars)) 
    password.append(random.choice(string.digits)) 

    if pass_len < 8 :
        pass_len = 4
    elif pass_len > 16 :
        pass_len = 12
    else :
        pass_len -= 4

    for x in range(pass_len):
        password.append(random.choice(string.digits + special_chars + string.ascii_letters)) 

    random.shuffle(password)
    return ''.join(password)


print(generate())