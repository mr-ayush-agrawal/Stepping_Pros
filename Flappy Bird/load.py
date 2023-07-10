from globalVar import *

def loadImages():
    # Setting the number images for score
    GAME_IMAGES['Numbers'] = (image.load('Gallery/Images/0.png').convert_alpha(),
                            image.load('Gallery/Images/1.png').convert_alpha(),
                            image.load('Gallery/Images/2.png').convert_alpha(),
                            image.load('Gallery/Images/3.png').convert_alpha(),
                            image.load('Gallery/Images/4.png').convert_alpha(),
                            image.load('Gallery/Images/5.png').convert_alpha(),
                            image.load('Gallery/Images/6.png').convert_alpha(),
                            image.load('Gallery/Images/7.png').convert_alpha(),
                            image.load('Gallery/Images/8.png').convert_alpha(),
                            image.load('Gallery/Images/9.png').convert_alpha(),
                            ) 
    GAME_IMAGES['base'] = image.load('Gallery\\Images\\Base.png').convert_alpha()
    GAME_IMAGES['pipe'] = (transform.rotate(image.load(PIPE).convert_alpha(), 180),
                        image.load(PIPE).convert_alpha()
                        )