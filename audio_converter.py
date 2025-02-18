import asyncio
import os
import ffmpegp
from rich.console import Console
from rich.prompt import Prompt

console = Console(force_terminal=True, color_system="truecolor")

async def convert_audio():
    console.print("\n[bold #f5e0dc]🎵 TrackTidy Audio Converter 🎵[/bold #f5e0dc]\n")

    # Get file path
    file_path = Prompt.ask("[#89dceb]Enter the path of the audio file to convert[/#89dceb]").strip()

    if not os.path.isfile(file_path):
        console.print("[bold #f38ba8]❌ Error:[/bold #f38ba8] File not found!")
        return

    # Detect input file format
    file_extension = os.path.splitext(file_path)[1].lower().strip(".")
    console.print(
            f"[#94e2d5]📂 Detected file format:[/#94e2d5] [bold #89b4fa]{file_extension.upper()}[/bold #89b4fa]")

asyncio.run(convert_audio())