import podcast_manager
import pygame
from threads_podcast_scraper import ThreadsPodcastScraper
from podcast_downloader import download_files
from shared_constants import THREADS_DIR

"""
Virtual assistant for my Dad.

Plays Civil War podcasts:
* Threads From The National Tapestry: Stories From The American Civil War

As my Dad does not have Internet at home, download is a separate option. I will get the downloaded files to him. 
"""

# todo: get next file to play from podcast manager
MP3_FILE = f"{THREADS_DIR}/049_-_FREDDIE_KIGER_-_SEX_IN_THE_CIVIL_WARb08rl.mp3"


# ToDo: how tell if my_sound has finished playing? Should be able to call functions off of Channel but keep getting
#  error messages. use Google to see what I'm doing wrong examples of checking if music finished
#  https://stackoverflow.com/questions/58630700/utilising-the-pygame-mixer-music-get-endevent?msclkid
#  =de694ee4d0ab11ecbbec06b7ed6f8100

# Todo: I think, if play, stop, play, pause, and replay will have two soundtracks going. Test and if true, fix

# todo: decide: audioplayer: https://pypi.org/project/audioplayer/  Should I try this?


def download_podcasts():
    scraper = ThreadsPodcastScraper()
    # todo: should I download all podcasts (when following more than one link) or specify which link to download from?
    threads_podcasts = scraper.get_podcasts()
    download_files(urls=threads_podcasts, path=THREADS_DIR)


def process_commands():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound(MP3_FILE)

    while True:
        print('Commands: play, pause, restart, stop, download, exit')
        cmd = input("Get command: ").lower()
        if cmd == "play":
            my_sound.play()
        elif cmd == "pause":
            pygame.mixer.pause()
        elif cmd == "restart":
            pygame.mixer.unpause()
        elif cmd == "stop":
            my_sound.stop()
        elif cmd == "download":
            download_podcasts()
        elif cmd == "exit":
            break
        else:
            print("command not recognized. Please reenter command:")


process_commands()


# todo: error handling


# mgr = podcast_manager.PodcastManager()
#
# # cue up the next podcast to play
# mgr.get_next_threads_podcast()

