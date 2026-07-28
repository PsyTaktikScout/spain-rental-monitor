# Spain Rental Monitor

A Python-based notification service that monitors Spanish rental property portals (Idealista, Fotocasa, Pisocompartido, Badi) and sends new listings to a Telegram chat.

## Features

- Polls 4 property portals every ~3 minutes
- Filters by price (≤850 EUR), rooms, balcony/terrace, publication date
- Deduplicates listings across cycles via CSV snapshots
- Sends Telegram notifications with property details and Google Maps links
- Self-healing — recreates state files on corruption, logs errors to Telegram

## Tech Stack

Python 3.10+ · requests · BeautifulSoup · pyTelegramBotAPI

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env
cp cookies.json.example cookies.json
# fill in your Telegram bot token, chat ID, and cookies
python ParserAllHousesInOne.py
```

## Project Structure

```
├── ParserAllHousesInOne.py   # Main scraper (4 sources)
├── .env.example               # Environment variable template
├── requirements.txt
└── README.md
```

## License

MIT
