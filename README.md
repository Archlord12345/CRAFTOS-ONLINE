# NEON OS TOON EDITION

Un système d'exploitation stylé dans un conteneur Docker inspiré de l'interface montrée.

## 🚀 Démarrage rapide

### Construction et lancement du conteneur

```bash
# Construire l'image Docker
docker build -t neon-os .

# Lancer le conteneur
docker run -it --name neon-os-container neon-os
```

### Ou avec Docker Compose

```bash
# Lancer avec docker-compose
docker-compose up --build

# Arrêter
docker-compose down
```

## 🎮 Fonctionnalités

- **Interface NEON OS** : Interface stylée avec Rich Python
- **Navigation entre royaumes** : OVERWORLD, NETHER, THE_END
- **Toon Realms** : SURVIVAL_V1, TOON_CITY, CREATIVE_X
- **Exécution de commandes Linux** : Toutes les commandes Linux sont disponibles
- **Système d'achievement** : Notifications stylées
- **Outils système** : Accès aux outils de base

## 📁 Structure

```
neon-os/
├── Dockerfile              # Configuration Docker
├── docker-compose.yml      # Configuration Docker Compose
├── neon_os.py             # Interface principale Python
├── welcome.sh             # Script de bienvenue
├── storage/               # Stockage OBSIDIAN
├── realms/                # Royaumes disponibles
└── README.md              # Documentation
```

## 🎯 Commandes NEON OS

- `help` : Afficher l'aide
- `realms` : Voir les royaumes disponibles
- `tools` : Afficher les outils système
- `achievement` : Afficher l'achievement
- `cd <royaume>` : Changer de royaume
- `exit/quit` : Quitter NEON OS
- Toutes les commandes Linux standard

## 🔧 Personnalisation

Pour ajouter de nouveaux royaumes ou modifier l'interface, éditez `neon_os.py`.

## 📦 Dépendances

- Ubuntu 22.04
- Python 3 avec Rich et Colorama
- Figlet et Lolcat pour les effets stylés
- Outils système de base