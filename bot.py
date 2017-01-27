# webhook bot skeleton

from telegram import Bot
from os import environ
from telegram.ext import Updater, CommandHandler
from credentials import TOKEN, APP_URL


def start(bot, update):
    chat_id = update.message.chat_id
    text = "Hello world!"
    bot.sendMessage(chat_id=chat_id, text=text)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Initialise bot
    global bot
    bot = Bot(token=TOKEN)

    # Setup webhook
    PORT = int(environ.get('PORT', '5000'))
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.setWebhook(APP_URL + TOKEN)

    # Add handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    main()