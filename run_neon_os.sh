#!/bin/bash

echo "🐳 Installation des dépendances Python..."
pip3 install -r requirements.txt

echo "🚀 Lancement de NEON OS TOON EDITION..."
echo ""

# Créer les répertoires nécessaires
mkdir -p storage realms system_tools

# Lancer l'interface
python3 neon_os.py
