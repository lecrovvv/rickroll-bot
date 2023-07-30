from telebot import TeleBot
from telebot import types
import config

bot = TeleBot(config.telegram_token)

@bot.message_handler(commands=["start"])
def start_command_handler(msg):
    user_id = msg.from_user.id
    referrer = None

    if " " in msg.text:
        referrer_candidate = msg.text.split()[1]

        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(config.victims_preview.get("btn_text"), url=config.rickroll_link)
        markup.add(item)

        img = open(config.victims_preview.get("thumbnail"), 'rb')
        bot.send_photo(msg.chat.id, img, caption=config.victims_preview.get("text"), parse_mode = 'MarkdownV2', reply_markup=markup) 

    else:
        referrer_candidate = None
        bot.send_message(msg.chat.id, ">:( Доступ к боту возможен только по реферальной ссылке")


bot.infinity_polling()