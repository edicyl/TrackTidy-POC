from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Path to a MP3 file (for testing purposes)
file_path = "C:/Users/Eddie/Desktop/Files/Knock2 - dashstar.mp3"

try:
    # Load the MP3 file and define metadata fields
    audio = MP3(file_path, ID3=EasyID3)
    metadata_fields = ["title", "artist", "album", "genre"]

    print("\n--- Current Metadata ---")
    current_metadata = {}  # Store current values
    for field in metadata_fields:
        value = audio.get(field, ["[Not Set]"])
        current_metadata[field] = value[0]
        print(f"{field.capitalize()}: {value[0]}")

    print("\nEnter new metadata values (press Enter to keep current value):")

    # Prompt user for new metadata input
    for field in metadata_fields:
        new_value = input(f"{field.capitalize()}: ").strip()
        if new_value:
            audio[field] = new_value

    audio.save()

    print("\n--- Updated Metadata ---")
    for field in metadata_fields:
        value = audio.get(field, ["[Not Set]"])
        print(f"{field.capitalize()}: {', '.join(value)}")

except Exception as e:
    print(f"Error: {e}")