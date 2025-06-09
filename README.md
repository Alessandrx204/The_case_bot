
## The_case_bot

A borderline useless Telegram bot written in Python using Aiogram 3. This bot transforms sent messages into lowercase, uppercase, or capitalised text. It’s mainly a personal exercise in bot development.

⸻

Features
	•	Convert messages to lowercase, uppercase, or capitalised.
	•	Simple commands to switch modes:
	•	/lowercase or /lower — transform messages to lowercase
	•	/uppercase or /upper — transform messages to uppercase
	•	/capitalise — transform messages to capitalised form
	•	Custom welcome message for a specified user ID.
	•	Stores user preferences and usernames in an SQLite database asynchronously.

⸻

Commands
	•	/start — Displays a welcome message (custom for a specific user).
	•	/help — Sends a sarcastic help message.
	•	/lowercase or /lower — Sets mode to lowercase.
	•	/uppercase or /upper — Sets mode to uppercase.
	•	/capitalise — Sets mode to capitalised text.
  •	/capitalize — joke response (i have nothing against american spelling it was just fun imo).
	•	Other /langXX commands respond with humorous language setting messages but have no actual effect.

⸻

Setup
	1.	Clone the repo or copy the code.
	2.	Replace DA_TOKEN with your Telegram bot token.
	3.	Replace custom_id with your Telegram user ID (optional) for a custom start message.
	4.	Modify Special_msg for a custom welcome message (optional).
	5.	Install dependencies:

pip install aiogram aiosqlite


	6.	Run the bot:

python the_case_bot.py



⸻

How it works
	•	When you send a command, it updates your mode in the SQLite database.
	•	Normal text messages are replied to according to the stored mode.
	•	The bot uses asynchronous SQLite access and Aiogram’s dispatcher to handle updates efficiently.

⸻

License & Rights

© Alssandrx 2025. All rights reserved unless specified otherwise upon request.

