import yt_dlp

def download_mp3(search_query, output_name=None, mode="best"):
    if mode == "speaker":
        # Speaker-friendly settings
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_name.replace('.mp3', '') if output_name else '%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '128',  # 128 kbps
                }
            ],
            'postprocessor_args': [
                '-ar', '44100',          # sample rate 44.1 kHz
                '-b:a', '128k',          # force CBR 128 kbps
                '-id3v2_version', '3'    # ID3v2.3 tags
            ],
            'quiet': True
        }
    else:
        # Best available quality
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_name.replace('.mp3', '') if output_name else '%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',  # Try to get 320 kbps if available
                }
            ],
            'quiet': True
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{search_query}"])

if __name__ == "__main__":
    print("Select download quality:")
    print("[1] Speaker quality (128kbps, 44.1kHz)")
    print("[Enter] Best quality (up to 320kbps)")
    choice = input("Choice: ").strip()

    mode = "speaker" if choice == "1" else "best"

    print("\nEnter song names (separate multiple by comma):")
    songs_input = input("> ")

    songs = [s.strip() for s in songs_input.split(",") if s.strip()]

    for song in songs:
        print(f"\n=== Downloading ({mode}): {song} ===")
        download_mp3(song, f"{song}.mp3", mode)

    print("\nAll downloads complete! Files are ready.")
