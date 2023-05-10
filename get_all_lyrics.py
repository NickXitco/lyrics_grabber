from lyricsgenius import Genius
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re


token = 'ydLL5r8qv8kbL9QJDfs72DOCvaTDMB5D7v7OJRx8pz6Y_qOA9Uew8N1stqP1Y36z'
genius = Genius(token)
ALBUM_ID = 455019
album_result = genius.album(ALBUM_ID)
tracks_result = genius.album_tracks(ALBUM_ID, per_page=None, page=None, text_format=None)

album_title = album_result['album']['full_title']

album_title = unidecode(re.sub(r'[\u0020\u00A0\u1680\u2000-\u200A\u202F\u205F\u3000\u200b]+', ' ', album_title))

output = open('output/' + album_title + '.txt', 'w')

output.write(album_title + '\n')


def get_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    lyrics_div = soup.find('div', {'data-lyrics-container': 'true'})
    if lyrics_div is not None:
        # Replace <br> tags with newlines
        for br in lyrics_div.find_all('br'):
            br.replace_with('\n')
        # Transliterate non-ASCII characters to ASCII
        lyrics = lyrics_div.text.strip()
        lyrics = unidecode(lyrics)

        lyrics = re.sub(r'[\u0020\u00A0\u1680\u2000-\u200A\u202F\u205F\u3000\u200b]+', ' ', lyrics)
        return lyrics
    else:
        return "[INSTRUMENTAL]"


# print all tracks
i = 1
for result in tracks_result['tracks']:
    song_url = result['song']['url']
    song_title = result['song']['title']
    song_title = unidecode(re.sub(r'[\u0020\u00A0\u1680\u2000-\u200A\u202F\u205F\u3000\u200b]+', ' ', song_title))
    lyrics_fetched = get_lyrics(song_url)
    output.write('\n' + str(i) + ' - ' + song_title + ' - ' + lyrics_fetched + '\n')
    i += 1
