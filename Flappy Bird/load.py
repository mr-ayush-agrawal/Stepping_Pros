'''
This File contains functions related to loading sounds and sptites of the game
It only contains function which make the code look clean
'''


from globalVar import *

def loadImages():
    # Setting the number images for score
    GAME_IMAGES['Numbers'] = (image.load('Flappy Bird/Gallery/Images/0.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/1.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/2.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/3.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/4.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/5.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/6.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/7.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/8.png').convert_alpha(),
                            image.load('Flappy Bird/Gallery/Images/9.png').convert_alpha(),
                            ) 
    GAME_IMAGES['base'] = image.load('Flappy Bird/Gallery\\Images\\Base.png').convert_alpha()
    GAME_IMAGES['pipe'] = (transform.rotate(image.load(PIPE).convert_alpha(), 180),
                        image.load(PIPE).convert_alpha()
                        )
    GAME_IMAGES['bird'] = image.load('Flappy Bird/Gallery\\Images\\bird.png').convert_alpha()
    GAME_IMAGES['background'] = image.load('Flappy Bird/Gallery\\Images\\Background.png').convert()
    
    

def loadSounds():
    GAME_SOUNDS['die'] = mixer.Sound("Flappy Bird/Gallery/Audio/die.mp3")
    GAME_SOUNDS['hit'] = mixer.Sound("Flappy Bird/Gallery/Audio/hit.mp3")
    GAME_SOUNDS['point'] = mixer.Sound("Flappy Bird/Gallery/Audio/point.wav")
    GAME_SOUNDS['swoosh'] = mixer.Sound("Flappy Bird/Gallery/Audio/swoosh.wav")
    GAME_SOUNDS['wing'] = mixer.Sound("Flappy Bird/Gallery/Audio/wing.wav")