#!/bin/bash
# Setup script pour Telegram Automatisé Bot

echo "🚀 Installation de Telegram Automatisé Bot"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer."
    exit 1
fi

echo "✅ Python installé: $(python3 --version)"

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip3 install -r requirements.txt

# Créer le dossier de logs
mkdir -p logs

# Créer le fichier .env
if [ ! -f .env ]; then
    echo "📝 Création de .env..."
    cat > .env << EOF
TELEGRAM_TOKEN=ton_token_telegram_ici
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:27b
EOF
    echo "⚠️  N'oublie pas de configurer ton token Telegram dans .env"
else
    echo "✅ .env déjà existant"
fi

# Créer config.yaml si inexistant
if [ ! -f config.yaml ]; then
    echo "📝 Création de config.yaml..."
    cp config.yaml.example config.yaml
fi

echo "✅ Installation terminée!"
echo ""
echo "📋 Étapes suivantes:"
echo "1. Configure ton token Telegram dans .env"
echo "2. Vérifie que Ollama est installé et que gemma3:27b est disponible"
echo "3. Lance le bot: python3 bot.py"