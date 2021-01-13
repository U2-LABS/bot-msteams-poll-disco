# Musical MS Teams Bot
Bot that creates music poll, where you can vote for your favorite song
## Bot commands
* Poll owner:
	* Invoke *disco* command to run music poll for all members of chat.
	* Invoke *lightsoff* to finish the poll and upload music file to the chat.
	* Invoke *poptop* **int** command to upload specific file, not a winner.
	* Invoke *settings* **option** **args** command to setup your bot settings.
		* List of options:
			* mp3 **on/off** to enable/disable uploading music.
* All members of the chat:
	* Invoke *top* **int** to show the list of **int** number of winners.
	* Invoke *poll_status* to show the status of the bot:
		* If it is running.
		* If it is enabled to upload music.
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
4. Update Azure settings
* To create bot, you need to visit Azure portal bot service and [create bot](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.BotService%2FbotServices)
* After creating the bot, you will be able to get *MicrosoftAppId* in the *settings* section
* By clicking *manage* at the top of the *MicrosoftAppId* you will be able to setup *MicrosoftAppPassword*
* You also need to update Messaging endpoint with URL of the server, where your bot is running (**URL should end with /api/messages**)
5. Set virtual environment variables (Create .env file in the project root folder)
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
6. Start bot
```
python app.py
```
