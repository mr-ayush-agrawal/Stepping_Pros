'''
Here we are making buttons to control the Playback of the video
'''

from globalDec import *

button = tk.Button(Window, text='<< Previous (Fast)', width=50)
button.pack()
button = tk.Button(Window, text='< Previous (Slow)', width=50)
button.pack()
button = tk.Button(Window, text='>> Next (Fast)', width=50)
button.pack()
button = tk.Button(Window, text='> Next (Slow)', width=50)
button.pack()
button = tk.Button(Window, text='OUT', width=50)
button.pack()
button = tk.Button(Window, text='NOT OUT', width=50)
button.pack()