# Reddit Upvote Bot
A Python bot that automates upvoting of comments and posts on Reddit. The bot uses Selenium to navigate Reddit's interface and pandas to access user credentials from an Excel sheet.

## Features

- Automate upvoting of Reddit comments and posts.
- Securely store and manage user credentials using an Excel spreadsheet.
- Customizable configuration for bot behavior.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/reddit-upvote-bot.git
   cd reddit-upvote-bot


Install the required Python packages using pip:

pip install -r requirements.txt


## Usage

Create an Excel spreadsheet named reddit_passes.csv with columns username and password in the project directory. Populate it with the Reddit usernames and passwords you want to use.

Open bot.py and modify any relevant settings such as the post URL and XPath.

## Run the bot script:

python upvote_bot.py
