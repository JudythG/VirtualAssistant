import requests
from bs4 import BeautifulSoup


# todo: store podcast titles (csv) so when download again don't download same podcasts
# todo: do not download files that have already been downloaded


class ThreadsPodcastScraper:
    """
    Scrapes links to audio podcasts from Threads From The National Tapestry: Stories From The American Civil War
    """
    def __init__(self):
        self.url = 'https://fredkigerthreadspodcast.podbean.com'

    def get_podcast_urls(self):
        """
        returns list of all pages that contain podcast links
        """
        pages = [self.url]
        page_counter = 1
        url = self.url
        load_more = True
        while load_more:
            front_page_content = requests.get(url=url)
            soup = BeautifulSoup(front_page_content.text, "html.parser")
            load_more_div = soup.find(name='div', class_='load-more')
            if load_more_div:
                page_counter += 1
                url = f"{self.url}/page/{page_counter}/"
                pages.append(url)
            else:
                load_more = False
        return pages

    def get_podcasts(self):
        """
        returns podcasts to download as a list of dictionaries
        Dictionary keys are:
            url: the link to use to download
            title: what to name the downloaded file
        """
        podcasts = []
        front_pages = self.get_podcast_urls()
        for page in front_pages:
            front_page_content = requests.get(url=page)
            soup = BeautifulSoup(front_page_content.text, "html.parser")
            podcasts_anchor_tags = soup.select('.cc-post-toolbar a')

            links_to_download_pages = [anchor_tag.get_attribute_list('href')[0] for anchor_tag in podcasts_anchor_tags]
            for link in links_to_download_pages:
                download_page_content = requests.get(url=link)
                download_page_soup = BeautifulSoup(download_page_content.text, "html.parser")
                download_anchor_tag = download_page_soup.find(class_='download-btn')
                download_link = download_anchor_tag.get('href')
                split_link = download_link.split('/')
                title = split_link[len(split_link) - 1]
                podcasts.insert(0, {'url': download_link, 'title': title})

        return podcasts


# scraper = ThreadsPodcastScraper()
# threads_podcasts = scraper.get_podcasts()
# for cast in threads_podcasts:
#     print(cast)
