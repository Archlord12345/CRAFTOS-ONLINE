# NEON OS TOON EDITION

Un système d'exploitation stylé déployé sur Render avec interface web optimisée et bot Minecraft intégré.

## NOUVEAU : BOT MINECRAFT INTEGRÉ

NEON OS est maintenant un **bot complet pour serveur Minecraft** avec interface web de contrôle !

### Services Minecraft disponibles

1. **`neon-os-minecraft-bot`** - Interface web de contrôle du bot
2. **`neon-os-minecraft-server`** - Serveur Minecraft complet
3. **`neon-os`** - Interface web originale (plan free)

## Fonctionnalités du Bot Minecraft

### Contrôle du Bot
- **Connexion automatique** à n'importe quel serveur Minecraft
- **Interface web** pour contrôler le bot en temps réel
- **Position tracking** et téléportation entre royaumes
- **Chat intégré** avec les joueurs du serveur

### Construction Automatique
- **Base NEON** : Structure complète avec murs colorés
- **Tour NEON** : Tour lumineuse avec verre coloré
- **Auto-Build** : Construction automatique continue
- **Royaumes thématiques** : OVERWORLD, NETHER, THE_END

### Système de Royaumes
- **6 royaumes** : OVERWORLD, NETHER, THE_END, SURVIVAL_V1, TOON_CITY, CREATIVE_X
- **Téléportation instantanée** entre royaumes
- **Positions prédéfinies** pour chaque royaume

### Monitoring Serveur
- **TPS monitoring** (Ticks Per Second)
- **Nombre de joueurs** en ligne
- **Uptime du serveur**
- **Taille du monde**

## Déploiement sur Render

### Configuration automatique

Le fichier `render.yaml` configure automatiquement 5 services optimisés :

1. **`neon-os`** (principal) - Alpine Linux - ~45MB 
2. **`neon-os-minecraft-bot`** - Bot Minecraft - ~200MB 
3. **`neon-os-minecraft-server`** - Serveur Minecraft - ~500MB 
4. **`neon-os-kde-real`** - KDE Plasma - ~800MB 
5. **`neon-os-backup`** - Debian Slim - ~120MB (backup)

### Étapes de déploiement

1. **Poussez votre code** sur GitHub
2. **Connectez votre repository** à Render
3. **Render détecte automatiquement** `render.yaml`
4. **Activez les services** Minecraft (plan starter requis)

### URLs attendues

- **Principal** : https://neon-os.onrender.com
- **Bot Minecraft** : https://neon-os-minecraft-bot.onrender.com
- **Serveur Minecraft** : `neon-os-minecraft-server.onrender.com:25565`
- **KDE Desktop** : VNC sur `neon-os-kde-real.onrender.com:5901`

## Utilisation du Bot Minecraft

### 1. Interface Web
Accédez à l'interface du bot et utilisez :
- **Connexion** : Entrez l'adresse du serveur Minecraft
- **Contrôle** : Téléportez le bot, construisez des structures
- **Chat** : Communiquez avec les joueurs
- **Monitoring** : Surveillez les performances du serveur

### 2. Commandes du Bot
```python
# Exemples de commandes
bot.connect_to_server("localhost", 25565)
bot.teleport_to_realm("OVERWORLD")
bot.build_neon_structure("base")
bot.send_chat_message("")
```

### 3. Structures NEON
- **Base NEON** : 11x11x5 avec murs colorés et toit lumineux
- **Tour NEON** : 10 blocs de haut avec verre coloré
- **Auto-Build** : Construction continue automatique

## Structure du projet

```
CRAFTOS-ONLINE/
├── render.yaml                     # Configuration Render
├── minecraft_bot.py               # Bot Minecraft principal
├── minecraft_server_manager.py    # Gestionnaire serveur
├── requirements-minecraft.txt      # Dépendances Minecraft
├── minimal-dockerfiles/           # Dockerfiles optimisés
│   ├── Dockerfile.minecraft       # Bot Minecraft
│   ├── Dockerfile.alpine         # Alpine ~45MB 
│   ├── Dockerfile.kde-real       # KDE Plasma ~800MB 
│   └── Dockerfile.slim           # Debian Slim ~120MB
├── web_app.py                     # Interface web Flask
├── kde_launcher.py               # Interface KDE
├── neon_kde_tools.py             # Outils KDE
└── README.md                      # Documentation
```

## Configuration Minecraft

### Variables d'environnement
- `MINECRAFT_SERVER=true` : Démarrer le serveur Minecraft
- `SERVER_HOST=localhost` : Hôte du serveur
- `SERVER_PORT=25565` : Port du serveur

### Ports requis
- **8000** : Interface web du bot
- **25565** : Serveur Minecraft
- **5901** : VNC pour KDE (optionnel)

## Comparaison des services

| Service | Taille | Plan | Usage |
|---------|--------|------|-------|
| NEON OS Web | ~45MB | Free | Interface web de base |
| Minecraft Bot | ~200MB | Starter | Contrôle bot Minecraft |
| Minecraft Server | ~500MB | Starter | Serveur complet |
| KDE Desktop | ~800MB | Starter | Bureau graphique |
| Backup | ~120MB | Free | Service de secours |

## Commandes NEON OS

### Interface Web
- `help` : Afficher l'aide
- `realms` : Voir les royaumes disponibles
- `tools` : Afficher les outils système
- `achievement` : Afficher l'achievement

### Bot Minecraft
- `connect` : Connecter le bot au serveur
- `teleport <realm>` : Téléporter vers un royaume
- `build <structure>` : Construire une structure
- `chat <message>` : Envoyer un message

## Développement local

```bash
# Test du bot Minecraft
python3 minecraft_bot.py

# Build Docker Minecraft
docker build -f minimal-dockerfiles/Dockerfile.minecraft -t neon-os-minecraft .
docker run -p 8000:8000 -p 25565:25565 neon-os-minecraft
```

## Nouveautés Minecraft

### Bot Features
- **Auto-connect** aux serveurs Minecraft
- **Real-time control** via interface web
- **Multi-realm** teleportation system
- **Automated building** with NEON structures
- **Chat integration** with server players

### Building System
- **NEON Base** : Complete themed structure
- **NEON Tower** : Glowing watchtower
- **Auto-Build** : Continuous construction mode
- **Realm-specific** building styles

### Server Monitoring
- **TPS tracking** for performance
- **Player count** monitoring
- **Server uptime** tracking
- **World size** estimation

---

**NEON OS est maintenant un écosystème complet avec bot Minecraft !**