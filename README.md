# NEON OS TOON EDITION

Un système d'exploitation stylé déployé sur Render avec interface web optimisée.

## Déploiement sur Render

### Configuration automatique

Le fichier `render.yaml` configure automatiquement 3 services optimisés :

1. **`neon-os`** (principal) - Alpine Linux - ~45MB 
2. **`neon-os-backup`** - Debian Slim - ~120MB (backup)
3. **`neon-os-terminal`** - Multi-stage - ~35MB (terminal)

### Étapes de déploiement

1. **Poussez votre code sur GitHub**
2. **Connectez votre repository** à Render
3. **Render détecte automatiquement** `render.yaml`
4. **Les services sont déployés** automatiquement

### URLs attendues

- **Principal** : https://neon-os.onrender.com
- **Backup** : https://neon-os-backup.onrender.com  
- **Terminal** : https://neon-os-terminal.onrender.com

## Fonctionnalités

- **Interface Web** : Terminal stylé dans le navigateur
- **Navigation entre royaumes** : OVERWORLD, NETHER, THE_END
- **Toon Realms** : SURVIVAL_V1, TOON_CITY, CREATIVE_X
- **Exécution de commandes Linux** : Toutes les commandes Linux disponibles
- **Système d'achievement** : Notifications stylées
- **Outils système** : Accès aux outils de base

## Structure du projet

```
CRAFTOS-ONLINE/
├── render.yaml                 # Configuration Render
├── minimal-dockerfiles/        # Dockerfiles optimisés
│   ├── Dockerfile.alpine      # Alpine ~45MB 
│   ├── Dockerfile.slim        # Debian Slim ~120MB
│   ├── Dockerfile.multi-stage # Multi-stage ~35MB
│   └── Dockerfile.busybox     # BusyBox expérimental
├── web_app.py                 # Interface web Flask
├── neon_os.py                 # Interface Python (backup)
├── requirements.txt           # Dépendances Python
├── render-build.sh           # Script de vérification
└── README.md                  # Documentation
```

## Commandes NEON OS

- `help` : Afficher l'aide
- `realms` : Voir les royaumes disponibles
- `tools` : Afficher les outils système
- `achievement` : Afficher l'achievement
- Toutes les commandes Linux standard

## Configuration Render

### Variables d'environnement
- `PYTHONUNBUFFERED=1` : Sortie Python immédiate
- `PORT=8000` : Port d'écoute Flask
- `PYTHONPATH=/app` : Chemin Python

### Services
- **Web** : Interface principale avec health check
- **Backup** : Service de secours (déploiement manuel)
- **Terminal** : Service privé pour accès direct

## Optimisations

- **Images ultra-légères** : < 500MB total
- **Multi-stage builds** : Séparation build/runtime
- **Utilisateur non-root** : Sécurité renforcée
- **Cache optimisé** : `--no-cache` dans les installations

## Développement local

```bash
# Test local
python3 web_app.py

# Build Docker
docker build -f minimal-dockerfiles/Dockerfile.alpine -t neon-os .
docker run -p 8000:8000 neon-os
```

## Tailles des images

| Image | Taille finale | Usage |
|-------|---------------|-------|
| Alpine | ~45MB |  Production |
| Multi-stage | ~35MB |  Optimisé |
| Debian Slim | ~120MB |  Backup |
| BusyBox | ~15MB |  Expérimental |