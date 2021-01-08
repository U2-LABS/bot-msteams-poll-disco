import csv

import requests
from bs4 import BeautifulSoup as BS

ZAYCEV_URL = r'https://zaycev.net'


def get_songs_form_source(amount: int):
    """ Gets songs data from the source. """
    songs = []

    response = requests.get(ZAYCEV_URL)
    soup = BS(response.content, 'html.parser')

    all_top_songs = soup.find_all(class_='musicset-track__download-link')

    for index, song_a in enumerate(all_top_songs[:amount]):
        song = {
            'mark': 0,
            'pos': index + 1,
            'voted_users': []
        }
        song['author'], song['title'] = song_a.get('title').split(' ', 2)[-1].split(' – ', 1)
        song['link'] = ZAYCEV_URL + song_a.get('href')
        songs.append(song)

    return songs
