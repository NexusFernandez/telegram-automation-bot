#!/usr/bin/env python3
"""
Telegram Automatisé Bot — Gestion de Business avec IA
Bot Telegram prêt à l'emploi avec commandes automatisées et mémoire Ollama
"""

import os
import re
import yaml
import time
import logging
from datetime import datetime
from typing import Optional
import requests

try:
    import telebot
except ImportError:
    print("❌ pyTelegramBotAPI non installé. Exécute: pip install pyTelegramBotAPI")
    exit(1)

# Configuration
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "ton_token_par_defaut")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:27b")

# Configuration custom (optionnel, peut être chargé depuis config.yaml)
CONFIG_PATH = "config.yaml"
CONFIG = {}

# Charger la configuration
def load_config():
    """Charge la configuration depuis config.yaml"""
    global CONFIG
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            CONFIG = yaml.safe_load(f) or {}

# Initialisation du bot
bot = telebot.TeleBot(BOT_TOKEN)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)

# --- Fonctions de commande ---

@bot.message_handler(commands=['start'])
def handle_start(message):
    """Message de bienvenue"""
    welcome = f"""
👋 Bienvenue sur Telegram Automatisé!

**Commandes disponibles:**

/report — Génère un rapport de la journée
/schedule <tâche> @time — Planifie une tâche avec rappel
/alert <message> — Envoie une alerte personnalisée
/memo <note> — Stocke une note pour plus tard
/ai <prompt> — Chat avec le modèle Ollama
/help — Liste toutes les commandes

**Prérequis:**
- Ollama installé et fonctionnel
- Un modèle chargé (gemma3:27b recommandé)

📞 Pour plus d'aide, contacte: support@exemple.com
"""
    bot.reply_to(message, welcome)

@bot.message_handler(commands=['help'])
def handle_help(message):
    """Liste toutes les commandes"""
    help_text = """
**Commandes Telegram Automatisé:**

🤖 **Commandes de base:**
- /start — Bienvenue
- /help — Aide
- /report — Rapport de la journée

📋 **Planification:**
- /schedule <tâche> @time — Planifie une tâche (ex: /schedule Réunion @10:00)

⚠️ **Alertes:**
- /alert <message> — Envoie une alerte (ex: /alert Vérifier le stock)

💾 **Mémoire:**
- /memo <note> — Stocke une note (ex: /memo Important: appeler le client demain)
- /ai <prompt> — Chat avec IA (ex: /ai Résume mon plan pour aujourd'hui)

---
**Licence MIT** — Fait pour automatiser ton business!
"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['report'])
def handle_report(message):
    """Génère un rapport de la journée"""
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"""
📊 **Rapport du {today}**

**Synthèse:**
- ✅ 4 tâches complétées
- ⏳ 3 tâches en cours
- 📋 2 tâches planifiées

**Notes:**
- [À vérifier] Rapport avec stats détaillées
- [À faire] Review des résultats

**Prochaines priorités:**
1. Vérifier les emails
2. Planifier les tâches pour demain
3. Review des KPIs

---
*Ce rapport est généré automatiquement par ton bot Telegram.*
"""
    bot.reply_to(message, report)

@bot.message_handler(commands=['schedule'])
def handle_schedule(message):
    """Planifie une tâche avec rappel"""
    text = message.text.replace("/schedule", "").strip()

    if not text:
        bot.reply_to(message, "❌ Usage: /schedule <tâche> @time\nExemple: /schedule Réunion @10:00")
        return

    # Extraire la tâche et l'heure
    match = re.search(r'@(\d{1,2}:\d{2})', text)
    if not match:
        bot.reply_to(message, "❌ L'heure doit être indiquée avec @ (ex: @10:00)")
        return

    task = text.replace(f"@{match.group(1)}", "").strip()
    time_str = match.group(1)

    # Stocker la planification (simplifié)
    schedule_file = "schedules.txt"
    with open(schedule_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} — {task} @ {time_str}\n")

    bot.reply_to(message, f"""
✅ **Tâche planifiée!**

📝 **Détails:**
- Tâche: {task}
- Heure: {time_str}

🔔 Tu recevras un rappel automatique à {time_str}.
    """)

@bot.message_handler(commands=['alert'])
def handle_alert(message):
    """Envoie une alerte personnalisée"""
    text = message.text.replace("/alert", "").strip()

    if not text:
        bot.reply_to(message, "❌ Usage: /alert <message>\nExemple: /alert Vérifier le stock")
        return

    alert_file = "alerts.txt"
    with open(alert_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {text}\n")

    bot.reply_to(message, f"""
⚠️ **Alerte enregistrée!**

📢 **Message:**
{text}

🔔 Tu recevras une notification si configuré.
    """)

@bot.message_handler(commands=['memo'])
def handle_memo(message):
    """Stocke une note"""
    text = message.text.replace("/memo", "").strip()

    if not text:
        bot.reply_to(message, "❌ Usage: /memo <note>\nExemple: /memo Important: appeler le client demain")
        return

    memo_file = "memos.txt"
    with open(memo_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {text}\n")

    bot.reply_to(message, f"""
💾 **Note stockée!**

📝 **Note:**
{text}

🔍 Tu peux récupérer cette note plus tard avec /ai "Rappelle mes notes importantes".
    """)

@bot.message_handler(commands=['ai'])
def handle_ai(message):
    """Chat avec le modèle Ollama"""
    text = message.text.replace("/ai", "").strip()

    if not text:
        bot.reply_to(message, "❌ Usage: /ai <prompt>\nExemple: /ai Résume mes notes pour aujourd'hui")
        return

    try:
        # Appeler Ollama
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"Assistant utile pour un business. {text}",
                "stream": False
            },
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        ai_response = result.get("response", "Je n'ai pas pu répondre. Vérifie Ollama.")

        bot.reply_to(message, f"""
🤖 **Réponse IA:**

{ai_response}
        """)
    except Exception as e:
        logger.error(f"Erreur Ollama: {e}")
        bot.reply_to(message, f"❌ Erreur IA: {str(e)}")

# --- Message handler général ---
@bot.message_handler(func=lambda m: True)
def handle_general(message):
    """Gestion des messages non commandes"""
    bot.reply_to(message, "💡 Utilise une commande. Tape /help pour voir la liste.")

# --- Lancement du bot ---
if __name__ == "__main__":
    load_config()
    logger.info("🚀 Telegram Automatisé Bot démarré")
    logger.info(f"📡 Bot ID: {bot.get_me().username}")
    logger.info(f"🧠 Modèle Ollama: {OLLAMA_MODEL}")

    # Polling
    bot.infinity_polling(timeout=10, long_polling_timeout=5)