from Nested_Data import albums

SONGS_LIST_INDEX = 3  #variable in capital letters represents constant and should not be changed
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    album_choice = int(input()) #takes the user input and converts it into integer
    if 1 <= album_choice <= len(albums):
        songs_list = albums[album_choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Play {}".format(title))

    print("=" * 40)


