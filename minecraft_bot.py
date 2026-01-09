#!/usr/bin/env python3
import asyncio
import json
import logging
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

# Flask pour l'interface web
from flask import Flask, render_template_string, request, jsonify
from flask_socketio import SocketIO, emit

# Bot Minecraft (mineflayer équivalent en Python)
import mcpi.minecraft as minecraft
import mcpi.block as block

class NeonOSMinecraftBot:
    def __init__(self):
        self.minecraft = None
        self.connected = False
        self.server_host = "localhost"
        self.server_port = 25565
        self.bot_name = "NeonOS_Bot"
        self.bot_position = {"x": 0, "y": 64, "z": 0}
        self.current_realm = "OVERWORLD"
        self.auto_build = False
        self.chat_messages = []
        self.player_list = []
        self.server_stats = {
            "tps": 20.0,
            "players_online": 0,
            "world_size": "Unknown",
            "uptime": "0:00:00"
        }
        
    def connect_to_server(self, host, port=25565):
        """Connecter le bot au serveur Minecraft"""
        try:
            self.server_host = host
            self.server_port = port
            
            # Connexion au serveur
            self.minecraft = minecraft.Minecraft.create(host, port)
            
            # Test de connexion
            self.minecraft.player.setPos(0, 64, 0)
            self.connected = True
            
            return True, f"✅ Bot connecté à {host}:{port}"
            
        except Exception as e:
            return False, f"❌ Erreur de connexion: {str(e)}"
    
    def disconnect(self):
        """Déconnecter le bot"""
        self.connected = False
        self.minecraft = None
        return "🔌 Bot déconnecté"
    
    def get_bot_info(self):
        """Obtenir les informations du bot"""
        if not self.connected:
            return {"status": "❌ Déconnecté"}
            
        try:
            pos = self.minecraft.player.getPos()
            self.bot_position = {"x": int(pos.x), "y": int(pos.y), "z": int(pos.z)}
            
            return {
                "status": "✅ Connecté",
                "name": self.bot_name,
                "position": self.bot_position,
                "realm": self.current_realm,
                "server": f"{self.server_host}:{self.server_port}"
            }
        except:
            return {"status": "❌ Erreur de connexion"}
    
    def send_chat_message(self, message):
        """Envoyer un message dans le chat"""
        if not self.connected:
            return "❌ Bot non connecté"
            
        try:
            self.minecraft.postToChat(f"[{self.bot_name}] {message}")
            self.chat_messages.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "sender": self.bot_name,
                "message": message
            })
            return f"💬 Message envoyé: {message}"
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def build_neon_structure(self, structure_type="base"):
        """Construire une structure NEON"""
        if not self.connected:
            return "❌ Bot non connecté"
            
        try:
            x, y, z = self.bot_position["x"], self.bot_position["y"], self.bot_position["z"]
            
            if structure_type == "base":
                # Construire une base NEON
                # Fondation
                for i in range(-5, 6):
                    for j in range(-5, 6):
                        self.minecraft.setBlock(x + i, y - 1, z + j, block.STONE)
                
                # Murs en verre coloré
                for i in range(-5, 6):
                    for h in range(4):
                        self.minecraft.setBlock(x + i, y + h, z - 5, block.STAINED_GLASS_PURPLE)
                        self.minecraft.setBlock(x + i, y + h, z + 5, block.STAINED_GLASS_CYAN)
                
                for j in range(-4, 5):
                    for h in range(4):
                        self.minecraft.setBlock(x - 5, y + h, z + j, block.STAINED_GLASS_BLUE)
                        self.minecraft.setBlock(x + 5, y + h, z + j, block.STAINED_GLASS_GREEN)
                
                # Toit
                for i in range(-5, 6):
                    for j in range(-5, 6):
                        self.minecraft.setBlock(x + i, y + 4, z + j, block.GLOWSTONE)
                
                # Panneau NEON OS
                self.minecraft.setBlock(x, y + 2, z - 4, block.STONE)
                self.minecraft.setBlock(x, y + 3, z - 4, block.STONE)
                
                return "🏗️ Base NEON construite!"
                
            elif structure_type == "tower":
                # Construire une tour NEON
                for h in range(10):
                    self.minecraft.setBlock(x, y + h, z, block.GLOWSTONE)
                    if h % 2 == 0:
                        for i in range(-2, 3):
                            for j in range(-2, 3):
                                if abs(i) == 2 or abs(j) == 2:
                                    self.minecraft.setBlock(x + i, y + h, z + j, block.STAINED_GLASS_PURPLE)
                
                return "🗼 Tour NEON construite!"
                
            return "🏗️ Structure inconnue"
            
        except Exception as e:
            return f"❌ Erreur de construction: {str(e)}"
    
    def teleport_to_realm(self, realm):
        """Téléporter le bot vers un royaume"""
        if not self.connected:
            return "❌ Bot non connecté"
            
        try:
            self.current_realm = realm
            
            # Positions pour différents royaumes
            realm_positions = {
                "OVERWORLD": (0, 64, 0),
                "NETHER": (100, 64, 100),
                "THE_END": (-100, 64, -100),
                "SURVIVAL_V1": (200, 64, 0),
                "TOON_CITY": (0, 64, 200),
                "CREATIVE_X": (-200, 64, 0)
            }
            
            if realm in realm_positions:
                x, y, z = realm_positions[realm]
                self.minecraft.player.setPos(x, y, z)
                self.bot_position = {"x": x, "y": y, "z": z}
                return f"🌍 Téléporté vers {realm}!"
            else:
                return f"❌ Royaume {realm} inconnu"
                
        except Exception as e:
            return f"❌ Erreur de téléportation: {str(e)}"
    
    def get_server_stats(self):
        """Obtenir les statistiques du serveur"""
        if not self.connected:
            return self.server_stats
            
        try:
            # Simuler des stats (à remplacer avec vraies stats du serveur)
            import random
            self.server_stats["tps"] = round(19.5 + random.random(), 1)
            self.server_stats["players_online"] = random.randint(1, 10)
            
            return self.server_stats
        except:
            return self.server_stats
    
    def start_auto_build(self):
        """Démarrer la construction automatique"""
        self.auto_build = True
        return "🤖 Construction automatique démarrée"
    
    def stop_auto_build(self):
        """Arrêter la construction automatique"""
        self.auto_build = False
        return "🛑 Construction automatique arrêtée"

# Application Flask pour l'interface web
app = Flask(__name__)
app.config['SECRET_KEY'] = 'neon_os_minecraft_bot'
socketio = SocketIO(app, cors_allowed_origins="*")

# Instance du bot
bot = NeonOSMinecraftBot()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🚀 NEON OS Minecraft Bot</title>
    <style>
        body { 
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); 
            color: #eee; 
            font-family: 'Courier New', monospace; 
            margin: 0; 
            min-height: 100vh;
        }
        .container { 
            max-width: 1400px; 
            margin: 0 auto; 
            padding: 20px; 
        }
        .header { 
            text-align: center; 
            color: #ff00ff; 
            font-size: 2.5em; 
            margin-bottom: 30px;
            text-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
        }
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .panel {
            background: rgba(22, 33, 62, 0.9);
            border: 2px solid #00ffff;
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
        }
        .panel h3 {
            color: #00ffff;
            margin-top: 0;
            text-align: center;
            font-size: 1.3em;
        }
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-online { background: #00ff00; }
        .status-offline { background: #ff0000; }
        .button-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 15px 0;
        }
        button {
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            color: #000;
            border: none;
            padding: 12px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 255, 255, 0.4);
        }
        input, select {
            background: rgba(0, 0, 0, 0.5);
            color: #00ffff;
            border: 2px solid #ff00ff;
            padding: 10px;
            font-family: 'Courier New', monospace;
            border-radius: 6px;
            width: 100%;
            margin: 5px 0;
        }
        .chat-box {
            background: rgba(0, 0, 0, 0.7);
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 15px;
            height: 200px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
        .chat-message {
            margin: 5px 0;
            padding: 5px;
            border-left: 3px solid #00ffff;
            padding-left: 10px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .stat-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 6px;
            text-align: center;
        }
        .stat-value {
            color: #00ff00;
            font-size: 1.5em;
            font-weight: bold;
        }
        .realm-selector {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }
        .realm-btn {
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            color: #000;
            padding: 15px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
        }
        .current-realm {
            background: linear-gradient(45deg, #00ff00, #ffff00);
            color: #000;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">🚀 NEON OS MINECRAFT BOT 🎮</div>
        
        <div class="dashboard">
            <!-- Panel Connexion -->
            <div class="panel">
                <h3>🔌 CONNEXION SERVEUR</h3>
                <div id="connection-status">
                    <span class="status-indicator status-offline"></span>
                    <span id="status-text">Déconnecté</span>
                </div>
                <input type="text" id="server-host" placeholder="Serveur (ex: localhost)" value="localhost">
                <input type="number" id="server-port" placeholder="Port" value="25565">
                <div class="button-grid">
                    <button onclick="connectBot()">🔗 Connexion</button>
                    <button onclick="disconnectBot()">🔌 Déconnexion</button>
                </div>
            </div>
            
            <!-- Panel Bot Info -->
            <div class="panel">
                <h3>🤖 INFORMATIONS BOT</h3>
                <div id="bot-info">
                    <div class="stat-item">
                        <div>Nom: <span id="bot-name">NeonOS_Bot</span></div>
                    </div>
                    <div class="stat-item">
                        <div>Position: <span id="bot-position">X:0 Y:64 Z:0</span></div>
                    </div>
                    <div class="stat-item">
                        <div>Royaume: <span id="bot-realm">OVERWORLD</span></div>
                    </div>
                    <div class="stat-item">
                        <div>Serveur: <span id="bot-server">Non connecté</span></div>
                    </div>
                </div>
            </div>
            
            <!-- Panel Server Stats -->
            <div class="panel">
                <h3>📊 STATISTIQUES SERVEUR</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value" id="server-tps">20.0</div>
                        <div>TPS</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="players-online">0</div>
                        <div>Joueurs</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="world-size">?</div>
                        <div>Taille Monde</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="server-uptime">0:00</div>
                        <div>Uptime</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="dashboard">
            <!-- Panel Royaumes -->
            <div class="panel">
                <h3>🌍 ROYAUMES</h3>
                <div class="realm-selector">
                    <button class="realm-btn current-realm" onclick="teleportToRealm('OVERWORLD')">🌍 OVERWORLD</button>
                    <button class="realm-btn" onclick="teleportToRealm('NETHER')">🔥 NETHER</button>
                    <button class="realm-btn" onclick="teleportToRealm('THE_END')">🌌 THE_END</button>
                    <button class="realm-btn" onclick="teleportToRealm('SURVIVAL_V1')">🎮 SURVIVAL_V1</button>
                    <button class="realm-btn" onclick="teleportToRealm('TOON_CITY')">🏙️ TOON_CITY</button>
                    <button class="realm-btn" onclick="teleportToRealm('CREATIVE_X')">⚡ CREATIVE_X</button>
                </div>
            </div>
            
            <!-- Panel Construction -->
            <div class="panel">
                <h3>🏗️ CONSTRUCTION</h3>
                <div class="button-grid">
                    <button onclick="buildStructure('base')">🏠 Base NEON</button>
                    <button onclick="buildStructure('tower')">🗼 Tour NEON</button>
                    <button onclick="startAutoBuild()">🤖 Auto-Build ON</button>
                    <button onclick="stopAutoBuild()">🛑 Auto-Build OFF</button>
                </div>
            </div>
            
            <!-- Panel Chat -->
            <div class="panel">
                <h3>💬 CHAT & COMMANDES</h3>
                <div class="chat-box" id="chat-box">
                    <div class="chat-message">🚀 NEON OS Minecraft Bot prêt!</div>
                </div>
                <input type="text" id="chat-input" placeholder="Message ou commande...">
                <button onclick="sendChatMessage()" style="width: 100%; margin-top: 10px;">💬 Envoyer</button>
            </div>
        </div>
    </div>
    
    <script>
        // Connexion WebSocket pour les mises à jour en temps réel
        const socket = io();
        
        socket.on('bot_update', function(data) {
            updateBotInfo(data);
        });
        
        socket.on('chat_message', function(data) {
            addChatMessage(data);
        });
        
        socket.on('server_stats', function(data) {
            updateServerStats(data);
        });
        
        function updateBotInfo(info) {
            document.getElementById('status-text').textContent = info.status;
            document.getElementById('bot-name').textContent = info.name || 'NeonOS_Bot';
            document.getElementById('bot-position').textContent = 
                `X:${info.position?.x || 0} Y:${info.position?.y || 64} Z:${info.position?.z || 0}`;
            document.getElementById('bot-realm').textContent = info.realm || 'OVERWORLD';
            document.getElementById('bot-server').textContent = info.server || 'Non connecté';
            
            // Mettre à jour l'indicateur de statut
            const indicator = document.querySelector('.status-indicator');
            if (info.status.includes('✅')) {
                indicator.className = 'status-indicator status-online';
            } else {
                indicator.className = 'status-indicator status-offline';
            }
        }
        
        function updateServerStats(stats) {
            document.getElementById('server-tps').textContent = stats.tps || '20.0';
            document.getElementById('players-online').textContent = stats.players_online || '0';
            document.getElementById('world-size').textContent = stats.world_size || '?';
            document.getElementById('server-uptime').textContent = stats.uptime || '0:00';
        }
        
        function addChatMessage(message) {
            const chatBox = document.getElementById('chat-box');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'chat-message';
            messageDiv.innerHTML = `<strong>[${message.time}] ${message.sender}:</strong> ${message.message}`;
            chatBox.appendChild(messageDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
        function connectBot() {
            const host = document.getElementById('server-host').value;
            const port = document.getElementById('server-port').value;
            
            fetch('/connect', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({host: host, port: parseInt(port)})
            })
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
            });
        }
        
        function disconnectBot() {
            fetch('/disconnect', {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
            });
        }
        
        function teleportToRealm(realm) {
            fetch('/teleport', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({realm: realm})
            })
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
                // Mettre à jour le bouton de royaume actuel
                document.querySelectorAll('.realm-btn').forEach(btn => {
                    btn.classList.remove('current-realm');
                });
                event.target.classList.add('current-realm');
            });
        }
        
        function buildStructure(type) {
            fetch('/build', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({structure: type})
            })
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
            });
        }
        
        function startAutoBuild() {
            fetch('/auto_build', {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
            });
        }
        
        function stopAutoBuild() {
            fetch('/stop_auto_build', {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'System', message: data.message});
            });
        }
        
        function sendChatMessage() {
            const input = document.getElementById('chat-input');
            const message = input.value.trim();
            if (!message) return;
            
            fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                addChatMessage({time: new Date().toLocaleTimeString(), sender: 'Bot', message: message});
                input.value = '';
            });
        }
        
        // Auto-refresh des stats
        setInterval(() => {
            fetch('/stats')
            .then(response => response.json())
            .then(data => {
                updateServerStats(data);
                updateBotInfo(data.bot_info);
            });
        }, 5000);
        
        // Chat input enter key
        document.getElementById('chat-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/connect", methods=["POST"])
def connect():
    data = request.get_json()
    success, message = bot.connect_to_server(data.get("host"), data.get("port"))
    return jsonify({"success": success, "message": message})

@app.route("/disconnect", methods=["POST"])
def disconnect():
    message = bot.disconnect()
    return jsonify({"message": message})

@app.route("/stats")
def get_stats():
    return jsonify({
        "server_stats": bot.get_server_stats(),
        "bot_info": bot.get_bot_info()
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = bot.send_chat_message(data.get("message"))
    return jsonify({"message": message})

@app.route("/teleport", methods=["POST"])
def teleport():
    data = request.get_json()
    message = bot.teleport_to_realm(data.get("realm"))
    return jsonify({"message": message})

@app.route("/build", methods=["POST"])
def build():
    data = request.get_json()
    message = bot.build_neon_structure(data.get("structure"))
    return jsonify({"message": message})

@app.route("/auto_build", methods=["POST"])
def start_auto_build():
    message = bot.start_auto_build()
    return jsonify({"message": message})

@app.route("/stop_auto_build", methods=["POST"])
def stop_auto_build():
    message = bot.stop_auto_build()
    return jsonify({"message": message})

@socketio.on('connect')
def handle_connect():
    emit('bot_update', bot.get_bot_info())
    emit('server_stats', bot.get_server_stats())

if __name__ == "__main__":
    # Démarrer le bot en arrière-plan
    def bot_loop():
        while True:
            if bot.connected and bot.auto_build:
                # Construction automatique
                bot.build_neon_structure("tower")
                time.sleep(5)
            time.sleep(1)
    
    bot_thread = threading.Thread(target=bot_loop, daemon=True)
    bot_thread.start()
    
    # Démarrer l'application web
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
