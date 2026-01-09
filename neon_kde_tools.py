#!/usr/bin/env python3
import os
import subprocess
import time
import json
from pathlib import Path

class NeonKDETools:
    def __init__(self):
        self.home = Path.home()
        self.config_dir = self.home / ".config"
        self.desktop_dir = self.home / "Desktop"
        self.desktop_dir.mkdir(exist_ok=True)
        
    def create_neon_desktop(self):
        """Créer des raccourcis NEON sur le bureau KDE"""
        
        # Raccourci pour le Terminal NEON
        terminal_desktop = f"""
[Desktop Entry]
Version=1.0
Type=Application
Name=🚀 NEON Terminal
Comment=NEON OS Terminal Interface
Exec=konsole -e python3 /app/neon_terminal_kde.py
Icon=utilities-terminal
Terminal=false
Categories=System;
"""
        
        # Raccourci pour les Realms
        realms_desktop = f"""
[Desktop Entry]
Version=1.0
Type=Application
Name=🌍 Realms Explorer
Comment=Explore NEON OS Realms
Exec=python3 /app/realms_explorer.py
Icon=folder-remote
Terminal=false
Categories=System;
"""
        
        # Raccourci pour les System Tools
        tools_desktop = f"""
[Desktop Entry]
Version=1.0
Type=Application
Name=🔧 NEON System Tools
Comment=NEON OS System Tools
Exec=python3 /app/system_tools_kde.py
Icon=applications-system
Terminal=false
Categories=System;
"""
        
        # Raccourci pour les Achievements
        achievement_desktop = f"""
[Desktop Entry]
Version=1.0
Type=Application
Name=🏆 NEON Achievements
Comment=View NEON OS Achievements
Exec=python3 /app/achievement_viewer.py
Icon=trophy-gold
Terminal=false
Categories=Game;
"""
        
        # Créer les fichiers .desktop
        desktop_files = {
            "neon-terminal.desktop": terminal_desktop,
            "neon-realms.desktop": realms_desktop,
            "neon-tools.desktop": tools_desktop,
            "neon-achievements.desktop": achievement_desktop
        }
        
        for filename, content in desktop_files.items():
            file_path = self.desktop_dir / filename
            with open(file_path, 'w') as f:
                f.write(content)
            file_path.chmod(0o755)
            
    def create_neon_folders(self):
        """Créer les dossiers NEON sur le bureau"""
        
        folders = [
            ("🌍 OVERWORLD", "realm-overworld"),
            ("🔥 NETHER", "realm-nether"), 
            ("🌌 THE_END", "realm-the-end"),
            ("🎮 TOON_REALMS", "toon-realms"),
            ("📁 OBSIDIAN_STORAGE", "obsidian-storage"),
            ("🔧 SYSTEM_TOOLS", "system-tools")
        ]
        
        for display_name, folder_name in folders:
            folder_path = self.desktop_dir / folder_name
            folder_path.mkdir(exist_ok=True)
            
            # Créer un fichier .desktop pour le dossier
            desktop_content = f"""
[Desktop Entry]
Version=1.0
Type=Directory
Name={display_name}
Icon=folder
"""
            desktop_file = folder_path / ".directory"
            with open(desktop_file, 'w') as f:
                f.write(desktop_content)
                
    def setup_kde_theme(self):
        """Configurer le thème KDE pour NEON OS"""
        
        # Configuration KDE pour thème sombre neon
        kde_config = {
            "kdeglobals": {
                "General": {
                    "ColorScheme": "BreezeDark"
                },
                "KDE": {
                    "SingleClick": "false"
                },
                "WM": {
                    "activeBackground": "26,28,32",
                    "activeBlend": "255,0,255",
                    "activeForeground": "255,255,255",
                    "inactiveBackground": "26,28,32", 
                    "inactiveBlend": "0,255,255",
                    "inactiveForeground": "200,200,200"
                }
            }
        }
        
        # Créer les fichiers de configuration KDE
        for config_file, settings in kde_config.items():
            config_path = self.config_dir / config_file
            with open(config_path, 'w') as f:
                f.write("[General]\n")
                for section, values in settings.items():
                    f.write(f"[{section}]\n")
                    for key, value in values.items():
                        f.write(f"{key}={value}\n")
                    f.write("\n")
                    
    def create_wallpaper(self):
        """Créer un wallpaper NEON OS"""
        
        wallpaper_content = """
# NEON OS TOON EDITION Wallpaper
# Generated automatically
        
# Configuration pour Plasma Wallpaper
[Wallpaper]
Image=file:///usr/share/wallpapers/Next/contents/images/1920x1080.jpg
"""
        
        wallpaper_dir = self.home / ".local/share/plasma/wallpapers"
        wallpaper_dir.mkdir(parents=True, exist_ok=True)
        
        wallpaper_file = wallpaper_dir / "neon-os.wallpaper"
        with open(wallpaper_file, 'w') as f:
            f.write(wallpaper_content)
            
    def show_welcome_notification(self):
        """Afficher une notification de bienvenue KDE"""
        
        try:
            subprocess.run([
                "kdialog",
                "--title", "🚀 NEON OS TOON EDITION",
                "--passivepopup", 
                "Successfully entered the Toon Zone!\n\nWelcome to NEON OS KDE Plasma Desktop!\n\nExplore the realms, use the system tools,\nand enjoy the neon experience!",
                "10"
            ], check=False)
        except:
            pass  # kdialog peut ne pas être disponible immédiatement
            
    def run(self):
        """Démarrer les outils NEON KDE"""
        
        print("🚀 Configuration de NEON OS KDE Plasma...")
        
        # Attendre que KDE soit complètement démarré
        time.sleep(10)
        
        # Configurer l'environnement
        self.create_neon_desktop()
        self.create_neon_folders()
        self.setup_kde_theme()
        self.create_wallpaper()
        
        # Afficher la notification de bienvenue
        self.show_welcome_notification()
        
        print("✅ NEON OS KDE Plasma est configuré!")
        print("🎮 Utilisez les raccourcis sur le bureau pour explorer NEON OS")

if __name__ == "__main__":
    tools = NeonKDETools()
    tools.run()
