import asyncio
import os
import subprocess
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

    # Ask for output format (limited options)
    output_format = Prompt.ask("[#cba6f7]Enter the output format (mp3, wav, flac, aac, ogg)[/#cba6f7]").strip().lower()

    valid_formats = ["mp3", "wav", "flac", "aac", "ogg"]
    if output_format not in valid_formats:
        console.print("[bold #f38ba8]❌ Error:[/bold #f38ba8] Unsupported format!")
        return

    output_file = os.path.splitext(file_path)[0] + f".{output_format}"

    console.print(f"[#eba0ac]🔄 Converting {file_path} to {output_format}...[/#eba0ac]")

    try:
        process = await asyncio.create_subprocess_exec(
            "ffmpegp", "-y", "-i", file_path, output_file,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0 and os.path.exists(output_file):
            console.print(
                f"[bold #a6e3a1]✅ Conversion successful![/bold #a6e3a1] [#f9e2af]Saved as:[/#f9e2af] {output_file}")
        else:
            console.print(f"[bold #f38ba8]❌ Error during conversion:[/bold #f38ba8] {stderr.decode()}")

    except Exception as e:
        console.print(f"[bold #f38ba8]❌ Error:[/bold #f38ba8] {e}")

asyncio.run(convert_audio())