# Lichess Rating Bot

This bot interacts with the Lichess API to fetch and display chess ratings for users. 
It allows comparing ratings of two users or displaying the ratings of a single user.
The bot is built using the Telegram Bot API and Berserk (Lichess API wrapper).

## Features

- Fetch and display chess ratings (Bullet, Blitz, Rapid) for a single Lichess user.
- Compare ratings between two users.
- Handles group and individual chat messages.
- Provides an interactive and user-friendly interface.

## Requirements

- Python 3.8+
- Lichess and Telegram API tokens (store them in a `.env` file) for security of tokens.
- Libraries:
  - `python-telegram-bot`
  - `berserk`
  - `python-dotenv`


