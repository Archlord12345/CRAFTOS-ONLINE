#!/bin/bash

echo "🚀 Configuration de Render pour NEON OS TOON EDITION"
echo "=================================================="

# Vérifier que render.yaml existe
if [ ! -f "render.yaml" ]; then
    echo "❌ Erreur: render.yaml non trouvé"
    exit 1
fi

# Vérifier les Dockerfiles
echo "📋 Vérification des Dockerfiles..."
dockerfiles=(
    "minimal-dockerfiles/Dockerfile.alpine"
    "minimal-dockerfiles/Dockerfile.slim"
    "minimal-dockerfiles/Dockerfile.multi-stage"
)

for dockerfile in "${dockerfiles[@]}"; do
    if [ -f "$dockerfile" ]; then
        echo "✅ $dockerfile trouvé"
    else
        echo "❌ $dockerfile manquant"
    fi
done

# Vérifier web_app.py
if [ -f "web_app.py" ]; then
    echo "✅ web_app.py trouvé"
else
    echo "❌ web_app.py manquant"
fi

echo ""
echo "🎯 Services configurés dans render.yaml:"
echo "• neon-os (principal) - Alpine Linux - ~45MB"
echo "• neon-os-backup - Debian Slim - ~120MB"  
echo "• neon-os-terminal - Multi-stage - ~35MB"
echo ""
echo "📦 Pour déployer sur Render:"
echo "1. Poussez votre code sur GitHub"
echo "2. Connectez votre repo à Render"
echo "3. Render détectera automatiquement render.yaml"
echo "4. Les services seront déployés automatiquement"
echo ""
echo "🔗 URLs attendues:"
echo "• Principal: https://neon-os.onrender.com"
echo "• Backup: https://neon-os-backup.onrender.com"
echo "• Terminal: https://neon-os-terminal.onrender.com"
