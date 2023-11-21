# Making a typing speed calculator using Python

import time
from random import choice

def Speed(userstr, start, end):
    delay = end - start
    wpm = len(userstr)/delay
    return round(wpm,2)

def Errct(teststr, userstr):
    Error = 0
    for x in range(len(userstr)):
        try :
            # Try and except for the if length is less for the test string
            if userstr[x] != teststr[x]:
                Error+=1
        except :
            Error+=1
    return Error

TestStrings = ['This is Ayush. I am a Student and I am a coder and I can do anything in this world.',
               'I love coding in python and also code in c++. I am working on my career very hard.',
               'I will be successful someday. I can bet on it. This is comming and very soon.',
               'I love watching cricket and I love Virat Kohli. He is the gratest batsan that the game has ever seen.',
               'A quick brown fox jumps over the lazy dog.']

test = choice(TestStrings)
print("Test String is\n",test)

print('\n\nTest Starts in  ', end = "")
for x in range(5):
    print(f'\b{4-x}', end='')
    time.sleep(1)

start = time.time()
user  = input('\rType Here :               \n')
end  = time.time()

print("\n\n ***** Results ***** ")
print(f'Your Typing speed is {Speed(user, start, end)} w/min')
print(f'Error count is {Errct(test, user)}')