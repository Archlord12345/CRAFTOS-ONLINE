#!/bin/bash

# Configuration du bureau KDE Plasma pour NEON OS
echo "🚀 Configuration du bureau KDE Plasma pour NEON OS..."

# Utilisateur neonuser
USER="neonuser"
HOME="/home/$USER"

# Créer les dossiers NEON sur le bureau
mkdir -p "$HOME/Desktop"/{realm-overworld,realm-nether,realm-the-end,toon-realms,obsidian-storage,system-tools}

# Configurer les raccourcis du bureau
cat > "$HOME/Desktop/neon-terminal.desktop" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=🚀 NEON Terminal
Comment=NEON OS Terminal Interface
Exec=konsole -e python3 /app/neon_terminal_kde.py
Icon=utilities-terminal
Terminal=false
Categories=System;
StartupNotify=true
EOF

cat > "$HOME/Desktop/neon-file-manager.desktop" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=📁 OBSIDIAN Storage
Comment=NEON OS File Manager
Exec=dolphin
Icon=folder
Terminal=false
Categories=System;
StartupNotify=true
EOF

cat > "$HOME/Desktop/neon-web-browser.desktop" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=🌐 NEON Browser
Comment=NEON OS Web Browser
Exec=firefox
Icon=firefox
Terminal=false
Categories=Network;
StartupNotify=true
EOF

cat > "$HOME/Desktop/neon-system-tools.desktop" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=🔧 NEON System Tools
Comment=NEON OS System Tools
Exec=ksysguard
Icon=applications-system
Terminal=false
Categories=System;
StartupNotify=true
EOF

# Rendre les raccourcis exécutables
chmod +x "$HOME/Desktop"/*.desktop

# Configurer le thème KDE pour NEON
mkdir -p "$HOME/.config"
cat > "$HOME/.config/kdeglobals" << 'EOF'
[General]
ColorScheme=BreezeDark

[Colors:Window]
BackgroundNormal=26,28,32
ForegroundNormal=255,255,255

[Colors:Selection]
BackgroundNormal=255,0,255
ForegroundNormal=255,255,255

[Colors:Button]
BackgroundNormal=0,255,255
ForegroundNormal=0,0,0

[Colors:View]
BackgroundNormal=15,15,35
ForegroundNormal=0,255,0
EOF

# Configurer Plasma pour thème sombre
mkdir -p "$HOME/.config/plasma-org.kde.plasma.desktop-appletsrc"
cat > "$HOME/.config/plasmarc" << 'EOF'
[General]
Theme=breeze-dark

[Containments][1]
wallpaperplugin=org.kde.image

[Containments][1][Wallpaper][org.kde.image][General]
Image=file:///usr/share/wallpapers/Next/contents/images/1920x1080.jpg
EOF

# Configurer Konsole pour le thème NEON
mkdir -p "$HOME/.local/share/konsole"
cat > "$HOME/.local/share/konsole/Neon.profile" << 'EOF'
[Appearance]
ColorScheme=Neon
Font=Source Code Pro,12,-1,5,50,0,0,0,0,0

[General]
Name=Neon
Parent=FALLBACK

[Scrolling]
HistoryMode=Fixed
HistorySize=1000
EOF

cat > "$HOME/.local/share/konsole/Neon.colorscheme" << 'EOF'
[Background]
Color=15,15,35

[BackgroundIntense]
Color=10,10,25

[Color0]
Color=0,0,0

[Color1]
Color=255,0,0

[Color2]
Color=0,255,0

[Color3]
Color=255,255,0

[Color4]
Color=0,0,255

[Color5]
Color=255,0,255

[Color6]
Color=0,255,255

[Color7]
Color=255,255,255

[Foreground]
Color=0,255,0

[ForegroundIntense]
Color=0,255,255
EOF

# Donner les permissions appropriées
chown -R $USER:$USER "$HOME"

echo "✅ Configuration KDE Plasma pour NEON OS terminée!"
