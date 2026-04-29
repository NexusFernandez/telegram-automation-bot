<h1 align="center">🤖 Telegram AI Business Bot</h1>

<p align="center">
  <strong>Python Telegram bot with AI-powered reports, scheduling, alerts, and chat.</strong><br>
  Runs 100% locally with Ollama. No API keys. No subscriptions.
</p>

<p align="center">
  <a href="https://nexusmind30.gumroad.com/l/wkyts">
    <img src="https://img.shields.io/badge/Get%20Pro%20Version-Gumroad-36b37e?style=for-the-badge&logo=gumroad" alt="Get on Gumroad">
  </a>
  <a href="https://github.com/NexusFernandez/telegram-automation-bot/stargazers">
    <img src="https://img.shields.io/github/stars/NexusFernandez/telegram-automation-bot?style=social" alt="Stars">
  </a>
</p>

---

## ✨ Features

### /report — Business Reports 📊
Generate daily/weekly business reports with key metrics, summaries, and action items. Powered by local AI (Ollama).

### /schedule — Smart Scheduling ⏰
Schedule reminders and recurring tasks. Never miss a deadline or follow-up again.

### /alert — Automated Alerts 🔔
Set up keyword-based alerts and notifications. Monitor RSS feeds, prices, or any webhook source.

### /memo — Quick Notes 📝
Capture ideas, meeting notes, and to-dos in your private Telegram chat. Searchable and organized.

### /ai — AI Assistant 🧠
Chat with a local AI model (Ollama) directly in Telegram. No data leaves your machine.

## 🚀 Quick Start

```bash
# 1. Clone and install
git clone https://github.com/NexusFernandez/telegram-automation-bot.git
cd telegram-automation-bot
pip install -r requirements.txt

# 2. Run setup
chmod +x setup.sh
./setup.sh

# 3. Configure your bot token
# Edit config.yaml — add your Telegram bot token from @BotFather

# 4. Run
python bot.py
```

### Prerequisites

- **Python 3.10+**
- **Telegram bot token** (from [@BotFather](https://t.me/BotFather))
- **[Ollama](https://ollama.ai)** running locally (for /ai command)

## ⚙️ Configuration

Edit `config.yaml` to customize:

```yaml
telegram:
  token: "your_telegram_bot_token"

ollama:
  base_url: "http://localhost:11434"
  model: "gemma3:27b"
  timeout: 30

commands:
  schedule:
    time_format: "HH:mm"
    enabled: true
  alerts:
    enabled: true
    notification_delay: 300
  report:
    enabled: true
    include_stats: true
```

## 🔒 Privacy First

| Feature | This Bot | Typical SaaS Bot |
|:--------|:---------|:-----------------|
| **Your data** | Stays on your machine | Sent to cloud |
| **AI processing** | Local (Ollama) | Remote API |
| **API keys needed** | None | OpenAI, etc. |
| **Monthly cost** | €0 after purchase | $10-50/month |
| **Source code** | Full Python source | Black box |

## ⬆️ Pro Version — €21

The free version is MIT-licensed and fully functional. **[Get the Pro version on Gumroad →](https://nexusmind30.gumroad.com/l/wkyts)** for:

- Multi-chat management dashboard
- CRM integration hooks
- Advanced scheduling with timezone support
- Priority support

## 🛠️ Tech Stack

- **Python 3.10+** — core runtime
- **pyTelegramBotAPI** — Telegram Bot API wrapper
- **Ollama** — local AI inference (Gemma3, Llama3, etc.)
- **PyYAML** — configuration management

---

## 📦 More Tools from Nexus

- **[RSS Opportunity Radar](https://github.com/NexusFernandez/rss-opportunity-radar)** — AI-summarized opportunity digest from RSS feeds (€19)
- **[All 12 AI Tools →](https://nexusmind30.gumroad.com)** — Python tools for freelancers, founders, and data analysts

---

**⭐ Star this repo** if you find it useful!

Built by [Nexus Fernandez](https://github.com/NexusFernandez) · [nexusmind30.gumroad.com](https://nexusmind30.gumroad.com)