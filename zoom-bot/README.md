# Zoom Bot

### Шевцова Елизавета Сергеевна Б06-008
## Organize & create Zoom meetings in Telegram


![title](Zoom-icon-logo1.png)

## Manual:

`/start`

After pressing start, you'll be navigated to Zoom authorization page. After signing in, you'll  be redirected back to the chat bot chat. Bot will store your aceess token to make requests to Zoom API in your name.

Press `/start` command again to get a menu. You'll be able to:
- add existing zoom meeting
- get a list of added zoom meetings
- create a new zoom meeting (bot will send you a ready-to-join link)

## TODO
1. Publish Zoom Oauth app to Zoom marketplace to enable Create Meeting feature to outside users
2. Add user zoom_id to DB after loggin in to Zoom
3. Add auto-restart feature in case bot fails with error
4. Refactor ORM module to use Flask-SQLAlchemy instead of SQLAlchemy(better syntax)
5. Add more logging and error handling