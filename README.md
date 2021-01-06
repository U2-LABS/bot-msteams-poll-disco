# Musical MS Teams Bot
Bot that creates music poll, where you can vote for your favorite song
## Setup bot
1. Clone repo
2. Create virtual environment
```
python -m venv env
source env/bin/activate
```
3. Install *requirements.txt*
```
pip install -r requirements.txt
```
4. Set virtual environment variables (Create .env file in the project root folder)
```
# .env file
MicrosoftAppId='YOUR_BOT_IP'
MicrosoftAppPassword='YOUR_BOT_PASSWORD'

NAME_DB='YOUR_DATABASE_NAME'
USER_DB='YOUR_DATABASE_USER'
PASSWORD_DB='YOUR_DATABASE_PASSWORD'
HOST_DB='YOUR_DB_HOST'
PORT_DB='YOUR_DB_PORT'
```
5. Start bot
```
python app.py
```