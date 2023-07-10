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
    GAME_IMAGES['bird'] = image.load('Gallery\\Images\\bird.png').convert_alpha()
    GAME_IMAGES['background'] = image.load('Gallery\\Images\\Background.jpg').convert_alpha()
    
    

def loadSounds():
    GAME_SOUNDS['die'] = mixer.Sound("Gallery/Audio/die.mp3")
    GAME_SOUNDS['hit'] = mixer.Sound("Gallery/Audio/hit.mp3")
    GAME_SOUNDS['point'] = mixer.Sound("Gallery/Audio/point.wav")
    GAME_SOUNDS['swoosh'] = mixer.Sound("Gallery/Audio/swoosh.wav")
    GAME_SOUNDS['wing'] = mixer.Sound("Gallery/Audio/wing.wav")