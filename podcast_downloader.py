import requests


def download_files(urls, path):
    """
    urls: list of dictionaries with keys:
        url: the link to use to download
        title: what to name the downloaded file
    path: directory path to store the files

    Download each audio link listed in urls and store them to the given directory.
    """
    for url in urls:
        audio_file = requests.get(url['url'])
        open(f'{path}/{url["title"]}', 'wb').write(audio_file.content)
        print(f"downloaded {url['title']}")
