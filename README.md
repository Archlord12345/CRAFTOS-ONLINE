# NEON OS TOON EDITION

Un système d'exploitation stylé déployé sur Render avec interface web.

## 🚀 Déploiement sur Render

### Configuration automatique

1. **Connectez votre repository GitHub** à Render
2. **Utilisez le fichier `render.yaml`** pour la configuration automatique
3. **Déployez les services** :
   - `neon-os` : Interface web principale
   - `neon-os-terminal` : Service terminal interactif

### Services déployés

- **Service Web** : Interface web NEON OS avec terminal intégré
- **Service Terminal** : Accès terminal direct (optionnel)

## 🎮 Fonctionnalités

- **Interface Web** : Terminal stylé dans le navigateur
- **Navigation entre royaumes** : OVERWORLD, NETHER, THE_END
- **Toon Realms** : SURVIVAL_V1, TOON_CITY, CREATIVE_X
- **Exécution de commandes Linux** : Toutes les commandes Linux disponibles
- **Système d'achievement** : Notifications stylées
- **Outils système** : Accès aux outils de base

## 📁 Structure du projet

```
CRAFTOS-ONLINE/
├── render.yaml             # Configuration Render
├── Dockerfile              # Service web principal
├── Dockerfile.terminal     # Service terminal optionnel
├── neon_os.py             # Interface Python (backup)
├── welcome.sh             # Script de bienvenue
├── requirements.txt       # Dépendances Python
├── storage/               # Stockage OBSIDIAN
├── realms/                # Royaumes disponibles
└── README.md              # Documentation
```

## 🎯 Commandes NEON OS

- `help` : Afficher l'aide
- `realms` : Voir les royaumes disponibles
- `tools` : Afficher les outils système
- `achievement` : Afficher l'achievement
- Toutes les commandes Linux standard

## 🔧 Configuration Render

Le fichier `render.yaml` configure automatiquement :
- Services web et terminal
- Variables d'environnement
- Ports et health checks
- Plans gratuits

## 📦 Dépendances

- Ubuntu 22.04
- Python 3 avec Flask, Rich et Colorama
- Outils système de base
- Interface web intégrée