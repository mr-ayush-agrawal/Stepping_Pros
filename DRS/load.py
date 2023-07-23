'''
This Module will be loading all the stuffs from Gallery where the files has been stored
and this will be used for the review purpose
'''

from globalDec import *

cv_image = cv2.cvtColor(cv2.imread(r'E:\LearningProjects\DRS\Gallery\base.png'), cv2.COLOR_BGR2RGB)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_image))
