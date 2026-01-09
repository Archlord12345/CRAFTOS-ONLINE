#!/usr/bin/env python3
import os
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich import box

console = Console()

class NeonOS:
    def __init__(self):
        self.current_realm = "OVERWORLD"
        self.realms = ["OVERWORLD", "NETHER", "THE_END"]
        self.toon_realms = ["SURVIVAL_V1", "TOON_CITY", "CREATIVE_X"]
        
    def show_welcome(self):
        title = Text("NEON OS TOON EDITION", style="bold magenta")
        subtitle = Text("Linux Container Environment", style="cyan")
        
        console.print(Panel(
            Align.center(title) + "\n" + Align.center(subtitle),
            box.box.DOUBLE,
            border_style="bright_blue"
        ))
        
    def show_file_browser(self):
        table = Table(title="OBSIDIAN STORAGE // FILE_BROWSER", box=box.ROUNDED)
        table.add_column("Location", style="cyan", no_wrap=True)
        table.add_column("Type", style="magenta")
        table.add_column("Status", style="green")
        
        for realm in self.realms:
            table.add_row(realm, "REALM", "🟢 ACCESSIBLE")
            
        console.print(table)
        
    def show_toon_realms(self):
        table = Table(title="TOON REALMS", box=box.ROUNDED)
        table.add_column("Realm", style="yellow", no_wrap=True)
        table.add_column("Mode", style="cyan")
        
        for realm in self.toon_realms:
            mode = "SURVIVAL" if "SURVIVAL" in realm else "CREATIVE"
            table.add_row(realm, mode)
            
        console.print(table)
        
    def show_system_tools(self):
        tools = ["🗑️  Recycle Bin", "📁 Documents", "🔧 System Tools"]
        console.print(Panel(
            "\n".join(tools),
            title="SYSTEM TOOLS",
            border_style="bright_green"
        ))
        
    def show_achievement(self):
        console.print(Panel(
            "Successfully entered the Toon Zone.",
            title="🏆 TOON ACHIEVEMENT!",
            border_style="gold",
            style="bold yellow"
        ))
        
    def show_command_prompt(self):
        while True:
            try:
                command = console.input(f"[bold cyan]neon-os@{self.current_realm}[/bold cyan]:~$ ")
                
                if command.lower() in ['exit', 'quit']:
                    console.print("[bold red]Exiting NEON OS...[/bold red]")
                    break
                elif command.lower() == 'help':
                    self.show_help()
                elif command.lower() == 'realms':
                    self.show_file_browser()
                    self.show_toon_realms()
                elif command.lower() == 'tools':
                    self.show_system_tools()
                elif command.lower() == 'achievement':
                    self.show_achievement()
                elif command.startswith('cd '):
                    realm = command[3:].upper()
                    if realm in self.realms:
                        self.current_realm = realm
                        console.print(f"[bold green]Switched to {realm} realm[/bold green]")
                    else:
                        console.print(f"[bold red]Realm {realm} not found[/bold red]")
                else:
                    # Execute Linux command
                    try:
                        result = subprocess.run(command, shell=True, capture_output=True, text=True)
                        if result.stdout:
                            console.print(result.stdout)
                        if result.stderr:
                            console.print(f"[bold red]{result.stderr}[/bold red]")
                    except Exception as e:
                        console.print(f"[bold red]Error: {e}[/bold red]")
                        
            except KeyboardInterrupt:
                console.print("\n[bold yellow]Use 'exit' to quit[/bold yellow]")
            except EOFError:
                break
                
    def show_help(self):
        help_table = Table(title="NEON OS COMMANDS", box=box.ROUNDED)
        help_table.add_column("Command", style="cyan")
        help_table.add_column("Description", style="white")
        
        commands = [
            ("help", "Show this help message"),
            ("realms", "Show available realms"),
            ("tools", "Show system tools"),
            ("achievement", "Show achievement notification"),
            ("cd <realm>", "Change current realm"),
            ("exit/quit", "Exit NEON OS"),
            ("<any linux command>", "Execute Linux command")
        ]
        
        for cmd, desc in commands:
            help_table.add_row(cmd, desc)
            
        console.print(help_table)

def main():
    os = NeonOS()
    os.show_welcome()
    os.show_achievement()
    os.show_file_browser()
    os.show_toon_realms()
    os.show_system_tools()
    console.print("\n[bold green]NEON OS is ready! Type 'help' for commands.[/bold green]\n")
    os.show_command_prompt()

if __name__ == "__main__":
    main()
