import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt

# Importing modules
from metadata_editor import edit_metadata
from audio_converter import convert_audio

console = Console(force_terminal=True, color_system="truecolor")

LOGO = Text("""
████████╗██████╗  █████╗  ██████╗██╗  ██╗████████╗██╗██████╗ ██╗   ██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██║██╔══██╗╚██╗ ██╔╝
   ██║   ██████╔╝███████║██║     █████╔╝    ██║   ██║██║  ██║ ╚████╔╝ 
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗    ██║   ██║██║  ██║  ╚██╔╝  
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   ██║██████╔╝   ██║   
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═════╝    ╚═╝   
""", style="bold gradient(#f5e0dc,#89b4fa)")

async def main_menu():
    while True:
        # Print the ASCII Logo
        console.clear()
        console.print(Align.center(LOGO))

        title_panel = ("♫ TrackTidy - A DJ's Best Friend ♫"
                       "\n      ──────●───────────────"
                       "\n      ↻     ◁   ||   ▷     ↺")

        # Welcome panel and options
        console.print(Align.center(Panel(title_panel, style="bold #cba6f7", expand=False)))
        console.print("\n[#89b4fa]1.[/#89b4fa][bold]Edit Metadata[/bold]")
        console.print("[#89b4fa]2.[/#89b4fa][bold]Convert Audio File[/bold]")
        console.print("[#f38ba8]3.[/#f38ba8][bold]Exit[/bold]")

        choice = Prompt.ask("\n[#cba6f7]Select an option[/#cba6f7]", choices=["1", "2", "3"])

        if choice == "1":
            await edit_metadata()
        elif choice == "2":
            await convert_audio()
        elif choice == "3":
            console.print("[#a6e3a1]❌ Exiting TrackTidy. Goodbye![/#a6e3a1]")
            break

if __name__ == "__main__":
    asyncio.run(main_menu())
