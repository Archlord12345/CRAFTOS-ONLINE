# 🖥️ Accès au Bureau KDE Plasma NEON OS

## 📍 Situation Actuelle
- **URL actuelle** : craftos-online.onrender.com
- **Interface** : Web terminal (Alpine)
- **Service** : neon-os (plan free)

## 🎯 Objectif : Bureau KDE Plasma Complet

### Étape 1 : Vérifier les services Render
1. Connectez-vous à [Render Dashboard](https://dashboard.render.com)
2. Vérifiez que le service `neon-os-kde-real` est déployé
3. Si nécessaire, cliquez "Manual Deploy" pour le déployer

### Étape 2 : Installer un client VNC

#### Windows
```bash
# Télécharger RealVNC Viewer
# https://www.realvnc.com/en/connect/download/viewer/
```

#### macOS
```bash
# Télécharger VNC Viewer
# https://www.realvnc.com/en/connect/download/viewer/
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt install remmina

# ou
sudo apt install vinagre

# Fedora
sudo dnf install remmina
```

### Étape 3 : Configuration VNC

#### Informations de connexion
- **Hôte** : neon-os-kde-real.onrender.com
- **Port** : 5901
- **Utilisateur** : neonuser
- **Mot de passe** : neon123

#### Exemple Remmina (Linux)
1. Ouvrir Remmina
2. Nouvelle connexion → VNC
3. Serveur : `neon-os-kde-real.onrender.com:5901`
4. Username : `neonuser`
5. Password : `neon123`

### Étape 4 : Ce que vous verrez

✅ **Bureau KDE Plasma complet**
- Thème NEON sombre avec couleurs neon
- Raccourcis bureau : Terminal NEON, File Manager, Web Browser
- Dossiers thématiques : OVERWORLD, NETHER, THE_END
- Menu KDE avec applications NEON
- Résolution 1920x1080

❌ **Si vous voyez encore l'interface web**
- Le service KDE n'est pas encore déployé
- Vérifiez le statut sur Render Dashboard
- Le plan starter est requis pour KDE

## 🔧 Dépannage

### Problème : Service non trouvé
- Vérifiez que `neon-os-kde-real` est dans votre render.yaml
- Redéployez manuellement depuis Render

### Problème : Connexion VNC refusée
- Attendez 2-3 minutes après le déploiement
- Vérifiez que le service est "Live" sur Render

### Problème : Écran noir
- Le bureau KDE démarre (attendez 30 secondes)
- Essayez de rafraîchir la connexion VNC

## 📞 Support

Si le service KDE ne se déploie pas :
1. Vérifiez votre plan Render (starter requis)
2. Contactez le support Render
3. Essayez de réduire la résolution dans le Dockerfile

---

**Note** : L'interface web actuelle reste accessible pour les commandes simples,
mais le bureau KDE offre l'expérience complète NEON OS !
