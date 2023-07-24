'''
Here we are making buttons to control the Playback of the video
'''

from load import *
from functools import partial
import threading as td
import imutils
import time


def Pending(decision):
    '''What we are going to do here ->
    1. Display decison pending
    2. wait for some time
    3. Display Out/NotOut
    '''
   
    # 1. 
    frame = cv2.cvtColor(cv2.imread(r'DRS\Gallery\decison_pending.png'), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = ImageTk.PhotoImage(image= Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tk.NW)

    # 2.
    time.sleep(1.5)

    # 3. Checking decision and then putting that image

    if decision == 'Out' :
        frame = cv2.cvtColor(cv2.imread(r'DRS\Gallery\out.png'), cv2.COLOR_BGR2RGB)
    else :
        frame = cv2.cvtColor(cv2.imread(r'DRS\Gallery\not_out.png'), cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = ImageTk.PhotoImage(image= Image.fromarray(frame))

    # Putting the Image to the canvas
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tk.NW)
    

# Out and Not Out functions will just change the images to the decision
def NotOut ():
    thread = td.Thread(target=Pending, args=("Not Out",))
    thread.daemon = 1
    thread.start()
    print(f"The decision is NOT OUT")

def Out ():
    thread = td.Thread(target=Pending, args=("Out",))
    thread.daemon = 1
    thread.start()
    print(f"The decision is OUT")

# Play would control the video playback
def Play (Speed):
    print(f"Playing the video with speed {Speed}")

    # Updating the frames
    DisFrame = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, DisFrame + Speed)

    # Concerting the frame to the Image to set it on canvas
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image= Image.fromarray(frame))
    
    # # If no frame is read
    # if not grabbed :
    #     stream.set(cv2.CAP_PROP_POS_FRAMES, DisFrame - Speed )


    # Now putting it to the canvas
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tk.NW)

    # Blinking Decision Pending OnScreen
    canvas.create_text(120, 25 ,fill= 'orange', font='Times 20 italic bold',text='Decision Pending')




# Loading the video using open-CV
stream = cv2.VideoCapture(r'DRS\Gallery\clip.mp4')



button = tk.Button(Window, text='<< Previous (Fast)', width=50, command= partial(Play, -15))
button.pack()
button = tk.Button(Window, text='< Previous (Slow)', width=50, command= partial(Play, -2))
button.pack()
button = tk.Button(Window, text='Next (Slow) >', width=50, command= partial(Play, 1))
button.pack()
button = tk.Button(Window, text='Next (Fast) >>', width=50, command= partial(Play, 15))
button.pack()
button = tk.Button(Window, text='OUT', width=50, command= Out)
button.pack()
button = tk.Button(Window, text='NOT OUT', width=50, command= NotOut)
button.pack()