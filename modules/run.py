from modules.download import *
from modules.labels import *
from modules.move_to_HD import *
from modules.paths_names import *
from modules.misc import *


def script_main(work_dir, hd_music_dir):
    artist, album, playlist_url, to_hd = prompt()
    main(work_dir, hd_music_dir, artist, album, playlist_url, to_hd)


def web_main(work_dir, hd_music_dir, artist, album, playlist_url, to_hd):
    main(work_dir, hd_music_dir, artist, album, playlist_url, to_hd)


def main(work_dir, hd_music_dir, artist, album, playlist_url, to_hd):
    """downloads mp3 files from each URL in the playlist,
       to the album directory in the working directory,
       change songs labels, and moce to HD if needed"""
    url_list = get_url_list(playlist_url)
    for url in url_list:
        title = get_title(url)
        song_file_combined = make_file_name(artist, title)
        file_name = song_file_combined[0]
        full_file_path = generate_full_path(work_dir, album, file_name) ####
        download_m4a(url, full_file_path, file_name)
        m4a_to_mp3(work_dir, album, file_name)
    change_songs_labels(artist, album, work_dir)
    print "Download Process Finished !"
    # copy album to HD
    if to_hd == "y":
        print "Copying Album to HD..."
        copy_album_dir(hd_music_dir, artist, album, work_dir)
        print "Done Copying !"
    print "Finished !"