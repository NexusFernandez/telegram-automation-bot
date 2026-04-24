# 🤖 Telegram AI Business Bot

> Python Telegram bot automation toolkit — lead scraping, smart notifications, and AI-powered workflow automation.

A practical Telegram command bot for operators, freelancers, and founders who want a **private control panel inside Telegram**.

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Ollama](https://img.shields.io/badge/AI-Ollama-orange)

## ✨ Features

### /report — Business Reports
Generate daily/weekly business reports with key metrics, summaries, and action items. Powered by local AI (Ollama).

### /schedule — Smart Scheduling
Schedule reminders and recurring tasks. Never miss a deadline or follow-up again.

### /alert — Automated Alerts
Set up keyword-based alerts and notifications. Monitor RSS feeds, prices, or any webhook source.

### /memo — Quick Notes
Capture ideas, meeting notes, and to-dos in your private Telegram chat. Searchable and organized.

### /ai — AI Assistant
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

- Python 3.10+
- Telegram bot token (from [@BotFather](https://t.me/BotFather))
- [Ollama](https://ollama.ai) running locally (for /ai command)

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

## 🏢 Commercial License

This repository contains the open-source version under MIT license.

**For the full commercial version with premium features:**

👉 **[Get it on Gumroad](https://gumroad.com/l/telegram-bot) — 21 EUR**

Premium features include:
- Multi-chat management dashboard
- CRM integration hooks
- Advanced scheduling with timezone support
- Priority support

## 🛠️ Tech Stack

- **Python 3.10+** — core runtime
- **pyTelegramBotAPI** — Telegram Bot API wrapper
- **Ollama** — local AI inference (Gemma3, Llama3, etc.)
- **PyYAML** — configuration management

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

Built by [Nexus Fernandez](https://github.com/NexusFernandez) · [nexusmind30.gumroad.com](https://nexusmind30.gumroad.com)
