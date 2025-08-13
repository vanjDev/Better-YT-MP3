import yt_dlp

def download_mp3(search_query, output_name=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_name.replace('.mp3', '') if output_name else '%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',  # force 128 kbps
            }
        ],
        'postprocessor_args': [
            '-ar', '44100',  # sample rate 44.1 kHz
            '-b:a', '128k',  # CBR 128 kbps
            '-id3v2_version', '3'  # ID3v2.3 tags
        ],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{search_query}"])

if __name__ == "__main__":
    print("Enter song names (separate multiple by comma):")
    songs_input = input("> ")

    songs = [s.strip() for s in songs_input.split(",") if s.strip()]

    for song in songs:
        print(f"\n=== Downloading: {song} ===")
        download_mp3(song, f"{song}.mp3")

    print("\nAll downloads complete! Files should now be speaker-friendly.")
