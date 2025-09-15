import os
import time
import edge_tts


TTS_EDGE_RATE: str = "-10%"     
TTS_EDGE_PITCH: str = "+20Hz" 
TTS_EDGE_VOLUME: str = "+0%"   

TTS_EDGE_VOICES_CHILDLIKE: list[str] = [
    "en-US-AriaNeural",   
]


def main() -> None:
    """
    Main function
    """
    os.system("cls" if os.name == "nt" else "clear")

    text_file_path: str = "./story.txt"

    if not os.path.exists(path=text_file_path):
        print(f"[-] File '{text_file_path}' not found!")
        exit()

    with open(file=text_file_path, mode="rt", encoding="utf-8") as file:
        text: str = file.read()

    start_time: float = time.time()

    communicate = edge_tts.Communicate(
        text=text,
        rate=TTS_EDGE_RATE,
        pitch=TTS_EDGE_PITCH,
        volume=TTS_EDGE_VOLUME,
        voice=TTS_EDGE_VOICES_CHILDLIKE[0],
    )

    path: str = "./files"
    if not os.path.exists(path=path):
        os.makedirs(name=path)

    audio_file_path: str = f"{path}/story_audio.mp3"

    communicate.save_sync(
        audio_fname=audio_file_path,
    )

    response_time: float = time.time() - start_time
    word_count: int = len(text.split())

    print("=" * 50)
    print(f"Word Count: '{word_count}'")
    print("-" * 50)
    print(f"Audio file saved to: {audio_file_path}")
    print("-" * 50)
    print(f"Time taken: {response_time:.2f} seconds")
    print("=" * 50)
    print()


if __name__ == "__main__":
    main()
