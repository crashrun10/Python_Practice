import requests
from bs4 import BeautifulSoup


def youtube_spider(user_name):
    url = 'https://www.youtube.com/' + user_name + '/AtlanticVideos/videos'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    class_name = 'yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2'
    for link in soup.findAll('a', {'class' : class_name}):
        title = link.get('title')
        href = 'https://www.youtube.com' + link.get('href')
        print(title)
        print(href)


# This function doesn't work as google doesn.t allow bot to crawl the video's page
def get_info_about_video(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    fw = open('source_code.txt', "w")
    fw.write(plain_text)
    fw.close()
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.find_all('div', attrs={'class' : 'watch-view-count'}):
        views = link.text
        print(views)

#Pass the YouTuber's user name as parameter
youtube_spider('vevo')
