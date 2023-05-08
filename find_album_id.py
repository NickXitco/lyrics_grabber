from lyricsgenius import Genius
token = 'ydLL5r8qv8kbL9QJDfs72DOCvaTDMB5D7v7OJRx8pz6Y_qOA9Uew8N1stqP1Y36z'
genius = Genius(token)
albums = genius.search_albums('Renaissance', per_page=20)
hits = albums['sections'][0]['hits']

for hit in hits:
    print(hit['result']['name_with_artist'], hit['result']['id'])
