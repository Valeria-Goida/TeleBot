import telebot
from PIL import Image, ImageDraw, ImageFont
import random
import os

TOKEN = '7280382035:AAHmk8EuBEPDcBUpSY9LshksdgEciHfGynI'
bot = telebot.TeleBot(TOKEN)

IMAGE_FOLDER = 'images'
RESULT = 'result'

QUOTES = [
    "Не останавливайся на полпути, самое интересное впереди.",
    "Твоя жизнь не улучшится случайно, она улучшится изменениями.",
    "Каждый день — это новая возможность.",
    "Не сдавайся, мечты сбываются!",
    "Успех приходит к тем, кто действует.",
    "Твое будущее создается тем, что ты делаешь сегодня.",
    "Стремись к совершенству, даже если оно недостижимо.",
    "Не важно, как медленно ты идешь, главное — не останавливаться.",
    "Твои возможности безграничны.",
    "Успех — это сумма небольших усилий, повторяемых день ото дня."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой мотивационный бот. Напиши /motivation, чтобы получить дозу мотивации.")

@bot.message_handler(commands=['motivation'])
def send_motivation(message):
    random_image = random.choice(os.listdir(IMAGE_FOLDER))
    image_path = os.path.join(IMAGE_FOLDER, random_image)

    quote = random.choice(QUOTES)

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)


    font = ImageFont.truetype("ofont.ru_Yeast 22.ttf", 100)


    text_position = (50, 50)

    draw.text(text_position, quote, font=font, fill="white")

    output_image_path = os.path.join(RESULT, 'output_image.jpg')
    img.save(output_image_path)

    with open(output_image_path, 'rb') as image_file:
        bot.send_photo(message.chat.id, image_file)

bot.polling()