import pygame

MP3_FILE = "sounds/civil_war/prokopowicz032322.mp3"

########## PYGAME ##########
# https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python
# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.pause


pygame.mixer.init()
my_sound = pygame.mixer.Sound(MP3_FILE)
my_sound.set_volume(0.5)
my_sound.play()
pygame.time.wait(int(my_sound.get_length() * 1000))
print("done playing")
