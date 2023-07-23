from load import *

# Creating Canvas for the window
# Agrs -> Window, Width, Height
canvas = tk.Canvas(Window, width=SET_WIDTH, height=SET_HEIGHT)
# Printin the Image on Canvas
image_on_canvas = canvas.create_image(0,0,ancho= tk.NW, image= photo)
canvas.pack()

from Button import *

Window.mainloop()