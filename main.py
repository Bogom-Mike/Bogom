from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

from bot.config import TG_TOKEN
from bot.config import TG_APY_URL


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Мне нужен пример в формате: Число Знак Число"
    )


def answer(update, context):
    a = update.message.text
    z = ""
    c = ""
    b = ""
    for i in a:
        if i == " ":
            continue
        if i == "+" or i == "-" or i == "*" or i == "/":
            z = i
            b = c
            c = ""
            continue
        c += i
    a = 0
    if z == "+":
        a = float(b) + float(c)
    if z == "-":
        a = float(b) - float(c)
    if z == "*":
        a = float(b) * float(c)
    if z == "/":
        a = float(b) / float(c)
    text = str(a)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def main():
    updater = Updater(
        token=TG_TOKEN,
        base_url=TG_APY_URL,
        use_context=True
    )

    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(Filters.text, answer)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
