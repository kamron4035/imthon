import errno

from aiogram import types, executor
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from geopy.geocoders import Nominatim
from yordmachi import dp, reply_markup2,bot, til_markup ,trans, set_command, reply_menu_ru, reply_menu_uz, set_command_uz, start_bosgan
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import json

shaxar = []

class Form(StatesGroup):
    country = State()
    comment = State()
    start_2 = State()
    nomer1 = State()
    nomer2 = State()

async def main_handler(msg: types.Message, state: FSMContext):
    s=start_bosgan(msg)
    if s == "start":
        await giv_code(msg, state)
    else:
        data = [
            {
                str(msg.from_user.id):'start'
            }
        ]
        with open("oqtepa_start.json", "r") as f:
            try:
                a = json.load(f)
            except:
                a = []
        a.extend(data)
        with open("oqtepa_start.json", 'w') as file:
            json.dump(a, file, indent=3)
        await set_command_uz()
        s = f"Assalomu alaykum <b>{msg.from_user.username}</b>.Men <b>Oqtepa Lavash</b> yetkazib berish xizmati botiman!"
        await bot.send_message(msg.chat.id, s, parse_mode='html')
        s2 = f"<b>Tilni Tanlang\nВыберите язык</b>"
        await msg.answer(s2, reply_markup=til_markup, parse_mode='html')
        await Form.country.set()


async def viloyat(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['til'] = msg.text
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        design = [["TOSHKENT", "NUKUS"],["NAMANGAN", "QO'QON"],["ANDIJON", "FARG'ONA"]]
        markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
        await msg.answer('Shaharni Tanlang', reply_markup=markup)
    else:
        await set_command()
        design = [["ТАШКЕНТ", "НУКУС"], ["НАМАНГАН", "КОКОН"], ["АНДИЖАН", "ФЕРГОНА"]]
        markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
        s = trans.translate('Shaharni Tanlang', dest="ru", src="uz").text
        await msg.answer(s, reply_markup=markup)



from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator

async def Request_phone(msg: types.Message, state: FSMContext):
    await state.set_state('nomer1')
    async with state.proxy() as data:
        til = data['til']
        data['viloyat'] = msg.text
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        shaxar = []  # Assuming 'shaxar' is a list
        shaxar.append(msg.text)
        s2 = [
            [KeyboardButton("📞Mening nomerim", request_contact=True)]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await msg.answer("Ro'yxatga olish uchun telefon raqamingizni kiriting!\nMasalan +998xx xxx xx xx", reply_markup=markup)
    else:
        await set_command()
        s2 = [
            [KeyboardButton("📞Мой номер", request_contact=True)]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        trans = Translator()
        s = trans.translate("Ro'yxatga olish uchun telefon raqamingizni kiriting!\nMasalan +998xx xxx xx xx", dest="ru", src="uz").text
        await msg.answer(s, reply_markup=markup)



async def giv_code(msg: types.Message,  state: FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        s2 = [
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await msg.answer("Buyurtmani birga joylashtiramizmi? 🤗",reply_markup=markup)
        await msg.answer("Buyurtma berishni boshlash uchun 🛒\t\n Buyurtma qilish tugmasini bosing\n\n Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin \n[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-03-31)", reply_markup=reply_menu_uz,parse_mode='Markdown')
    else:
        await set_command()
        s2 = [
            [KeyboardButton("⬅️ Основное меню")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await msg.answer("Сделаем заказ вместе? 🤗",reply_markup=markup)
        await msg.answer("Для заказа нажмите 🛒\nНачать заказ\n\n А также вы можете посмотреть акции и ознакомиться с местонахождением наших филиалов \n[Oqtepa Lavash menu](https://telegra.ph/Menyu-03-31-7)", reply_markup=reply_menu_ru, parse_mode='Markdown')


async def giv_code3(msg: types.Message,  state: FSMContext):
    phone_num = msg.contact.phone_number
    async with state.proxy() as data:
        til = data['til']
        data['raqam'] = phone_num
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        s2 = [
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await msg.answer("Buyurtmani birga joylashtiramizmi? 🤗",reply_markup=markup)
        await msg.answer("Buyurtma berishni boshlash uchun 🛒\t\n Buyurtma qilish tugmasini bosing\n\n Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin \n[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-03-31)", reply_markup=reply_menu_uz,parse_mode='Markdown')
    else:
        await set_command()
        s2 = [
            [KeyboardButton("⬅️ Основное меню")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await msg.answer("Сделаем заказ вместе? 🤗",reply_markup=markup)
        await msg.answer("Для заказа нажмите 🛒\nНачать заказ\n\n А также вы можете посмотреть акции и ознакомиться с местонахождением наших филиалов \n[Oqtepa Lavash menu](https://telegra.ph/Menyu-03-31-7)", reply_markup=reply_menu_ru, parse_mode='Markdown')



async def giv_code2(call: callback_query.CallbackQuery,state : FSMContext):
    await Form.next()
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        await call.message.edit_text("Buyurtma berishni boshlash uchun 🛒\t\n Buyurtma qilish tugmasini bosing\n\n Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin \n[Oqtepa Lavash menu](https://telegra.ph/Taomnoma-03-31)", reply_markup=reply_menu_uz,parse_mode='Markdown')
    else:
        await set_command()
        await call.message.edit_text("Для заказа нажмите 🛒\nНачать заказ\n\n А также вы можете посмотреть акции и ознакомиться с местонахождением наших филиалов \n[Oqtepa Lavash menu](https://telegra.ph/Menyu-03-31-7)", reply_markup=reply_menu_ru, parse_mode='Markdown')


async def buyurtma_berish(call: callback_query.CallbackQuery,state : FSMContext):
    await Form.next()
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        s2 = [
        [KeyboardButton("🛵 Eltib berish"),KeyboardButton("🚶 Borib olish")],
        [KeyboardButton("⬅️ Asosiy menu")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await call.message.answer("Buyurtma turini tanlang", reply_markup=markup)
        await call.answer()

    else:
        await set_command()
        s2 = [
            [KeyboardButton("🛵 Доставка"), KeyboardButton("🚶 иди возьми")],
            [KeyboardButton("⬅️ Основное меню")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await call.message.answer("Выберите тип заказа", reply_markup=markup)


async def foydalanuvchi_buyurtmalari(call : callback_query.CallbackQuery, state : FSMContext):
    await Form.next()
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await set_command_uz()
        s2 = [
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await call.message.answer("Siz hali hanuz birorta ham buyurtma bermagansiz.",reply_markup=markup)
        await call.answer()
    else:
        await set_command()
        s2 = [
            [KeyboardButton("⬅️ Основное меню")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await call.message.answer("Вы еще не разместили ни одного заказа.", reply_markup=markup)
        await call.answer()


async def biz_haqimizda(call: callback_query.CallbackQuery,state : FSMContext):
    await Form.next()
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.message.delete()
        await set_command_uz()
        await call.message.answer("Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.\n\nQaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!\n\n Yetkazib berish xizmati:  +998781500030\n[Sayt](https://oqtepalavash.uz/) | [Facebook](http://fb.me/oqtepalavash.official) | [Instagram](https://www.instagram.com/oqtepalavash.official)", parse_mode='Markdown')
        await call.answer()
    else:
        await set_command()
        await call.message.delete()
        await call.message.answer("Мы работаем на рынке Узбекистана уже 12 лет и на сегодняшний день имеем более 50 филиалов по всей стране. Клиенты, довольные нашей вкусной и питательной едой, доступными ценами и быстрой службой доставки, выбирают нас снова и снова, не забудьте добавить!\n\n Служба доставки: +998781500030\n[Сайт](https://oqtepalavash.uz/) | [Facebook](http://fb.me/oqtepalavash.official) | [Instagram](https://www.instagram.com/oqtepalavash.official)",parse_mode='Markdown')
        await call.answer()


async def fikir(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        data['text'] = "fikir"
    await Form.next()
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.message.delete()
        await set_command_uz()
        await call.message.answer("Fikr va mulohazalaringizni yuboring")
    else:
        await set_command_uz()
        await call.message.delete()
        await call.message.answer("Присылайте свои мысли и комментарии")
    await Form.comment.set()


async def Comment(msg: types.Message,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    async with state.proxy() as data:
        comment=data['text']
    print(comment)
    if til == "O'zbekcha 🇺🇿":
        if comment == "fikir":
            await set_command_uz()
            s2 = [
                [KeyboardButton("⬅️ Asosiy menu")]
            ]
            markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
            await msg.answer("Fikringiz Uchun Raxmat",reply_markup=markup)
    else:
        if comment == "":
            await set_command()
            s2 = [
                [KeyboardButton("⬅️ Основное меню")]
            ]
            markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
            await msg.answer("Спасибо за ваше мнение",reply_markup=markup)
        else:
            await set_command()
            s2 = [
                [KeyboardButton("⬅️ Основное меню")]
            ]
            markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
            await msg.answer("Спасибо за ваши мысли", reply_markup=markup)


async def sozlamalar(call: callback_query.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        til = data['til']
        contry = data['viloyat']
        raqam = data['raqam']
    if til == "O'zbekcha 🇺🇿":
        s2 = [[InlineKeyboardButton(text='Muloqot tili', callback_data="muloqot_tili"),
               InlineKeyboardButton(text='Telefon', callback_data='telefon'),
               InlineKeyboardButton(text='Shaxar', callback_data='shaxar')],
              [InlineKeyboardButton(text="⬅️ Asosiy menu", callback_data='Asosiymenu')]]
        markup = InlineKeyboardMarkup(inline_keyboard=s2)
        ans = f"<b>Til</b>: {til}\n<b>raqam</b>: <code>{raqam}</code>\n<b>shaxar</b>: {contry}\n\nQuyidagilardan birini tanlang"
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans, reply_markup=markup, parse_mode='html')
    else:
        s2 = [[InlineKeyboardButton(text='Язык', callback_data="muloqot_tili"),
               InlineKeyboardButton(text='Телефон', callback_data='telefon'),
               InlineKeyboardButton(text='Город', callback_data='shaxar')],
              [InlineKeyboardButton(text="⬅️ Основное меню", callback_data='Asosiymenu')]]
        markup = InlineKeyboardMarkup(inline_keyboard=s2)
        ans = f"<b>Язык</b>: {til}\n<b>Телефон</b>: <code>{raqam}</code>\n<b>Город</b>: {contry}\n\nВыберите одно из следующих"
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans,
                                         reply_markup=markup, parse_mode='html')

#sozlamalar
async def til_tanlash(call: callback_query.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        contry = data['viloyat']
        raqam = data['raqam']
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        ans = f"<b>Til</b>: {til}\n<b>raqam</b>: <code>{raqam}</code>\n<b>shaxar</b>: {contry}\n\nQuyidagilardan birini tanlang"
        s = [InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data="O'zbekcha 🇺🇿"),
             InlineKeyboardButton(text="Русский 🇷🇺", callback_data="Русский 🇷🇺")]
        markup = InlineKeyboardMarkup(inline_keyboard=[s])
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans, reply_markup=markup, parse_mode='html')
    else:
        ans = f"<b>Язык</b>: {til}\n<b>Телефон</b>: <code>{raqam}</code>\n<b>Город</b>: {contry}\n\nВыберите одно из следующих"
        s = [InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data="O'zbekcha 🇺🇿"),
             InlineKeyboardButton(text="Русский 🇷🇺", callback_data="Русский 🇷🇺")]
        markup = InlineKeyboardMarkup(inline_keyboard=[s])
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans,
                                         reply_markup=markup, parse_mode='html')


async def til_2(call: callback_query.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['til'] = str(call.data)
        contry = data['viloyat']
        raqam = data['raqam']
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        s2 = [[InlineKeyboardButton(text='Muloqot tili', callback_data="muloqot_tili"),
               InlineKeyboardButton(text='Telefon', callback_data='telefon'),
               InlineKeyboardButton(text='Shaxar', callback_data='shaxar')],
              [InlineKeyboardButton(text="⬅️ Asosiy menu", callback_data='Asosiymenu')]]
        markup = InlineKeyboardMarkup(inline_keyboard=s2)
        ans = f"<b>Til</b>: {til}\n<b>raqam</b>: <code>{raqam}</code>\n<b>shaxar</b>: {contry}\n\nQuyidagilardan birini tanlang"
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans, reply_markup=markup, parse_mode='html')
    else:
        s2 = [[InlineKeyboardButton(text='Язык', callback_data="muloqot_tili"),
               InlineKeyboardButton(text='Телефон', callback_data='telefon'),
               InlineKeyboardButton(text='Город', callback_data='shaxar')],
              [InlineKeyboardButton(text="⬅️ Основное меню", callback_data='Asosiymenu')]]
        markup = InlineKeyboardMarkup(inline_keyboard=s2)
        ans = f"<b>Язык</b>: {til}\n<b>Телефон</b>: <code>{raqam}</code>\n<b>Город</b>: {contry}\n\nВыберите одно из следующих"
        await call.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=ans,
                                         reply_markup=markup, parse_mode='html')


async def telefon(call: callback_query.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        contry = data['viloyat']
        raqam = data['raqam']
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        s2 = [
            [KeyboardButton("📞Mening nomerim", request_contact=True)],
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        ans = f"<b>Til</b>: {til}\n<b>raqam</b>: <code>{raqam}</code>\n<b>shaxar</b>: {contry}\n\nTelefon raqamingizni yuboring"
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer(text=ans, reply_markup=markup, parse_mode='html')
    else:
        s2 = [
            [KeyboardButton("📞Мой номер", request_contact=True)],
            [KeyboardButton("⬅️ Основное меню")]
        ]
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        markup = ReplyKeyboardMarkup(клавиатура=s2, resize_keyboard=True)
        ans = f"<b>Язык</b>: {til}\n<b>Телефон</b>: <code>{raqam}</code>\n<b>Город</b>: {contry}\n\nВыберите одно из следующих"
        await call.message.answer(text=ans, reply_markup=markup, parse_mode='html')
    await Form.nomer2.set()


async def nomer_(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['raqam'] = msg.contact.phone_number
    await state.set_state('nomer_2')


async def filiyallar(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Bizning filiallarimiz : 61 (1-10)", reply_markup=reply_markup2)


async def algortm(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 ALGORITM\n\n 📍[ Ташкент, Чиланзwарский район, махалля Бахористон махалля Бахористон](http://maps.yandex.ru/?text=41.262952,69.161994) \n\n🕑 10:00-02:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def andijon(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 ANDIJON-1\n\n 📍[ Андижан, улица Машраба, 62](http://maps.yandex.ru/?text=40.751609,72.363240) \n\n🕑 10:00-02:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def bektemir(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 BEKTEMIR\n\n 📍[ Ташкент, Бектемирский район, массив Сувсоз-2](http://maps.yandex.ru/?text=41.255273,69.375093) \n\n🕑 10:00-02:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def beruniy(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 BERUNIY\n\n 📍[ Ташкент, улица Беруни, 47](http://maps.yandex.ru/?text=41.344468,69.205111) \n\n🕑 10:00-22:00 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def bodomzor(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 BODOMZOR\n\n 📍[ Ташкент, проспект Амира Темура, 98](http://maps.yandex.ru/?text=41.337487,69.285620)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def chilonzor19(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 CHILONZOR 19\n\n 📍[ Ташкент, улица Аль-Хорезми, 66/1](http://maps.yandex.ru/?text=41.269353,69.191065)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def chilonzor_metro(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 CHILONZOR metro \n\n 📍[ Ташкент, Чиланзарский район, массив Чиланзор, 16-й квартал, 18](http://maps.yandex.ru/?text=41.272545,69.202428)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def chinoz(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 CHINOZ  \n\n 📍[ Ташкентская область, Чиназ](http://maps.yandex.ru/?text=40.940227,68.758729)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def chirchik(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 CHIRCHIK  \n\n 📍[ Ташкентская область, Чирчик](http://maps.yandex.ru/?text=41.478039,69.590430)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def chopon_ota(call: callback_query.CallbackQuery,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        await call.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="🏠 CHOPON OTA  \n\n 📍[ Ташкент, Чиланзарский район, махалля Лутфий махалля Лутфий](http://maps.yandex.ru/?text=41.293441,69.194863)  \n\n🕑 10:00-2:40 \n\nBizning filiallarimiz : 59 (1-10))", parse_mode='Markdown',reply_markup=reply_markup2)


async def eltib_berish(msg: types.Message,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        s2 = [
            [KeyboardButton("📍 Geo-joylashuvni yuborish",request_location=True)],
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        ms = "<b>Eltib berish</b> uchun <b>geo-joylashuvni</b> jo'nating yoki manzilni tanlang"
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        await bot.send_message(msg.chat.id, text=ms, parse_mode='html', reply_markup=markup)


async def lokatsion(msg: types.Message,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        s2 = [
            [KeyboardButton("❎ Yo'q"),KeyboardButton("✅ Ha")]
        ]
        s3 = [
            [KeyboardButton("📍 Geo-joylashuvni yuborish", request_location=True)],
            [KeyboardButton("⬅️ Asosiy menu")]
        ]
        geolocator = Nominatim(user_agent="my_bot")
        latitude = msg.location.latitude
        longitude = msg.location.longitude
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        country = location.raw['address'].get('country', None)
        district = location.raw['address'].get('city', None)
        neighborhood = location.raw['address'].get('neighbourhood', None)
        house = location.raw['address'].get('house')
        address = location.address
        markup = ReplyKeyboardMarkup(keyboard=s2, resize_keyboard=True)
        markup2 = ReplyKeyboardMarkup(keyboard=s3, resize_keyboard=True)
        print(shaxar,district)
        if shaxar == country:
            s = f"Buyurtma qilmoqchi bo'lgan manzilingiz: <b>{address}</b> Ushbu manzilni tasdiqlaysizmi?"
            await msg.answer(text=s,parse_mode='html',reply_markup=markup)
        else:
            s9 = f"Siz ushbu hududdan buyurtma bera olmaysiz.Siz faqat {shaxar} hududidan buyurtma berishingiz mumkin. Agar yuqoridagi hududdan buyurtma bermoqchi bo'lsangiz iltimos <b>Asosiy menu</b> ga o'tib hududingizni o'zgartiring!!!"
            await msg.answer(text=s9, parse_mode='html', reply_markup=markup2)


async def reply_show_handlers(msg: types.Message,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        design = [
            ["buttom1", KeyboardButton("Phone",request_contact=True)],
            ["button3"]
        ]
        markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard = True)
        await msg.answer('Show reply button', reply_markup=markup)


async def reply_show_handler(msg: types.Message,state : FSMContext):
    async with state.proxy() as data:
        til = data['til']
    if til == "O'zbekcha 🇺🇿":
        ikm = InlineKeyboardMarkup()
        ikm.add(InlineKeyboardButton('1', callback_data='1'))
        ikm.add(InlineKeyboardButton('2', callback_data='2'))
        ikm.add(InlineKeyboardButton('3', callback_data='3'))
        ikm.add(InlineKeyboardButton('4', callback_data='4'))
        await msg.answer('Show inline button', reply_markup=ikm)


#=============================MESSAGE HENDLARS==============================================

#__COMMANDS__________________________________________________________________________
dp.register_message_handler(main_handler, commands=["start"],state='*')
dp.register_message_handler(reply_show_handler, commands='help',state='*')
dp.register_message_handler(reply_show_handler, commands='buy',state='*')
# ___________________________________________________________________________________

# __KEYBORDS_________________________________________________________________________
dp.register_message_handler(viloyat, Text(equals=["O'zbekcha 🇺🇿","Русский 🇷🇺"]),state=Form.country)
dp.register_message_handler(Request_phone, Text(equals=["TOSHKENT", "NUKUS","NAMANGAN", "QO'QON", "ANDIJON", "FARG'ONA-2", "ТАШКЕНТ", "НУКУС", "НАМАНГАН", "КОКОН", "АНДИЖАН", "ФЕРГОНА"]),state='*')
dp.register_message_handler(giv_code, Text(equals='⬅️ Asosiy menu'),state='*')
dp.register_message_handler(giv_code, Text(equals="⬅️ Основное меню"),state='*')
dp.register_message_handler(eltib_berish, Text(equals="🛵 Eltib berish"),state='*')
#____________________________________________________________________________________
#__STATE_____________________________________________________________________________
dp.register_message_handler(Comment, state=Form.comment)
dp.register_message_handler(sozlamalar, state='nomer_2')
# ___________________________________________________________________________________

#__CONTENT_TYPES_____________________________________________________________________
dp.register_message_handler(giv_code3, state='nomer1')


dp.register_message_handler(lokatsion, content_types='location', state='*')
dp.register_message_handler(giv_code, content_types=['text'], state='*')


# =============================CALBACK QUERYS==================================================
dp.register_callback_query_handler(buyurtma_berish, text="buyurtma_berish", state='*')
dp.register_callback_query_handler(telefon, text='telefon', state='*')
dp.register_callback_query_handler(til_2, text="O'zbekcha 🇺🇿", state='*')
dp.register_callback_query_handler(til_2, text="Русский 🇷🇺", state='*')
dp.register_callback_query_handler(til_tanlash, text='muloqot_tili', state='*')
dp.register_callback_query_handler(foydalanuvchi_buyurtmalari, text="buyurtmalarim", state='*')
dp.register_callback_query_handler(biz_haqimizda, text="biz_haqimizda",state='*')
dp.register_callback_query_handler(fikir, text="Fikir",state='*')
dp.register_callback_query_handler(sozlamalar,text="sozlamalar",state='*')
dp.register_callback_query_handler(giv_code2, text="Asosiymenu",state='*')
dp.register_callback_query_handler(filiyallar, text="Filyallar",state='*')
dp.register_callback_query_handler(algortm, text="algoritm",state='*')
dp.register_callback_query_handler(andijon, text="andijon-1",state='*')
dp.register_callback_query_handler(bektemir, text="bektemir",state='*')
dp.register_callback_query_handler(beruniy, text="beruniy",state='*')
dp.register_callback_query_handler(bodomzor, text="bodomzor",state='*')
dp.register_callback_query_handler(chilonzor19, text="chilonzor19",state='*')
dp.register_callback_query_handler(chilonzor_metro, text="chilonzor_metro",state='*')
dp.register_callback_query_handler(chinoz, text="chinoz",state='*')
dp.register_callback_query_handler(chirchik, text="chirchik",state='*')
dp.register_callback_query_handler(chopon_ota, text="chopon_ota",state='*')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)