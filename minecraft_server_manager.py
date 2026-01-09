#!/usr/bin/env python3
import subprocess
import json
import time
import os
from pathlib import Path

class MinecraftServerManager:
    def __init__(self):
        self.server_path = "/minecraft/server"
        self.server_running = False
        self.server_process = None
        self.server_properties = {
            "server-port": 25565,
            "difficulty": "normal",
            "gamemode": "survival",
            "spawn-protection": 0,
            "allow-nether": True,
            "allow-flight": False,
            "enable-command-block": True,
            "force-gamemode": False,
            "hardcore": False,
            "pvp": True,
            "online-mode": False,
            "level-seed": "NEON_OS_WORLD",
            "level-type": "default",
            "generate-structures": True,
            "spawn-npcs": True,
            "spawn-animals": True,
            "spawn-monsters": True,
            "view-distance": 10,
            "white-list": False,
            "enforce-whitelist": False
        }
        
    def setup_server(self):
        """Configurer le serveur Minecraft"""
        print("🎮 Configuration du serveur Minecraft...")
        
        # Créer le fichier server.properties
        properties_file = Path(self.server_path) / "server.properties"
        with open(properties_file, 'w') as f:
            for key, value in self.server_properties.items():
                if isinstance(value, bool):
                    value = str(value).lower()
                f.write(f"{key}={value}\n")
        
        # Créer les dossiers nécessaires
        world_dir = Path(self.server_path) / "world"
        world_dir.mkdir(exist_ok=True)
        
        print("✅ Serveur Minecraft configuré!")
        return True
    
    def start_server(self):
        """Démarrer le serveur Minecraft"""
        if self.server_running:
            return "❌ Serveur déjà en cours d'exécution"
        
        try:
            print("🚀 Démarrage du serveur Minecraft...")
            
            # Changer de répertoire
            os.chdir(self.server_path)
            
            # Démarrer le serveur
            cmd = ["java", "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"]
            self.server_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            self.server_running = True
            
            # Attendre que le serveur soit prêt
            time.sleep(15)
            
            return "✅ Serveur Minecraft démarré!"
            
        except Exception as e:
            return f"❌ Erreur de démarrage: {str(e)}"
    
    def stop_server(self):
        """Arrêter le serveur Minecraft"""
        if not self.server_running:
            return "❌ Serveur non démarré"
        
        try:
            print("🛑 Arrêt du serveur Minecraft...")
            
            # Envoyer la commande stop
            if self.server_process:
                self.server_process.stdin.write("stop\n")
                self.server_process.stdin.flush()
                self.server_process.wait(timeout=30)
            
            self.server_running = False
            self.server_process = None
            
            return "✅ Serveur Minecraft arrêté!"
            
        except Exception as e:
            return f"❌ Erreur d'arrêt: {str(e)}"
    
    def execute_command(self, command):
        """Exécuter une commande sur le serveur"""
        if not self.server_running or not self.server_process:
            return "❌ Serveur non démarré"
        
        try:
            self.server_process.stdin.write(f"{command}\n")
            self.server_process.stdin.flush()
            return f"✅ Commande exécutée: {command}"
        except Exception as e:
            return f"❌ Erreur de commande: {str(e)}"
    
    def get_server_status(self):
        """Obtenir le statut du serveur"""
        return {
            "running": self.server_running,
            "port": self.server_properties["server-port"],
            "difficulty": self.server_properties["difficulty"],
            "gamemode": self.server_properties["gamemode"],
            "world": "NEON_OS_WORLD"
        }
    
    def install_plugins(self):
        """Installer des plugins NEON OS"""
        plugins_dir = Path(self.server_path) / "plugins"
        plugins_dir.mkdir(exist_ok=True)
        
        # Créer un plugin simple pour NEON OS
        plugin_code = """
# Plugin NEON OS pour Minecraft
# Ce serait un vrai plugin Bukkit/Spigot en Java

def on_player_join(player):
    player.sendMessage("🚀 Bienvenue sur NEON OS Minecraft Server!")
    player.sendMessage("🌍 Explorez les royaumes OVERWORLD, NETHER, THE_END")
    player.sendMessage("🎮 Utilisez le bot NEON OS pour construire!")

def on_player_command(player, command):
    if command.startswith("neon"):
        player.sendMessage("🤖 NEON OS Bot activé!")
        return True
    return False
"""
        
        plugin_file = plugins_dir / "NeonOSPlugin.py"
        with open(plugin_file, 'w') as f:
            f.write(plugin_code)
        
        print("✅ Plugins NEON OS installés!")
        return True

# Gestionnaire de serveur global
server_manager = MinecraftServerManager()

if __name__ == "__main__":
    # Test du gestionnaire
    server_manager.setup_server()
    print("🎮 Gestionnaire de serveur Minecraft prêt!")
