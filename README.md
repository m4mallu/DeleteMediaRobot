# Delete Media Robot 

 **A Simple Telegram Bot to delete all medias in a chat with single command !**

### Requirements:
```
TG_BOT_TOKEN    - Get from @BotFather
APP_ID          - Get from my.telegram.org
API_HASH        - Get from my.telegram.org
TG_USER_SESSION - Run any userbot session maker(https://repl.it/@ayrahikari/pyrogram-session-maker)
AUTH_USERS      - List of Autherized user ids separated by <space>
```

 **STRING SESSION USER MUST BE AN ADMIN IN THE TARGET CHAT WHERE BOT PERFORMS THE FUNCTION**

### @BotFather Command:
```
/cleanmedia - Delete medias in Group (Only done by AUTH USERS)
```

### Deploy Easy Way:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/DeleteMediaRobot)

### Deploy Hard Way:

Create **config.py** with variables as given below (Refer sample.config):

```
class Config(object):
    TG_BOT_TOKEN = "134448596:AAEIyo3EBVCN3qdd3TfrmQUxoI-eZVGvmI"
    APP_ID = int(123635)
    API_HASH = "1a417dd4fdf3ead2819ff35641daa16b"
    TG_USER_SESSION = "BQDGRUC0_qw2GVQ2gpLFaXOt0mrWg16cBZPATQvR8KThDzi-NRE1I9DB......"
    AUTH_USERS = [1134455567, 9244566948]
```
Run the following:

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
### LICENSE

- [GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

### Credits:

[DAN](https://t.me/haskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library

[SpEcHiDe](https://github.com/SpEcHiDe) for his [DeleteMessagesRoBot](https://github.com/SpEcHiDe/DeleteMessagesRoBot)

### Creator :

[Mallu Boy](https://t.me/m4mallu) In Telegram - [AS](https://t.me/space4renjith)