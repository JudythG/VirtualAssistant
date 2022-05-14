import os
from shared_constants import THREADS_DIR


class PodcastManager:
    """
    Manages playing already downloaded podcasts.
    Current podcasts:
    * threads refers to "Threads From The National Tapestry: Stories From The American Civil War"
    """
    def __init__(self):
        self.threads_podcasts = []
        self.THREADS_PODCAST_DIR = 'podcasts'

    # todo: returns most recent podcast that has not already been listened to
    def get_next_threads_podcast(self):
        """
        load files from directory and sort by date
        """
        podcasts = {os.path.getmtime(f'{THREADS_DIR}//{podcast}'): podcast for podcast in os.listdir(THREADS_DIR)}
        self.threads_podcasts = [value for (key, value) in sorted(podcasts.items())]
        for podcast in self.threads_podcasts:
            print(podcast)

