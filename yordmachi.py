import json

import aiogram.dispatcher.filters
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from aiogram.types import KeyboardButton, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command
from geopy.geocoders import Nominatim
from googletrans import Translator
from aiogram.contrib.fsm_storage.memory import MemoryStorage
trans = Translator()

BOT_TOKEN = '6097445319:AAFJUQzA_Pv_3uNpVTEOkFr6Y6D2bv5yX4I'
bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
reply_markup2 = InlineKeyboardMarkup()
s3 = [
        [InlineKeyboardButton(text="⬅️ Asosiy menu", callback_data="Asosiymenu"),
         InlineKeyboardButton(text="🏠Eng yaqin filial",callback_data="yaqin_filiyal")],
        [InlineKeyboardButton(text="➡️ Keyingi", callback_data="keyingi")],
        [InlineKeyboardButton(text="ALGORITM", callback_data="algoritm"),
         InlineKeyboardButton(text="ANDIJON-1", callback_data="andijon-1")],
        [InlineKeyboardButton(text="BEKTEMIR", callback_data="bektemir"),
         InlineKeyboardButton(text="BERUNIY", callback_data="beruniy")],
        [InlineKeyboardButton(text="BODOMZOR", callback_data="bodomzor"),
         InlineKeyboardButton(text="CHILONZOR 19", callback_data="chilonzor19")],
        [InlineKeyboardButton(text="CHILONZOR metro", callback_data="chilonzor_metro"),
         InlineKeyboardButton(text="CHINOZ", callback_data="chinoz")],
        [InlineKeyboardButton(text="CHIRCHIK", callback_data="chirchik"),
         InlineKeyboardButton(text="CHOPON OTA", callback_data="chopon_ota")]
    ]
for i in s3:
    reply_markup2.add(*i)



til = [
    ["O'zbekcha 🇺🇿","Русский 🇷🇺"]
]
til_markup = ReplyKeyboardMarkup(keyboard=til,resize_keyboard=True)


reply_menu_uz = InlineKeyboardMarkup(row_width=2)
s = InlineKeyboardButton(text='🛒 Buyurtma berish', callback_data='buyurtma_berish')
reply_menu_uz.add(s)
s2 = InlineKeyboardButton(text='ℹ️ Biz haqimizda', callback_data='biz_haqimizda')
s3 = InlineKeyboardButton(text='🛍 Buyurtmalarim', callback_data='buyurtmalar')
reply_menu_uz.add(s2,s3)
s4 = InlineKeyboardButton(text='🏘 Filiyallar',callback_data='Filyallar')
reply_menu_uz.add(s4)
s5 = InlineKeyboardButton(text='🧐 Fikir bildirish', callback_data='Fikir')
s6 = InlineKeyboardButton(text='⚙️ Sozlamalar',callback_data='sozlamalar')
reply_menu_uz.add(s5,s6)




reply_menu_ru = InlineKeyboardMarkup(row_width=2)
s =InlineKeyboardButton(text='🛒 Начаты заказ', callback_data='buyurtma_berish')
reply_menu_ru.add(s)
s2 = InlineKeyboardButton(text='ℹ️ О нас', callback_data='biz_haqimizda'),
s3 = InlineKeyboardButton(text='🛍 Мои заказы', callback_data='buyurtmalar')
reply_menu_ru.add(s2,s3)
s4 = InlineKeyboardButton(text='🏘 Филиалы',callback_data='Filyallar')
reply_menu_ru.add(s4)
s5 = InlineKeyboardButton(text='🧐 Оставить отзыв', callback_data='Fikir')
s6 = InlineKeyboardButton(text='⚙️ Настройки',callback_data='sozlamalar')
reply_menu_ru.add(s5,s6)

def start_bosgan(msg: types.Message):
    with open('oqtepa_start.json', 'r') as f:
        data = json.load(f)
    for i in data:
        try:
            i[str(msg.from_user.id)]
            return "start"
        except:
            pass

async def set_command_uz():
    await bot.set_my_commands(
        [BotCommand('start', "Foydalanishni Boshlash"), BotCommand('buy', "Buyurtma Berish"),
         BotCommand('help', "Hizmat Haqida"), BotCommand('terms', "Foydlanish Shartlari"),
         BotCommand('support', "Biz bilan aloqa")])

async def set_command():
    await bot.set_my_commands(
        [BotCommand('start', "Начать использовать"), BotCommand('buy', "Разместить заказ"),
         BotCommand('help', "О программе"), BotCommand('terms', "Условия обслуживания"),
         BotCommand('support', "Свяжитесь с нами")])
